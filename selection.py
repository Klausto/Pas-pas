#!/usr/bin/env python
import cv2
import os
import button
import playing

def  count_files(path):

    ret = len(os.listdir(path))
    return ret

def  build_selection(cursor, path, models_number):

    i = cursor
    path_end = "/1.png"

    if models_number < 1:
        print "There are no models."
        return

    ## Loads the images we will need to build the interface;
    ## background + the first image of the models in the
    ## directory pointed by cursor and its neighbors

    final_img = cv2.imread("background2.png", 1)
    cv2.imshow('window', final_img)
    cv2.waitKey(10)
    imgprinc = cv2.imread(path + str(i % models_number + 1) + path_end, 1)
    img2 = cv2.imread(path + str((i + 1) % models_number + 1) + path_end, 1)
    img3 = cv2.imread(path + str((i + 2) % models_number + 1) + path_end, 1)
    img4 = cv2.imread(path + str((i - 1) % models_number + 1) + path_end, 1)
    img5 = cv2.imread(path + str((i - 2) % models_number + 1) + path_end, 1)

    ## Resizes the images to their final size in the interface

    imgprinc = cv2.resize(imgprinc, None, fx=0.4, fy=0.4, interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img2, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_LINEAR)
    img4 = cv2.resize(img4, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_LINEAR)
    img3 = cv2.resize(img3, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_LINEAR)
    img5 = cv2.resize(img5, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_LINEAR)

    ## Puts the resized images in the interface image

    final_img[250:660, 385:897] = imgprinc   ## img_princ at the center

    final_img[380:503, 915:1069] = img2      ## img2 at right of img_princ
    final_img[390:492, 1092:1220] = img3     ## img3 at right of img2 (2x right of img_princ)

    final_img[380:503, 203:357] = img4       ## img4 at left of img_princ
    final_img[390:492, 52:180] = img5        ## img5 at left of img2 (2x left of img_princ)

    cv2.imshow('window', final_img)          ## Display final_img
    cv2.waitKey(200) 
    return

def select_cartoon(path, mode):

    button_value = 0
    cartoon_selector = 0
    cartoons_number = count_files(path)
    c_path = path + "pap_"
    cartoon = []

    while (len(cartoon) == 0):
        build_selection(cartoon_selector, c_path, cartoons_number)
        button_value = button.waitpressedbutton(mode)
        if (button_value == "mode"):
            return None
        if (button_value == "next"): # next
            cartoon_selector += 1
        elif (button_value == "prev"): # prev
            cartoon_selector -= 1
        elif (button_value == "play"): # play
            return playing.load_selected(c_path + str(cartoon_selector % cartoons_number + 1) + "/")
