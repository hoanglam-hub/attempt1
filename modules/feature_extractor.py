import numpy as np
import cv2
from utils import ear_calculate, mar_calculate
from configs import left_eye_ear_index, right_eye_ear_index, lip_mar_index, FACE_LANDMARKS, FACE_3D

class FeatureExtractor:
    def extract(self, coordinates, frame_h, frame_w):
        left_EAR = ear_calculate(left_eye_ear_index, coordinates)
        right_EAR = ear_calculate(right_eye_ear_index, coordinates)
        EAR = (left_EAR + right_EAR) / 2
        MAR = mar_calculate(lip_mar_index, coordinates)

        face_2D_points = np.array([coordinates[i] for i in FACE_LANDMARKS])
        camera_matrix = np.array(
            [
                [frame_w, 0, frame_w / 2],
                [0, frame_w, frame_h / 2],
                [0, 0, 1]
            ], dtype=np.float64
        )
        dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
        # solve PnP
        success, rotation_vector, translation_vector = cv2.solvePnP(np.array(FACE_3D), face_2D_points, camera_matrix,
                                                                    dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
        # Convert rotation vector to rotation matrix
        rmat, _ = cv2.Rodrigues(rotation_vector)
        # Get Euler angles
        (pitch, yaw, roll), _, _, _, _, _ = cv2.RQDecomp3x3(rmat)  # x, y, z

        raw_features = np.array([MAR, EAR, pitch, yaw, roll])

        return raw_features

#





