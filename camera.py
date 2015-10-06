#!/usr/bin/env python
import cv2
import os

ramp_frame = 30
#cam = cv2.VideoCapture(0)
dir = 'image_pap'

#print cam.get(3), cam.get(4)

def get_image():
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,512)
    retval, im = cam.read()
    cam.release()
    cv2.waitKey(500)
    im = cv2.resize(im, None, fx = 2, fy = 2.134)
    return (im)

# def make_interface(file):

#         img = cv2.imread(os.path.join(dir, str(file) + ".png"))
#         background = cv2.imread("background.png", 1)
#         background[200:680, 300:940] = img
#         cv2.namedWindow("last picture", cv2.WND_PROP_FULLSCREEN)
#         cv2.setWindowProperty("last picture", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
#         cv2.imshow("last picture", background)
#         cv2.waitKey(0)

# def capture_picture_movie():
#     count_img = 0
#     while (count_img < 10):
#         file = count_img
#         cv2.waitKey(0)
#         for i in xrange(ramp_frame):
#          temp = get_image()
#         print("Taking image")
#         print("image " + str(count_img) + ".png")
#         camera_capture = get_image()
#         cv2.imwrite(os.path.join(dir, str(file) + ".png"), camera_capture)
#         make_interface(file)
#         cv2.destroyAllWindows()
#         count_img = count_img + 1

