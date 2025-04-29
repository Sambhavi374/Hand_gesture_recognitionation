import streamlit as st
from camera_input_live import camera_input_live

st.header("Camera Input Live Demo")

# Live feed
frame = camera_input_live(key="cam1",debounce=200)

if frame is not None:
    st.image(frame)
else:
    st.warning("Waiting for camera permission…")


