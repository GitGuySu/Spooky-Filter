import cv2 as cv
import time

video = cv.VideoCapture(0)
first_frame = None

while True:
    check,frame = video.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray  #the first frame that is captured is taken as reference
        continue            #loop starts again

    delta_frame = cv.absdiff(first_frame,gray)
    cv.imshow("spooky !!!!", delta_frame)
    key = cv.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv.destroyAllWindows()
