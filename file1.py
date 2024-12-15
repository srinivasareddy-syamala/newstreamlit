import streamlit as st

st.title("This is my first streamlit page")
st.file_uploader("please select the file",type=["*"])
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
