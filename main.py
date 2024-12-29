import streamlit as st
import cv2
from ultralytics import solutions
import os

# Streamlit app title
st.title("Speed Estimation App 🤖")
st.caption("Upload your video, and get vehicle speed results!")

st.sidebar.header("Upload Video")
uploaded_file = st.sidebar.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file:
    # Save the uploaded video to a temporary file
    with open("uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    st.sidebar.info("Processing video...")

    # Open the video
    cap = cv2.VideoCapture("uploaded_video.mp4")
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    # Prepare the output video writer
    output_video_path = "output/processed_video.avi"
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"XVID"), fps, (w, h))

    # Initialize SpeedEstimator
    speed_obj = solutions.SpeedEstimator(
        region=[(0, 360), (1480, 360)],
        model="yolo11n.pt",
        show=False,  # No live display during Streamlit processing
    )

    # Display placeholder for real-time frame updates
    frame_placeholder = st.empty()

    # Process the video
    frame_count = 0
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Estimate speed and write to output
        processed_frame = speed_obj.estimate_speed(frame)
        video_writer.write(processed_frame)

        # Display the current frame in Streamlit
        frame_bgr = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_bgr, channels="RGB", caption=f"Processing frame {frame_count}")
        frame_count += 1

    # Release resources
    cap.release()
    video_writer.release()

    # Notify user of completion and display the output video
    st.sidebar.success("Processing complete!")
    st.success(f"Video has been processed and saved as `{output_video_path}`.")
    # st.video(output_video_path)

else:
    st.sidebar.info("Please upload a video to get started.")
    st.markdown("### Upload a video using the sidebar to process it.")
