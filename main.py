import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame({
     '1列目':[1,2,3,4],
     '2列目':[10,20,30,40]
})

st.write(df)

st.dataframe(df)

st.dataframe(df,width = 200, height = 100)


df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)

df2

st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [36.69, 139.70],
    columns = ['lat','lon']
)

st.map(df3)

st.write('Display Image')


if st.checkbox('Show Image'):
    potita = Image.open('potita.jpg')

    st.image(potita,caption='potita',use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味:',text

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition

sidetext = st.sidebar.text_input('あなたの趣味を教えてください。2')

sidecondition = st.sidebar.slider('あなたの今の調子は？2',0,100,50)
'あなたの趣味:',sidetext
'コンディション:',sidecondition

left_column, right_column = st.columns(2)

button = left_column.button('右からカラム文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせの回答です')


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(0,100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
