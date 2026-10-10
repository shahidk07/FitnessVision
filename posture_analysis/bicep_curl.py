from .geometry import calculate_angle
import numpy as np

"""
calculate_bicep_curl_angles()
It receives something like:
landmarks = {
    "LEFT_SHOULDER": [x, y],
    "LEFT_ELBOW": [x, y],
    "LEFT_WRIST": [x, y],

    "RIGHT_SHOULDER": [x, y],
    "RIGHT_ELBOW": [x, y],
    "RIGHT_WRIST": [x, y],
}
"""


def calculate_bicep_curl_angles(landmarks):
    left_elbow_angle = calculate_angle(
        landmarks["LEFT_SHOULDER"],
        landmarks["LEFT_ELBOW"],
        landmarks["LEFT_WRIST"],
    )
    right_elbow_angle = calculate_angle(
        landmarks["RIGHT_SHOULDER"],
        landmarks["RIGHT_ELBOW"],
        landmarks["RIGHT_WRIST"],
    )

    return {
        "left_elbow_angle": left_elbow_angle,
        "right_elbow_angle": right_elbow_angle,
    }


def calculate_shoulder_width(landmarks):

    
    """
    Calculate the distance between the left and right shoulders.
    """

    left_shoulder = np.array(landmarks["LEFT_SHOULDER"], dtype=float)
    right_shoulder = np.array(landmarks["RIGHT_SHOULDER"], dtype=float)

    shoulder_width = np.linalg.norm(right_shoulder - left_shoulder)

    return shoulder_width


def calculate_elbow_position(landmarks):
    """
    We want to know:
    How far horizontally is the left elbow from the left shoulder?
    How far horizontally is the right elbow from the right shoulder?
    """

    left_elbow_position = (
        landmarks["LEFT_ELBOW"][0] - landmarks["LEFT_SHOULDER"][0]
    )
    right_elbow_position = (
        landmarks["RIGHT_ELBOW"][0] - landmarks["RIGHT_SHOULDER"][0]
    )

    return {
        "left_elbow_position": left_elbow_position,
        "right_elbow_position": right_elbow_position,
    }


def calculate_elbow_drift(current_position, starting_position):
    left_elbow_drift = (
        current_position["left_elbow_position"]
        - starting_position["left_elbow_position"]
    )
    right_elbow_drift = (
        current_position["right_elbow_position"]
        - starting_position["right_elbow_position"]
    )

    return {
        "left_elbow_drift": left_elbow_drift,
        "right_elbow_drift": right_elbow_drift,
 }

if __name__ == "__main__":

    # Simulated starting frame
    starting_landmarks = {
        "LEFT_SHOULDER": (0.40, 0.30),
        "RIGHT_SHOULDER": (0.60, 0.30),
        "LEFT_ELBOW": (0.42, 0.50),
        "RIGHT_ELBOW": (0.58, 0.50)
    }

    # Simulated current frame
    current_landmarks = {
        "LEFT_SHOULDER": (0.40, 0.30),
        "RIGHT_SHOULDER": (0.60, 0.30),
        "LEFT_ELBOW": (0.45, 0.50),
        "RIGHT_ELBOW": (0.56, 0.50)
    }

    # Calculate starting elbow positions
    starting_position = calculate_elbow_position(
        starting_landmarks
    )

    # Calculate current elbow positions
    current_position = calculate_elbow_position(
        current_landmarks
    )

    # Calculate elbow drift
    drift = calculate_elbow_drift(
        current_position,
        starting_position
    )

    print("Starting position:", starting_position)
    print("Current position:", current_position)
    print("Elbow drift:", drift)