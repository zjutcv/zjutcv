# Copyright (c) ZJUTCV. All rights reserved.
import cv2 as cv


def rgb2gray(src, des=None):
    """
    Transfer the rgb img to gray img
    Args:
        src: source path
        des: output path

    Returns: gray img

    """
    if des is None:
        des = src
    img = cv.imread(src)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(des, gray)
    return gray
