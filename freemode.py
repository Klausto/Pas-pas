#!/usr/bin/env python
import cv2
import selection
import playing
import camera
import image
import button
import RPi.GPIO as GPIO

# Activates the different GPIO inputs that will be used here

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def free_mode():

    takes_list = []

    background = cv2.imread("background2.png", 1)
    cv2.imshow("window", background)
    cv2.waitKey(50)            
    while ("true"):

        mode = GPIO.input(13) # reads the circle switch

        if (mode == False or len(takes_list) < 3):
            cv2.imshow("window", background)
        else:
            cv2.imshow("window", image.averager(takes_list)) # displays a weighed average of the last 3 pictures taken
        cv2.waitKey(100)

        button_value = button.waitpressedbutton("free")

        if (button_value == "mode"):         # The mode is no longer freemode, we have to return to go to the selected mode
            return

        if (button_value == "record"):                        # takes and displays a picture
            cv2.imshow("window", background)
            cv2.waitKey(10)
            takes_list.append(camera.get_image())
            cv2.imshow("window", takes_list[len(takes_list) - 1])
            cv2.waitKey(200)

        if (button_value == "delete" and len(takes_list) > 0): # deletes the last picture taken
            del takes_list[-1]
            cv2.imshow("window", background)
            cv2.waitKey(300)
        if (button_value == "save"):                        # saves the cartoon and returns
            playing.save(takes_list)
            return
        if (button_value == "play"):                        # plays the cartoon
            playing.play(takes_list)
