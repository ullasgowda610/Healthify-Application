import streamlit as st
import google.generativeai as genai
import pandas as pd
import os

api=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

# Lets create the UI
st.title(':orange[HEALTHIFY] :blue[AI  Powered  personal health assistant]')
st.subheader('''This application will assist you to have a better and healthy life you can ask health related questions  and get personalised guidance.''')
tips='''Follow the steps:
* Enter your details in the side bar.
* Enter your name,gender,age,height(cms),weight(kgs).
* Select the number on the fitness scale(0-5). 5-fittest and 0-No fitness at all.
* After filling the deatils write your Query here and get customised response'''
st.write(tips)

# Lets configure sidebar
st.sidebar.header(':blue[ENTER YOUR DETAILS]')
name=st.sidebar.text_input('Enter Your Name')
gender=st.sidebar.selectbox('Select your gender',['Male','Female'])
age=st.sidebar.text_input('Enter your age in years')
weight=st.sidebar.text_input('Enter your weights in kgs')
height=st.sidebar.text_input('Enter your height in cms')
bmi=pd.to_numeric(weight)/(pd.to_numeric(height)/100)**2
fitness=st.sidebar.slider('Rate your fittness between 0-5',0,5,step=1)
st.sidebar.write(f'Your BMI:{round(bmi,2)}kg/m^2')

#Lets use genai model to get the output
user_query=st.text_input('Enter your Question here')
prompt=f'''Assume you are a health expert.You are required to answer the question asked by the user .Use the following details provided by the user.
name of user is {name} 
gender is {gender} 
age is {age}
weight is {weight}
height is {height}
bmi is {bmi}
and user rates his/her fitness as {fitness} out of 5.

Your output should be in the following format
* It start by giving one two line comment on the details that are being provided by the user.
* It should explain what the real problem is based on the query asked by the user
* What could be the possible reason for the problem.
* What are the possible solutions for the problem.
* You can also mention what doctor to see(specialization) if required.
* Strictly do not recommend or advise any medicines.
* Output should be in bullet points and use tables wherever required.
* In the end give 5-7 line of summary of every thing that has been discussed.

here is the query from the user {user_query}'''

if user_query:
    response=model.generate_content(prompt)
    st.write(response.text)
