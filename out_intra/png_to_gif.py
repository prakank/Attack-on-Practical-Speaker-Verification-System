import glob
from PIL import Image
import os
import sys
# from common_import import NUM as num
num = sys.argv[1]

# filepaths

BASE_DIR = os.path.dirname(__file__)

fp_in1 = os.path.join(BASE_DIR, 'step1_png/step1_Num{}_*.png'.format(num))
fp_out1 = os.path.join(BASE_DIR, 'step1_gif/step1_Num{}.gif'.format(num))

fp_in2 = os.path.join(BASE_DIR, 'step2_png/step2_Num{}_*.png'.format(num))
fp_out2 = os.path.join(BASE_DIR, 'step2_gif/step2_Num{}.gif'.format(num))

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif

# for k in sorted(glob.glob(fp_in1), key=lambda x:int((x.split('_')[-1]).split(".")[0])):
#     print(k)

def save_gif(fp_in,fp_out):
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in), key=lambda x:int((x.split('_')[-1]).split(".")[0]))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,save_all=True, duration=50, loop=0)

print('Processing Gif for step1 ...')
save_gif(fp_in1,fp_out1)

print('\nProcessing Gif for step2 ...')
save_gif(fp_in2,fp_out2)

print("\nGif generated successfully!\n")