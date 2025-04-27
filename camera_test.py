import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

# 1. Define the transformer class
class HandGestureTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to an OpenCV image (BGR format)
        img = frame.to_ndarray(format="bgr24")

        # Here you can add your hand gesture detection code
        # For now, let's just draw text
        cv2.putText(img, "Detecting Hand Gestures...", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

        return img

# 2. Streamlit App UI
st.title("✋ Real-time Hand Gesture Recognition")

# RTC Configuration (to disable audio)
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}],
}

# 3. WebRTC Streamer
webrtc_streamer(
    key="hand-gesture",
    video_transformer_factory=HandGestureTransformer,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": True,   # ✅ only video
        "audio": False   # 🚫 no audio
    },
    async_transform=True,  # smoother async frame handling
)


