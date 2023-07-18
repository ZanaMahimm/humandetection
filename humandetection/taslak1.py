import cv2
import glob
import os
import uuid




net=cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model=cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)



#load class lists
classes=[]
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        #print(class_name)
        class_name=class_name.strip()  #satır arası boşluklar için
        
        classes.append(class_name)
         
        
        videos_path = glob.glob('*.mp4')


for video_path in sorted(videos_path):
    print("Processing video: ", video_path)
    cap = cv2.VideoCapture(video_path)
    counter = 0
    save_folder = video_path.split(".")[0]
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    while True:
        ret, frame = cap.read()
        counter += 1
        if not ret:
            break
        
        
        #object detection
        (class_ids, scores, bboxes)=model.detect(frame, confThreshold=0.3, nasThreshold=.4)
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h)=bbox
            cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 50), 3)
            
            class_name=classes[class_id[0]]
            
            cv2.putText(frame, str(class_id), (x, y-10), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 50), 2)
        
        if counter % 5 == 0:
            height= frame.shape[0]
            width=frame.shape[1]
            w=300
            h=300
            
            cv2.imwrite(f"{save_folder}/{str(uuid.uuid4())}.jpg", new1_frame)            
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
    
    cap.release()
    cv2.destroyAllWindows
    
    













