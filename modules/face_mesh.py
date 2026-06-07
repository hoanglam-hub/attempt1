from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

class MeshDetector:
    def __init__(self,model_path):
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)
        self.model = vision.FaceLandmarker.create_from_options(options)

    def detect(self, face_roi):
        mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=face_roi)
        result = self.model.detect(mp_frame)
        if len(result.face_landmarks) == 0:
            return None

        return result.face_landmarks[0]
