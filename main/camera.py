import cv2 as cv

# print(f"wel come {user_name}")

class cmera():
    def __init__(self):
        self.video_capture = cv.VideoCapture(0)

        while True:
            ret,frame = self.video_capture.read()
            cv.imshow('frame',frame)
            if cv.waitKey(0) & 0xFF == ord('q'):
                break
        cv.destroyAllwindows()
        self.video_capture.release()

obj=cmera()

