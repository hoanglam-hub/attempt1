from ultralytics import YOLO

class FaceDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model.predict(
            source=frame,
            conf=0.5,
            device='cpu',
            verbose=False
        )

        boxes = results[0].boxes
        if len(boxes) == 0:
            return None

        x1, y1, x2, y2 = map(int, boxes[0].xyxy[0].cpu().numpy())

        return x1, y1, x2, y2