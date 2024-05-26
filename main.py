import streamlit as st
import time
st.title('Name')
name = st.text_input('Your name: ')
btn = st.button('Proceed','primary')
if name is not None and btn:
  pr = st.progress(0)
  for i in range(101):
    pr.progress(i)
    time.sleep(.003)
  st.write('Hello, ' + name)

