#!/usr/bin/env python

import cv2
import os.path
import selection
import playing
import camera
import image
import button

import RPi.GPIO as GPIO

# Activates the different GPIO inputs that will be used

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def assisted_mode():

      # The model is loaded first
    model_list = selection.select_cartoon("/media/PAP/models/", "assisted")
    if model_list == None:
        return

    takes_list = []
    background = cv2.imread("background2.png", 1)
    model_cursor = 0
    takes_cursor = 0

    # When this condition is false, the program saves automatically the cartoon and returns
    while (len(model_list) > len(takes_list)):

        if ((GPIO.input(6) == False) or (len(takes_list) == 0)):
            cv2.imshow("window", model_list[model_cursor % len(model_list)])
            cv2.waitKey(100)
        else:
            cv2.imshow("window", takes_list[takes_cursor % len(takes_list)])
            cv2.waitKey(100)

        # I move the window again because of a window issue, that still occurs the first time model_cursor = 1
        cv2.moveWindow("window", 0, -30)

        button_value = button.waitpressedbutton("assisted")
        if (button_value == "mode"):
            return

        if (button_value == "record"):                        # take the picture
            model_cursor += 1
            cv2.imshow("window", background)
            cv2.waitKey(20)
            takes_list.append(camera.get_image())

        if (button_value == "delete" and len(takes_list) > 0): # delete the last picture from takes_list
            del (takes_list[-1])
            cv2.waitKey(300)

        if (button_value == "save"):                           # save the cartoon and returns
            if not os.path.exists("/media/PAP/cartoons"):
                cv2.imshow("window", cv2.imread("./save_failed"))
                cv2.waitKey(100)
            else:
                playing.save(takes_list)
                return

        if (button_value == "play"):                        # plays the cartoon
            playing.play(takes_list)
        if (button_value == "next"):                        # move to next image
            if (GPIO.input(6) == False):
                model_cursor += 1
            else:
                takes_cursor += 1
            cv2.waitKey(100)

        if (button_value == "prev"):                        # move to previous image
            if (GPIO.input(6) == False):
                model_cursor -= 1
            else:
                takes_cursor -= 1
            cv2.waitKey(100)
    
    # end of while loop, save and return
    if not os.path.exists("/media/PAP/cartoons"):
        cv2.imshow("window", cv2.imread("./save_failed"))
        cv2.waitKey(100)
    else:
        playing.save(takes_list)
        return
