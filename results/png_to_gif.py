import glob
from PIL import Image
import os
import sys
# from common_import import NUM as num
num = 12

# filepaths

BASE_DIR = os.path.dirname(__file__)

fp_in1 = os.path.join(BASE_DIR, 'steppp/f_*.png')
fp_out1 = os.path.join(BASE_DIR, 'step1_gif/step1_Num{}.gif'.format(num))


def save_gif(fp_in, fp_out):
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in),
                                                key=lambda x:int((x.split('_')[-1]).split(".")[0]))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=10, loop=0)


print('Processing Gif for step1 ...')
save_gif(fp_in1, fp_out1)


print("\nGif generated successfully!\n")
