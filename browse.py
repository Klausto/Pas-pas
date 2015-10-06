#!/usr/bin/env python
import cv2
import os.path
import selection
import playing
import button
import RPi.GPIO as GPIO

# Activates the different GPIO inputs that will be used here

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def browse_mode():

    cartoon_selector = 0
    cartoon = []
    cartoon_cursor = 1

    cartoons_number = selection.count_files("/media/PAP/cartoons/")
    c_path = "/media/PAP/cartoons/pap_"

    # if no USB key named PAP containing cartoons is found, displays an error and returns.
    # This will crash if it contains images that are not names pap_x and are not 1280 / 1024 size.
    if not os.path.exists("/media/PAP/cartoons/"):
        cv2.imshow("window", cv2.imread("./load_failed.png"))
        cv2.waitKey(0)
        return

    while (len(cartoon) == 0):
        cv2.imshow("window", cv2.imread("background2.png"))
        cv2.waitKey(10)
        
        # builds and displays the image containing thumbnails of the cartoons
        selection.build_selection(cartoon_selector, c_path, cartoons_number)
        cv2.waitKey(10)
        button_value = button.waitpressedbutton("browse")

        if (button_value == "mode"):  # the mode is no longer browse, so we return to go to the right mode
            return
        if (button_value == "next"): # sets the cursor to the next cartoon
            cartoon_selector += 1
        elif (button_value == "prev"): # sets the cursor to the previous cartoon
            cartoon_selector -= 1
        elif (button_value == "play"): # plays the cartoon
            cartoon = playing.load_selected(c_path + str(cartoon_selector % cartoons_number + 1) + "/")
            playing.play(cartoon)
