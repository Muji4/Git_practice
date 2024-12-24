from ultralytics import YOLO

model = r""

input = r""

res = model.predict(input,save= True,show_labels= True,conf=0.5)