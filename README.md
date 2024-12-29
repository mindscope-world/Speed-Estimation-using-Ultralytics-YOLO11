# Speed Estimation App

A Streamlit-based web application for real-time speed estimation in uploaded videos. Users can upload videos, view the real-time processing of each frame, and download the processed video once completed.

## Features
- Upload videos via the sidebar.
- Real-time display of processed frames during video analysis.
- Save the processed video in the output folder as `output/processed_video.avi`.
- Display the final processed video after completion.

## Prerequisites
Make sure the following libraries are installed:
- **Streamlit**: For building the user interface.
- **OpenCV**: For video processing.
- **Ultralytics**: For speed estimation using a pre-trained model.

Install the required libraries using pip:
```bash
pip install streamlit opencv-python ultralytics
```

## Installation
1. Clone this repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Save the code as `app.py` in the project directory.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser using the URL provided by Streamlit (usually `http://localhost:8501`).

## How It Works
1. **Upload Video**: Use the sidebar to upload a video file (`.mp4`, `.avi`, `.mov`).
2. **Real-Time Processing**: The app processes the video frame by frame, displaying each processed frame in real-time.
3. **Save & Display**: The processed video is saved as `processed_video.avi` in the root directory and displayed in the app after processing.

## File Structure
```
.
├── app.py               # Main application file
├── sample_videos/uploaded_video.mp4   # Temporarily stored uploaded video
├── output/processed_video.avi  # Output video after processing
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## Requirements File (`requirements.txt`)
```text
streamlit
opencv-python
ultralytics
```

## Demo
![App Screenshot](https://via.placeholder.com/800x400?text=Add+a+demo+image+or+GIF+here)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
Developed by Paul Ndirangu.

## Acknowledgments
- [Ultralytics](https://github.com/ultralytics) for the speed estimation model.
- [Streamlit](https://streamlit.io/) for the easy-to-build web interface.
- [OpenCV](https://opencv.org/) for efficient video processing.
```
