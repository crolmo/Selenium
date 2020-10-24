# -*- coding: utf-8 -*-

import os
import yaml


def listdir(dir_path):
    paths = []
    if os.path.isdir(dir_path):
        for dirname, dirnames, filenames in os.walk(dir_path):
            for file_name in filenames:
                file_path = os.path.join(dirname, file_name)
                if os.path.isfile(file_path):
                    paths.append(file_path)
    elif os.path.isfile(dir_path):
        paths.append(dir_path)
    return paths


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()

    return config


def abs_path(path):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    return PATH(path)