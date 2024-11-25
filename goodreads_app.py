import streamlit as st
import pandas as pd

st.title('Analysis of Reading')
st.subheader('Web version')

file= st.file_uploader('import data')
if file == None:
	book_df= pd.read_csv('goodreads_history.csv')
	st.write('default file')
else:
	book_df= pd.read_csv(file)
	st.write('your file')
	
st.write(book_df.head())




