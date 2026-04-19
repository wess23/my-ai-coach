import streamlit as st
from google import genai

st.title("Coach AI DZ 🇩🇿")

# إدخال البيانات في الفرونت اند
weight = st.number_input("الوزن (كغ)", min_value=40)
height = st.number_input("الطول (سم)", min_value=100)

if st.button("أعطني الخطة"):
    client = genai.Client(api_key="AIzaSyBke1UDZe03kCP324MyKFjHicAhjzBbDvU")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"اعطني خطة فقدان وزن لشاب جزائري وزنه {weight} وطوله {height}. أجب بالدارجة الجزائرية."
    )
    st.write(response.text)