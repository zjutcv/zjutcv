# Copyright (c) ZJUTCV. All rights reserved.
def points2xyxy(points):
    """

    Args:
        points (list):

    Returns:

    """
    x_list = [points[i] for i in range(0, 8, 2)]
    y_list = [points[i] for i in range(1, 8, 2)]
    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list)
    return [x_min, y_min, x_max, y_max]


def zoom_bbox(bbox: list, ratio: float):
    """

    Args:
        bbox:
        ratio:

    Returns:

    """
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    return [
        bbox[0] - w * ratio, bbox[1] - h * ratio, bbox[2] + w * ratio,
        bbox[3] + h * ratio
    ]
