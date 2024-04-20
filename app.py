from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompts):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompts[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompts=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name district and has the following columns - NAME, POPULATION, 
    SEX RATIO \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM district ;
    \nExample 2 - Tell me all the sex ratio of North Delhi?, 
    the SQL command will be something like this SELECT SEX RATIO FROM district 
    where name="North Delhi"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="TEXT TO SQL")
st.header("Database contains district population,sex ratio and literacy rate")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompts)
    print(response)
    st.subheader("The query will be: ")
    st.header(response)
    main_response=read_sql_query(response,"district.db")
    st.subheader("The Response is: ")
    for row in main_response:
        print(row)
        st.header(row)