#!/usr/bin/python
import os
import pprint
import subprocess

src_dir = './datas/LibriSpeech/test-clean/'
dst_dir = './data/cod310/LibriSpeech_dataset/test_clean/wav'

for root, dirs, files in os.walk(src_dir):
    for f in files:
        prefix, suffix = os.path.splitext(f)
        if '.flac' == suffix:
            abspath_in = root + '/' + f
            dir_out = dst_dir
            if not os.path.exists(dir_out):
                os.makedirs(dir_out)
            abspath_out = dir_out + '/' + prefix + '.wav'
            subprocess.call(['ffmpeg', '-i', abspath_in, abspath_out])