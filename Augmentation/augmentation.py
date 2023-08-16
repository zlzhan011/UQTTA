import os

import cv2
import numpy as np
import add_both_lines
import add_horizontal_lines
import add_vertical_lines
import remove_lines


def augment_image(img):
    img_nolines = remove_lines.removeLines(img)      # remove all the lines in the image
    img_vertical_lines = add_vertical_lines.addVerticalLines(img_nolines)  # adds vertical lines to the image with no lines
    img_horizontal_lines = add_horizontal_lines.addHorizontalLines(img_nolines) # adds horizontal lines to the image with no lines
    img_both_lines = add_both_lines.addHorizontalVerticalLines(img_nolines) # adds both horizontal and vertical lines to the image with no lines
    return img, img_nolines, img_vertical_lines, img_horizontal_lines, img_both_lines

def aug_process(origin_img_path):
    _img_nolines = origin_img_path + '_img_nolines'
    _img_vertical_lines = origin_img_path + '_img_vertical_lines'
    _img_horizontal_lines = origin_img_path + '_img_horizontal_lines'
    _img_both_lines = origin_img_path + '_img_both_lines'
    dir_list = [_img_nolines, _img_vertical_lines, _img_horizontal_lines, _img_both_lines]
    for dir in dir_list:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    for item in os.listdir(origin_img_path):
        img = cv2.imread(os.path.join(origin_img_path, item))
        img, img_nolines, img_vertical_lines, img_horizontal_lines, img_both_lines = augment_image(img)

        cv2.imwrite(os.path.join(_img_nolines, item),img_both_lines)
        cv2.imwrite(os.path.join(_img_vertical_lines, item), img_vertical_lines)
        cv2.imwrite(os.path.join(_img_horizontal_lines, item), img_horizontal_lines)
        cv2.imwrite(os.path.join(_img_both_lines, item), img_both_lines)
    return _img_nolines, _img_vertical_lines, _img_horizontal_lines, _img_both_lines

if __name__ == '__main__':
    img_path = 'test_data/cTDaR_t10001_1.jpg'
    c_root = r'/data/cs_lzhan011/project/mmdetection/data/Cell_split_train_test/Cell_images'
    origin_img_path = os.path.join(c_root,'output_image_only_cell_test')
    origin_img_path = os.path.join(c_root, 'output_image_only_cell_train')
    aug_process(origin_img_path)


