import os

import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_array_equal

import zjutcv


def test_rgb2gray():
    in_img = np.random.rand(10, 10, 3).astype(np.float32)
    out_img = zjutcv.rgb2gray(in_img)
    computed_gray = (
            in_img[:, :, 0] * 0.299 + in_img[:, :, 1] * 0.587 +
            in_img[:, :, 2] * 0.114)
    assert_array_almost_equal(out_img, computed_gray, decimal=4)

    out_img_3d = zjutcv.rgb2gray(in_img, True)
    assert out_img_3d.shape == (10, 10, 1)
    assert_array_almost_equal(out_img_3d[..., 0], out_img, decimal=4)

    zjutcv.rgb2gray('./resources/zjutcv.jpg', des='./temp/zjutcv_gray.jpg')
    assert os.path.isfile('./temp/zjutcv_gray.jpg')
    os.remove('./temp/zjutcv_gray.jpg')







