import numpy as np

def calculate_angle(a,b,c):
    """
    Calculate angle 
     Calculate angle ABC in degrees.

    a, b, c are points represented as:
        [x, y]
        position vectors
    or:
        [x, y, z]
    """

    a = np.array(a,dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    """for representing the elbow angle
        we need  ba and bc"""
    #we want the vector from b to a 
    #we can calculate BA Vector=A-B
    ba = a-b
    bc = c-a

    #cos(theta)=ba.bc/|ba|*|bc|
    #calculate the denominator 
    denominator =np.linalg.norm(ba)* np.linalg.norm(bc)
    """
    np.linalg.norm(ba)=calculate the length(magnitude) of ba
    np.linalg.norm(bc)=calculate the length(magnitude) of bc
    """
    #check whether the denominator is zero
    if denominator==0:
        return None

    cosine_angle=np.dot(ba,bc)/denominator
    # Protect afainst floating-point errror
    # mathematically -1 ≤ cos(θ) ≤ 1
    cosine_angle=np.clip(cosine_angle,-1.0,1.1)
    # np.clip() forces the number into: [-1,1]
    
    # calculate the angle(theta)
    angle=np.degrees(np.arccos(cosine_angle))
    # arccos() does inverse cosine.->return the value in radians
    # np.degrees() converts radians into degrees.
    
    return angle


def calculate_torso_angle(landmarks):
    """
    Calculate the torso's deviation from vertical.

    Uses the midpoint of the shoulders and the midpoint of the hips.
    """ 

    shoulder_midpoint = (
        (landmarks["LEFT_SHOULDER"][0] +
         landmarks["RIGHT_SHOULDER"][0]) / 2,

        (landmarks["LEFT_SHOULDER"][1] +
         landmarks["RIGHT_SHOULDER"][1]) / 2
    )

    hip_midpoint = (
        (landmarks["LEFT_HIP"][0] +
         landmarks["RIGHT_HIP"][0]) / 2,

        (landmarks["LEFT_HIP"][1] +
         landmarks["RIGHT_HIP"][1]) / 2
    )