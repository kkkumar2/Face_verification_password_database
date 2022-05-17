# Face_verification_password_database
This project uses facial recognition and extract vectors from face and use that to encrpyt passwords



Libraryies:
	1) streamlit,mongodb,predefined algorithm with custom key

research:

detection:
	1) Haar cascade (xml file) bounding box not working 
	2) MTCNN     bounding box + KEYPOINTS  not needed 
	3) Deepface  not needed 
	4) DLIB 

training models :
	1) HOG + SVM (DLIB or face_Recognition)
	2) DEEPFACE(VGGNET,FACENET,ETC) use neural networks for only feature extraction
	
similarity:
	1) COSINE SIMILARITY use it from sklearn

Hashing :
	1) using predefined model 


open camera 10 images training part,train 

create a average feature vectors store it in database


camera popup fetch last frame 

fetch one frame find its similrarity 

if score is set 70% 
go to new page where user enter the credential detials

add view 

	add
hash it and store it in database , use top average vector for hashing 
	save 

	view 
	close



we can use database reddit

encryption = one key 

public key , private key 

cryptography , 

rsa public key , 



library ,
 

```bash
structure :

Data :
	person folder name:
		iamges

src(package folder)
	utils - folder
	CRUD.py    for mongodb
	predict.py  
	feature_extractor.py
	detect_Faces.py
	encryption.py	 
	
streamlit.py 
run.py
setup.py
requirements.txt
environmental.yml
```