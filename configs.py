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
