# import cv2 as cv
# from ultralytics import YOLO
#
# # print(f"wel come {user_name}")
# model = YOLO("/home/parshav/finalproject/peanutsdetectionsystem/my_model.pt")
# class cmera:
#     def __init__(self,img):
#         self.img = cv.imread(img)
#
#         frame_count = 0
#
#         while True:
#             # ret, frame = self.videoCap.read()
#             # if not ret:
#             #     break
#             results = model(self.img)
#
#             for result in results:
#                 class_names = result.names
#                 for box in result.boxes:
#                     if box.conf[0] > 0.4:
#                         x1, y1, x2, y2 = map(int, box.xyxy[0])
#
#                         cls = int(box.cls[0])
#                         class_name = class_names[cls]
#
#                         conf = float(box.conf[0])
#
#
#                         cv.rectangle(self.img, (x1, y1), (x2, y2), (0,0,255), 2)
#
#                         cv.putText(self.img, f"{class_name} {conf:.2f}",
#                                     (x1, max(y1 - 10, 20)), cv.FONT_HERSHEY_SIMPLEX,
#                                     0.6, (0,0,255), 2)
#
#
#                 cv.imshow("myframe",self.img)
#                 cv.imwrite("file.png",self.img)
#
#
#             frame_count += 1
#
#         # self.videoCap.release()
#
# obj=cmera("78.jpg")
#
import cv2 as cv
from ultralytics import YOLO

model = YOLO("/home/parshav/finalproject/peanutsdetectionsystem/my_model.pt")
count=0

class Camera:
    def __init__(self, img_path):
        self.image = cv.imread(img_path)

        if self.image is None:
            raise FileNotFoundError(f"Cannot load image: {img_path}")

        results = model(self.image)

        for result in results:
            class_names = result.names

            for box in result.boxes:
                conf = float(box.conf[0])

                if conf > 0.4:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cls = int(box.cls[0])
                    class_name = class_names[cls]

                    cv.rectangle(
                        self.image,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        2
                    )

                    cv.putText(
                        self.image,
                        f"{class_name} {conf:.2f}",
                        (x1, max(y1 - 10, 20)),
                        cv.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2
                    )

        cv.imshow("Detection", self.image)
        cv.imwrite(f"file{self.image}.png", self.image)



        cv.waitKey(0)
        cv.destroyAllWindows()



# obj = Camera("/home/parshav/finalproject/peanutsdetectionsystem/78.jpg")
ong = Camera("/home/parshav/finalproject/peanutsdetectionsystem/27.jpg")