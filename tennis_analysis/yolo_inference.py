from ultralytics import YOLO

model = YOLO("yolov8x")

result = model.predict('tennis_analysis/input_videos/input_video.mp4', save=True)

print(result)

for box in result:
    print(box)