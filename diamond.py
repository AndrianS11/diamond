import pickle
import streamlit as st

diamond_model = pickle.load(open('diamond_model.sav','rb'))

st.title('Estimasi Harga Diamond')
st.caption('Andrian Herbert Parsaoran Sitohang | 201351150')


carat = st.number_input ('Input Carat Berlian')
depth = st.number_input('Input Depth Berlian')
table = st.number_input('Input Table Berlian')
x = st.number_input('Input Nilain X')
y = st.number_input('Input Nilai Y')
z = st.number_input('Input Nilai Z')

predict = ''

if st.button('Estimasi Harga Belian') :
    predict = diamond_model.predict([[carat,depth,table,x,y,z]])

    st.write('Estimasi Harga Diamond dalam USD :', predict)
    st.write('Estimasi Harga Diamond dalam IDR :', predict*15000)
    