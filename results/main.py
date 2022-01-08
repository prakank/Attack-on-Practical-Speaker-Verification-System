import sys
import os
from PIL import Image
import glob
import matplotlib.pyplot as plt
import pickle
import numpy as np

name = 'feat-1-Num12'

file = open('spectrogram_feat_1_Num12.pkl', 'rb')

picklfile = pickle.load(file)
print(picklfile)
# plot the spectrogram of the first audio file
print(picklfile.keys())
try:
    os.mkdir(name)
except:
    pass
for key in picklfile.keys():
    print(key)
    plt.figure()
    plt.yticks(np.arange(-45, 45, 10))
    # plt.ylim(-20, 30)
    plt.plot(list(picklfile[key].reshape(-1)))
    # add text to the plot
    plt.title(key)
    plt.savefig('./'+name+'/f_'+key+'.png')
    plt.close()

# filepaths

BASE_DIR = os.path.dirname(__file__)

fp_in1 = os.path.join(BASE_DIR, './'+name+'/*.png')
fp_out1 = os.path.join(BASE_DIR, '{}.gif'.format(name))


def save_gif(fp_in, fp_out):
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in),
                                                key=lambda x:int((x.split('_')[-1]).split(".")[0]))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=1, loop=0)


print('Processing Gif for step1 ...')
save_gif(fp_in1, fp_out1)
print("\nGif generated successfully!\n")
