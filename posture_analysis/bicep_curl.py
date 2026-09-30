from .geometry import calculate_angle

""""
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
    left_elbow_angle=calculate_angle(
        landmarks=["LEFT_SHOULDER"],
        landmarks=["LEFT_ELBOW"],
        landmarks=["LEFT_WRIST"]
    )
    right_elbow_angle=calculate_angle(
        landmarks["RIGHT_SHOULDER"],
        landmarks["RIGHT_ELBOW"],
        landmarks["RIGHT_WRIST"]
    )

    return {
        "left_elbow_angle":left_elbow_angle,
        "right_elbow_angle":right_elbow_angle
    }