import pickle

import streamlit as st
st.write("Hello,let register first")
SepalLengthCm=st.number_input("Enter your Sepal Length cm")
SepalWidthCm=st.number_input("Enter your Sepal Width cm")
PetalLengthCm=st.number_input("Enter your Petal Length cm")
PetalWidthCm=st.number_input("Enter your Petal Width cm")
if st.button("Predict"):
    with open(r"C:\Users\My_Pc\Downloads\iris_model.pkl","rb") as file:
        loaded_model = pickle.load(file)
    result=loaded_model.predict([['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']])
    st.write(result)
