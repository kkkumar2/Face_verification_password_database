import streamlit as st
import cv2 
import os
import face_recognition
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
from statistics import mean

def face_extractor(rgb, boxes,type='train'):
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        kEncodings.append(encoding)
        kNames.append(input)
    if type == 'train':
        metadata_path = os.path.join(os.getcwd(),'metadata')
        os.makedirs(metadata_path,exist_ok=True)
        embed_path = os.path.join(metadata_path,'Embeddings.pkl')
        classname_path = os.path.join(metadata_path,'classname.pkl')
        with open(embed_path, 'wb') as f:
            pickle.dump(kEncodings, f)
        with open(classname_path, 'wb') as f:
            pickle.dump(kNames, f)
    else:
        return encodings

def face_detector(count,img,type='train'):
   
    RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(RGB,model='hog') 
      
    for (y1, x2, y2, x1) in boxes:
        cropped_face = RGB[y1:y2, x1:x2]
        cv2.rectangle(RGB, (x1, y1), (x2, y2), (255, 0, 0), 2)
        if type == 'train':
            face = cv2.resize(cropped_face, (200, 200))
            cv2.imwrite(os.path.join(os.getcwd(),'Data',input,'Frame'+str(count)+'.jpg'), face) 
            WINDOW.image(RGB) 
    return RGB,boxes


def fetch_image():
    os.makedirs(os.path.join(os.getcwd(),'Data',input),exist_ok=True)
    msg1 = "Image extraction Started"
    out_msg.text_area("Logging: ", msg1, height=10)
    count = 0
    cap = cv2.VideoCapture(0)
    while True:
        _,frame = cap.read()
        rgb, boxes =  face_detector(count,frame,'train')
        out = face_extractor(rgb, boxes)   
        count+=1    
        if count > 10:
            msg2 = "Image extraction completed"
            out_msg.text_area("Logging: ", msg2, height=10)
            break

def add_data():
    for k, v in name_dict.items():
        name_dict[k] = st.text_input(k, v)
    if name_dict['Username'] != '':
        username = name_dict['Username']
        print(username)
    if name_dict['Password'] != '':
        password = name_dict['Password']  
        print(password)

def view_data():
    pass

def predict():
    print("prediction started")
    metadata_path = os.path.join(os.getcwd(),'metadata')
    embed_path = os.path.join(metadata_path,'Embeddings.pkl')
    classname_path = os.path.join(metadata_path,'classname.pkl')

    embedding = pd.read_pickle(embed_path)
    classname = pd.read_pickle(classname_path)

    count = 0
    cap = cv2.VideoCapture(0)
    while True:
        _,frame = cap.read()
        rgb, boxes =  face_detector(count,frame)
        kEncodings = face_extractor(rgb, boxes,'predict') 
        
        kEncodings = np.array(kEncodings)
        embedding = np.array(embedding)

#        mean_embedding = np.average(embedding)
        score  = cosine_similarity(kEncodings, embedding)
        print(f"Cosine Similarity score is {score}")

        if max(score[0]) * 100 > 90:
            add = st.button("Add",on_click=add_data)
            view = st.button("View",on_click=view_data)
        count+=1    
        if count > 1:
            break


kEncodings = []; kNames = []
st.title("WEBCAM")
WINDOW = st.image([])
input = st.text_input("Enter the name")
take = st.button("Take Images",on_click=fetch_image)
take = st.button("Predict",on_click=predict)
out_msg = st.empty()
name_dict = {"Username":"", "Password":""}



