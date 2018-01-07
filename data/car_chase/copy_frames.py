# -*- coding:utf-8 -*-

from os import listdir, makedirs
from os.path import isdir, join
import shutil

DIR_XYZ_FRAMES = "frames_xyz"
DIR_HSV_FRAMES = "frames_hsv"
DIR_GRAY_FRAMES = "frames_gray"
DIR_EQ_FRAMES = "frames_eq"
DIR_HP_FILTER_FRAMES = "frames_hp_filter"
DIR_LP_FILTER_FRAMES = "frames_lp_filter"
DIR_TRANSFORMED = "../../../transform_frames"
DIR_FRAMES = "JPEGImages"


def make_dirs(dir_names):
    for dir_name in dir_names:
        shutil.rmtree(dir_name, ignore_errors=True)
        try:
            makedirs(dir_name)
        except OSError:
            if not isdir(dir_name):
                raise


def copy_frames(dir_from, dir_to, frame_names):
    for frame_name in listdir(dir_from):
        if frame_name in frame_names:
            path_frame = join(dir_from, frame_name)
            shutil.copy(path_frame, dir_to)


def main():
    directories = [DIR_XYZ_FRAMES, DIR_HSV_FRAMES, DIR_GRAY_FRAMES, DIR_EQ_FRAMES, DIR_HP_FILTER_FRAMES,
                   DIR_LP_FILTER_FRAMES]
    make_dirs(directories)
    frame_names = listdir(DIR_FRAMES)
    for dir_frames in directories:
        copy_frames(join(DIR_TRANSFORMED, dir_frames), dir_frames, frame_names)


if __name__ == "__main__":
    main()
