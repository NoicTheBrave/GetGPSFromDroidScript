import cv2 

cap = cv2.VideoCapture('demo.mp4')#'project.avi')
if cap.isOpened():
    current_frame = 0
    while True:
        ret, frame = cap.read()
        if ret:
            name = f'frameIn/frame{current_frame}.jpg'
            print(f"Creating file... {name}")
            cv2.imwrite(name, frame)
            #frame.append(name)
        current_frame += 1
    cap.release()
cv2.destroyAllWindows()