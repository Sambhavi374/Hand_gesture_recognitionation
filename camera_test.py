import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to a numpy array
        img = frame.to_ndarray(format="bgr24")

        # Perform any processing on the frame (if needed)
        # Example: Add text to the frame
        cv2.putText(img, "Camera Stream", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return img

# Streamlit app
st.title("Camera Input with Streamlit")

# Define STUN/TURN server settings
RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},  # Google's public STUN server
        # Add TURN server if needed
        # {"urls": "turn:your-turn-server.com", "username": "user", "credential": "pass"}
    ]
}

# Start the WebRTC streamer
webrtc_streamer(
    key="camera",
    video_transformer_factory=VideoTransformer,
    rtc_configuration=RTC_CONFIGURATION,
)