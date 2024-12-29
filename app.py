#pip install streamlit
#pip install plotly

#run the app with: streamlit run app.py

import streamlit as st
import pickle
import plotly.express as px

model = pickle.load(open('model.pkl', 'rb'))
# df = pickle.load(open('df.pkl', 'rb'))

st.title("Spam Message Classifier")

input_text = st.text_input("Enter Message")

submit = st.button("Predict")

if submit:
    prediction = model.predict([input_text])

    if prediction[0] == "spam":
        st.warning("This is a Spam message")
    else:
        st.success("This is a legit message")

st.balloons()