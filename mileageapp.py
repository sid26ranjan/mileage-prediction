import streamlit as st
from sklearn.externals import joblib 
import pandas as pd
import webbrowser


model=joblib.load('mileage_model.pkl') 
st.title(' MILEAGE PREDICTION ')

st.write("Details Required")
no_cylinder=st.number_input('enter the number of cylinders',1,16)
hp=st.number_input('enter the Horsepower',1)
acceleration=st.number_input('Time it takes to reach 0-60mph in seconds (Acceleration) ',1.1)
model_year=st.number_input('enter the model year',1)
if model_year <2000:
    model_year=model_year%100
else:
    model_year=100

origin_country = st.selectbox('select the origin of the car',['American','European','Asian'])

if(origin_country=='American'):
    origin=1
elif(origin_country=='European'):
    origin=2
elif(origin_country=='Asian'):
    origin=3

displacement=st.number_input('enter the engine displacement in cc',1.1)

weight=st.number_input('enter the weight in kg  (1lbs=0.453kg )',1.1)

mileage=model.predict([[no_cylinder,hp,acceleration,model_year,origin,displacement,weight]])

st.title(f""" Mileage of the vehicle is""")
st.title(f"""{round(mileage[0],2)} kmpl """)

st.write("    ")
st.write("    ")

if(st.button("Let's connect")):
    webbrowser.open('https://www.linkedin.com/in/siddhant-ranjan-04a6b716b/') 
