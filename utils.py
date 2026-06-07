import math

def euclid_calculate (point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return math.sqrt((x1 - x2)**2+(y1 - y2)**2)

def ear_calculate(list_point, landmarks):
    point = []
    for idx in list_point:
        point.append(landmarks[idx])
    d1 = euclid_calculate(point[1], point[5])
    d2 = euclid_calculate(point[2], point[4])
    d3 = euclid_calculate(point[0], point[3])
    return(d1 + d2)/(2 * d3)

def mar_calculate(list_point, landmarks):
    point = []
    for idx in list_point:
        point.append(landmarks[idx])
    d1 = euclid_calculate(point[1], point[7])
    d2 = euclid_calculate(point[2], point[6])
    d3 = euclid_calculate(point[3], point[5])
    d4 = euclid_calculate(point[0], point[4])
    return (d1 + d2 + d3)/(2 * d4)


def crop_roi(frame_h, frame_w, x1, y1, x2, y2, ratio=0.15):
    face_roi_w = x2 - x1
    face_roi_h = y2 - y1
    x1_pad = x1 - ratio * face_roi_w
    x1_pad = max(0, x1_pad)
    x2_pad = x2 + ratio * face_roi_w
    x2_pad = min(frame_w, x2_pad)
    y1_pad = y1 - ratio * face_roi_h
    y1_pad = max(0, y1_pad)
    y2_pad = y2 + ratio * face_roi_h
    y2_pad = min(frame_h, y2_pad)
    return x1_pad,y1_pad, x2_pad, y2_pad

