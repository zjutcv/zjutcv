# Copyright (c) ZJUTCV. All rights reserved.
import cv2

import mmcv


def save_image(channel_order):

    def warp_out(func):

        def warp(img, *args, des=None):
            # img: np.ndarray and str are available.
            img = mmcv.imread(img, channel_order=channel_order)

            out_img = func(img, *args)
            if des is not None:
                mmcv.imwrite(out_img, des)
            return out_img

        return warp

    return warp_out


@save_image(channel_order='rgb')
def rgb2gray(img, keepdim=False):
    """Convert a BGR image to grayscale image.

    Args:
        img (ndarray): The input image.
        keepdim (bool): False (by default): return the grayscale
                        image with 2 dims (H x W)
                        True : return with 3 dims (H x W x 1)

    Returns:
        gray_img (ndarray): The converted grayscale image.
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if keepdim:
        gray_img = gray_img[..., None]
    return gray_img
