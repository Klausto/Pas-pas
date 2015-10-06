import RPi.GPIO as GPIO
import cv2

# Activates the different GPIO inputs that will be used here

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def waitpressedbutton(mode):
    last_circle = GPIO.input(13)
    last_triangle = GPIO.input(6)
    last_playback = GPIO.input(19)

    # This loop constantly refreshes the various buttons and switches
    # If a button is pressed and catched here, the value is returned immediately
    # If a switch changed position, its value will be returned as well

    while True:
        record_button = GPIO.input(4)
        prev_button = GPIO.input(17)
        next_button = GPIO.input(18)
        delete_button = GPIO.input(27)
        play_button = GPIO.input(22)
        stop_button = GPIO.input(23)
        save_button = GPIO.input(24)

        if (mode == "free" and GPIO.input(13) == False):
            cv2.imshow("window", cv2.imread("background2.png"))

        # If one of these three are detected, this means a change of mode
        if (mode == "free" and GPIO.input(20) != False):
            return "mode"
        if (mode == "assisted" and GPIO.input(26) != False):
            return "mode"
        if (mode == "browse" and (GPIO.input(20) == False or GPIO.input(26) == False)):
            return "mode"

        # Catches the buttons
        if (record_button == False):            
            return "record"
        
        if (prev_button == False):
            return "prev"

        if (next_button == False):
            return "next"

        if (delete_button == False):
            return "delete"

        if (play_button == False):
            return "play"

        if (stop_button == False):
            return "stop"

        if (save_button == False):
            return "save"

        # Catches the switches changes (cirle, triangle and playback)
        # as we use only one per mode, we decided to have a unique return value.
       
        if (last_circle != GPIO.input(13)):
            return "other"
        if (last_triangle != GPIO.input(6)):
            return "other"
        if (last_playback != GPIO.input(19)):
            return "other"

