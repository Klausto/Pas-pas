#!/usr/bin/env python
import cv2
import selection
import RPi.GPIO as GPIO

# Activates the different GPIO inputs that will be needed here

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def load_selected(path):

    img_list = []
    img_number = selection.count_files(path) + 1
    path_end = ".png"

    for i in range (1, img_number):
        img_list.append(cv2.imread((path + str(i) + path_end), 1))
    return img_list

def play(cartoon):

    c_len = len(cartoon)
    i = 0
    
    if c_len == 0:
        return
    while ("true"):
        while (i < c_len):
            cv2.imshow("window", cartoon[i])
            i += 1
            if GPIO.input(23) == False:    # the stop button has been catched
                return
            cv2.waitKey(10)

        # loop mode
        if (GPIO.input(19) == False):
            i = 0

        # back and forth
        else:
            i -= 2
            while (i > 0):
                cv2.imshow("window", cartoon[i])
                if GPIO.input(23) == False:   # the stop button has been catched
                    return
                cv2.waitKey(10)
                i -= 1

def save(cartoon):

    if (len(cartoon) < 1):
        return

    import os
    
    # displays the saving message
    cv2.imshow("window", cv2.imread("saving.png", 1))
    cv2.waitKey(10)

    c_number = selection.count_files("/media/PAP/cartoons/")
    os.makedirs("/media/PAP/cartoons/pap_" + str(c_number + 1))
    for i in range (0, len(cartoon)):
        cv2.imwrite("/media/PAP/cartoons/pap_" + str(c_number + 1) + "/" + str(i + 1) + ".png", cartoon[i]);

    # displays the save success message for 5 seconds
    cv2.imshow("window", cv2.imread("save_success.png", 1))
    cv2.waitKey(5000)
    return
