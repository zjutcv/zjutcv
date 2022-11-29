# Copyright (c) ZJUTCV. All rights reserved.
import random

import numpy as np
from tqdm import tqdm

import mmcv


def random_int_not_in_the_list(exception=[]):
    return random.choice(
        list(
            set(range(max(min(exception) + 1, 0),
                      max(exception) + 2)) - set(exception)))


def split_coco(ann_file: str, percent, out_dir, name='coco'):

    def save_anns(name, images, annotations):
        sub_anns = dict()
        sub_anns['images'] = images
        sub_anns['annotations'] = annotations
        sub_anns['categories'] = anns['categories']

        mmcv.mkdir_or_exist(out_dir)
        mmcv.dump(sub_anns, f'{out_dir}/{name}.json')

    anns = mmcv.load(ann_file)

    np.random.seed(percent)

    image_list = anns['images']

    train_total = int(percent / 100. * len(image_list))
    train_inds = set(
        np.random.choice(
            range(len(image_list)), size=train_total, replace=False))
    train_ids, train_images, test_images = [], [], []

    for i in range(len(image_list)):
        if i in train_inds:
            train_images.append(image_list[i])
            train_ids.append(image_list[i]['id'])
        else:
            test_images.append(image_list[i])

    # get all annotations of labeled images
    train_ids = set(train_ids)
    train_annotations, test_annotations = [], []

    for ann in anns['annotations']:
        if ann['image_id'] in train_ids:
            train_annotations.append(ann)
        else:
            test_annotations.append(ann)

    # save train and test split
    train_name = f'{name}.train@{percent}'
    test_name = f'{name}.test@{100 - percent}'

    save_anns(train_name, train_images, train_annotations)
    save_anns(test_name, test_images, test_annotations)


def merge_coco(anno_file1, anno_file2, out_file):

    def save_anns(name, images, annotations):
        sub_anns = dict()
        sub_anns['images'] = images
        sub_anns['annotations'] = annotations
        sub_anns['categories'] = anns1['categories']

        mmcv.mkdir_or_exist(out_dir)
        mmcv.dump(sub_anns, out_file)

    # assert isinstance(merge_list, [list, tuple])
    anns1 = mmcv.load(anno_file1)
    anns2 = mmcv.load(anno_file2)

    merge_images = anns1['images']
    merge_annotations = anns1['annotations']

    exception_image_ids = []
    for image in merge_images:
        exception_image_ids.append(image['id'])

    exception_annotation_ids = []
    for ann in merge_annotations:
        exception_annotation_ids.append(ann['id'])

    dict_update_inds = {}

    for image in tqdm(anns2['images']):
        temp_num = random_int_not_in_the_list(exception_image_ids)
        exception_image_ids.append(temp_num)
        dict_update_inds[image['id']] = temp_num
        image['id'] = temp_num

    for ann in tqdm(anns2['annotations']):
        updated_image_id = dict_update_inds[ann['image_id']]
        ann['image_id'] = updated_image_id
        # new_anno_id = random_int_not_in_the_list(exception_annotation_ids)
        new_anno_id = max(exception_annotation_ids) + 1
        exception_annotation_ids.append(new_anno_id)
        ann['id'] = new_anno_id

    merge_images += anns2['images']
    merge_annotations += anns2['annotations']

    save_anns(name, merge_images, merge_annotations)
