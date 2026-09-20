import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = '/absolute/path/to/pose_landmarker.task'


import mediapipe as mp

# Get the BaseOptions class from MediaPipe.
# BaseOptions is used to configure the basic settings of the model,
# such as the path to the .task model file.
BaseOptions = mp.tasks.BaseOptions


# Get the PoseLandmarker class from MediaPipe.
# This is the main class responsible for performing human pose estimation.
PoseLandmarker = mp.tasks.vision.PoseLandmarker


# Get the PoseLandmarkerOptions class.
# This class is used to configure how the Pose Landmarker should operate,
# such as its running mode and callback function.
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions


# Get the PoseLandmarkerResult class.
# This represents the result returned by the Pose Landmarker after
# processing an image or video frame.
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult


# Get MediaPipe's RunningMode class.
# It allows us to specify whether we are processing a single image,
# a video, or a live stream.
VisionRunningMode = mp.tasks.vision.RunningMode


# Define the callback function that MediaPipe will call
# whenever a pose result is available.
#
# result:
#     Contains the detected pose information.
#
# output_image:
#     The MediaPipe image associated with the result.
#
# timestamp_ms:
#     Timestamp of the processed frame in milliseconds.
def print_result(
    result: PoseLandmarkerResult,
    output_image: mp.Image,
    timestamp_ms: int
):
    
    # Print the pose-estimation result to the terminal.
    # This is useful for testing whether MediaPipe is detecting a pose.
    print('pose landmarker result: {}'.format(result))


# Create the configuration for our Pose Landmarker.
options = PoseLandmarkerOptions(

    # Specify which trained MediaPipe model should be loaded.
    # model_path should point to our pose_landmarker.task file.
    base_options=BaseOptions(
        model_asset_path=model_path
    ),

    # Tell MediaPipe that we will continuously provide
    # frames from a live source such as a webcam.
    running_mode=VisionRunningMode.LIVE_STREAM,

    # Tell MediaPipe which function to call whenever
    # a pose-estimation result is ready.
    result_callback=print_result
)


# Create and initialize the Pose Landmarker using the options above.
#
# The "with" statement manages the Pose Landmarker resources
# and automatically closes/releases them when this block ends.
with PoseLandmarker.create_from_options(options) as landmarker:

    # At this point, the Pose Landmarker has been initialized.
    # We can now send webcam/video frames to "landmarker".
    pass