from modules import *
from configs import *
from utils import *
import cv2



if __name__ == '__main__':
    face_detector = FaceDetector(model_path=face_detector_path)
    face_mesh = MeshDetector(model_path = face_mesh_path)
    predictor = Predictor(model_path = predictor_path, mean_path = mean_path , std_path=std_path, device=device)
    feature_extractor = FeatureExtractor()
    camera = Camera()

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        box = face_detector.detect(frame)
        if box is not None:
            x1, y1, x2, y2 = box
            frame_h, frame_w = frame.shape[:2]
            x1_pad, y1_pad, x2_pad, y2_pad = crop_roi(frame_h, frame_w, x1, y1, x2, y2, ratio=0.15)
            face_roi = frame[int(y1_pad):int(y2_pad), int(x1_pad):int(x2_pad)]
            face_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)
            face_landmarks = face_mesh.detect(face_roi)

            coordinates = []
            for lm in face_landmarks:
                x = (lm.x * w + x1_pad)
                y = (lm.y * h + y1_pad)
                coordinates.append((x, y))

            feature = feature_extractor.extract(coordinates, frame_h, frame_w)




