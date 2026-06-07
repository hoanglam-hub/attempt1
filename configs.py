# checkpoint
face_detector_path = 'checkpoints/yolov8n-face.pt'
face_mesh_path = 'checkpoints/face_landmarker.task'
predictor_path = 'checkpoints/lstm_model.pth'

# normalization path
mean_path = 'checkpoints/lstm_mean.npy'
std_path = 'checkpoints/lstm_std.npy'

# frame size
frame_width = 640
frame_height = 480
device = 'cpu'

#index
right_eye_ear_index = [33, 159, 158, 133, 153, 145]
left_eye_ear_index = [362, 380, 374, 263, 386, 385]
lip_mar_index = [78, 81, 13, 311, 308, 402, 14, 178]
FACE_LANDMARKS = [1, 152, 263, 33, 291, 57]  # nose, chin, left eye, right eye, left mouth, right mouth
FACE_3D = [
    (0.0, 0.0, 0.0),  # Nose tip
    (0.0, -330.0, -65.0),  # Chin
    (-225.0, 170.0, -135.0),  # Left eye left corner
    (225.0, 170.0, -135.0),  # Right eye right corner
    (-150.0, -150.0, -125.0),  # Left mouth corner
    (150.0, -150.0, -125.0)  # Right mouth corner
]
