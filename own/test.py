from pykos import *

ACTUATOR_NAME_TO_ID = {
    "left_shoulder_yaw": 11,
    "left_shoulder_pitch": 12,
    "left_elbow_yaw": 13,
    "left_gripper": 14,
    "right_shoulder_yaw": 21,
    "right_shoulder_pitch": 22,
    "right_elbow_yaw": 23,
    "right_gripper": 24,
    "left_hip_yaw": 31,
    "left_hip_roll": 32,
    "left_hip_pitch": 33,
    "left_knee_pitch": 34,
    "left_ankle_pitch": 35,
    "right_hip_yaw": 41,
    "right_hip_roll": 42,
    "right_hip_pitch": 43,
    "right_knee_pitch": 44,
    "right_ankle_pitch": 45,
}

ACTUATOR_ID_TO_NAME = {v: k for k, v in ACTUATOR_NAME_TO_ID.items()}


ACTUATOR_IDS = [1,2,3]

KOS("192.168.42.1").actuator.command_actuators([
    {"actuator_id": ACTUATOR_NAME_TO_ID["right_elbow_yaw"], "position": 90.0, "velocity": 100.0, "torque": 1.0}, 
    {"actuator_id": ACTUATOR_NAME_TO_ID["left_hip_yaw"], "position": 180.0}
])

