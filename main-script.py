import pandas as pd
import streamlit as st
import numpy as np

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': ['a','b','c','d']
})

st.write('this is some text')
st.write('this is more text')
st.write(df)

st.write('this is a dataframe')

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20)))
st.dataframe(dataframe)

st.write('this is a table')
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20)))
st.table(dataframe)


st.write('this is a linechart')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c'])
st.line_chart(chart_data)

st.write('this is a map')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [-22, -40.50],
    columns=['lat', 'lon'])
st.map(map_data)
