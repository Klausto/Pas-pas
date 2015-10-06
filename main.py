import RPi.GPIO as GPIO
import cv2
import freemode
import assisted
import browse

# Activates the different GPIO inputs that will be used here

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    while (True):

        # Sets the window. Fullscreen gave us very poor performances, but
        # now we have trouble having the window not moving around
        # in the assisted mode.
        cv2.namedWindow("window", cv2.cv.CV_WINDOW_AUTOSIZE)
        cv2.resizeWindow("window", 1280, 1024)
        cv2.moveWindow("window", 0, -30)

        # Goes the the selected mode
        if (GPIO.input(26) == False):
            assisted.assisted_mode()
        elif (GPIO.input(20) == False):
            freemode.free_mode()
        else:
            browse.browse_mode()
    
main()
