import pandas as pd
import numpy as np
#import streamlit as st
#pip install firebase-admin
from google.cloud import firestore
from google.oauth2 import service_account

db = firestore.Client.from_service_account_json("m3-project-demo.json")

#Conexión a la db segura
#import json
#key_dict = json.loads(st.secrets["textkey"])
#creds = service_account.Credentials.from_service_account_info(key_dict)
#db = firestore.Client(credentials=creds, project="m3-project-demo")

doc_ref=db.collection(u"Alumnos")
#import data
df=pd.read_csv("Machote Inscripciones.csv")
#df=df.drop(["En cuantos proyectos esta el alumno","Unnamed: 3","Plan de estudios"],axis=1)
tmp=df.to_dict(orient="records")
list(map(lambda x: doc_ref.add(x),tmp))