import streamlit as st
from summarizer import summarize_text
from audio_utils import video_to_text

st.title("AI Video & Document Summarizer")

uploaded_file = st.file_uploader("Upload a video (.mp4) or text (.txt) file")

if uploaded_file:
    if uploaded_file.type == "video/mp4":
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.read())
        text = video_to_text("temp_video.mp4")
    else:
        text = uploaded_file.read().decode("utf-8")

    if text:
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)
