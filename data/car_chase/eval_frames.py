# -*- coding:utf-8 -*-

import os
import subprocess
import shutil
import codecs

COMMAND = "../../tools/test_net.py " \
          "--gpu 0 " \
          "--def ../../models/car_chase/test.prototxt " \
          "--net ../../data/coco_models/coco_vgg16_faster_rcnn_final.caffemodel " \
          "--imdb car_chase_val " \
          "--cfg ../../experiments/cfgs/config.yml"

DIR_XYZ_FRAMES = "frames_xyz"
DIR_HSV_FRAMES = "frames_hsv"
DIR_GRAY_FRAMES = "frames_gray"
DIR_EQ_FRAMES = "frames_eq"
DIR_HP_FILTER_FRAMES = "frames_hp_filter"
DIR_LP_FILTER_FRAMES = "frames_lp_filter"
DIR_FRAMES = "JPEGImages"
DIR_FRAMES_BACKUP = "JPEGImages_backup"
DIR_OUTPUT = "EVAL_RESULTS"


def make_dirs(dir_names):
    for dir_name in dir_names:
        shutil.rmtree(dir_name, ignore_errors=True)
        try:
            os.makedirs(dir_name)
        except OSError:
            if not os.path.isdir(dir_name):
                raise


def main():
    os.rename(DIR_FRAMES, DIR_FRAMES_BACKUP)
    directories = [DIR_XYZ_FRAMES, DIR_HSV_FRAMES, DIR_GRAY_FRAMES, DIR_EQ_FRAMES, DIR_HP_FILTER_FRAMES,
                   DIR_LP_FILTER_FRAMES]
    make_dirs([DIR_OUTPUT])
    for dir_frames in directories:
        os.rename(dir_frames, DIR_FRAMES)
        process = subprocess.Popen(COMMAND.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        with codecs.open(os.path.join(DIR_OUTPUT, dir_frames + ".txt"), mode="w", encoding="utf-8") as file_out:
            file_out.write(output)
        os.rename(DIR_FRAMES, dir_frames)
    os.rename(DIR_FRAMES_BACKUP, DIR_FRAMES)


if __name__ == "__main__":
    main()
