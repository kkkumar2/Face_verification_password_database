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

Data
	metadata
	
streamlit
	Dockerfile
	requirements.txt
	streamlit.py
Fastapi 
	Dockerfile
	requirements.txt
	app.py
	utils
		__init.py
		encrypt.py
		all_utils.py 
	webapp
		__init__.py
		schema.py for validations
		router
			__init__.py
			Database.py  route name : /database
			face_controller.py  route name : /controller
			
	Face_recognition
		__init__.py
		Face_detector.py to detect face from webcam
		validation.py   checking if user is already preesnet or not 
		Feature_extract.py if not  present extract feature
		
docker-compose.yml
.env
README.md
LICENSE





verification(1 image)
extract frame and detect faces and crop image
pass crop image to model 
compare it with pickle if present 
close webcam

webcam (10 images)
extract frame and detect faces and crop image
pass crop image to model 
extract features store it in pickle file
close webcam
```

