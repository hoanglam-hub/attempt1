import numpy as np
from utils import ear_calculate, mar_calculate
from configs import left_eye_ear_index, right_eye_ear_index

class FeatureExtractor:
    def __init__(self):
        self.FACE_LANDMARKS = [1, 152, 263, 33, 291, 57]  # nose, chin, left eye, right eye, left mouth, right mouth
        self.FACE_3D = np.array([
            (0.0, 0.0, 0.0),  # Nose tip
            (0.0, -330.0, -65.0),  # Chin
            (-225.0, 170.0, -135.0),  # Left eye left corner
            (225.0, 170.0, -135.0),  # Right eye right corner
            (-150.0, -150.0, -125.0),  # Left mouth corner
            (150.0, -150.0, -125.0)  # Right mouth corner
        ])

    def extract(self, coordinate, frame_h, frame_w):
        left_EAR = ear_calculate(left_eye_ear_index, coordinate)
        right_EAR = ear_calculate(right_eye_ear_index, coordinate)
        EAR = (left_EAR + right_EAR) / 2
        MAR = mar_calculate(lip_mar_index, coordinate)

        face_2D_points = np.array([coordinates[i] for i in self.FACE_LANDMARKS])
        camera_matrix = np.array(
            [
                [frame_w, 0, frame_w / 2],
                [0, frame_w, frame_h / 2],
                [0, 0, 1]
            ], dtype=np.float64
        )
        dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
        # solve PnP
        success, rotation_vector, translation_vector = cv2.solvePnP(self.FACE_3D, face_2D_points, camera_matrix,
                                                                    dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
        # Convert rotation vector to rotation matrix
        rmat, _ = cv2.Rodrigues(rotation_vector)
        # Get Euler angles
        (pitch, yaw, roll), _, _, _, _, _ = cv2.RQDecomp3x3(rmat)  # x, y, z

        raw_features = np.array([MAR, EAR, pitch, yaw, roll])

        return raw_features

#





