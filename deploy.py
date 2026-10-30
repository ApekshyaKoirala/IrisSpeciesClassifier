import streamlit as st
import joblib 

model=joblib.load("model.joblib")
sp_length=st.number_input("Enter sepal length")
sw_width=st.number_input("Enter sepal width")
pl_length=st.number_input("Enter petal length")
pw_width=st.number_input("Enter petal width")
if (st.button("Predict")):
    prediction=model.predict([[sp_length,sw_width,pl_length,pw_width]])[0]
    st.success(f"predicted species is{prediction}")


