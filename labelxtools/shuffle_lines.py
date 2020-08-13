import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import numpy as np
from tqdm import tqdm

import random
root = '/data/hourz/data/data_halmat/lists/train_960_1scene_addvoc_addxianggang.txt'
root_random = '/data/hourz/data/data_halmat/lists/train_960_1scene_addvoc_addxianggang_random.txt'

with open(root_random, 'w') as save:
    with open(root,'r') as fp:
        lines = fp.readlines()
        random.shuffle(lines)
        for line in lines:
            save.write(line)
