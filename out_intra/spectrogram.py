import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from scipy.io import wavfile

import librosa
import librosa.display
from pydub import AudioSegment
from tempfile import mktemp


# from common_import import NUM as num
num = sys.argv[1]


BASE_DIR = os.path.dirname(__file__)

# filename = 'you-got-it-1.wav'
# filename = 'step1/1221_1995.wav'
# filename = 'sound.mp3'
# Method described here https://stackoverflow.com/questions/15311853/plot-spectogram-from-mp3



def plot_mp3_matplot(img_num,filename, save_filename=None):
    """
    plot_mp3_matplot -- using matplotlib to simply plot time vs amplitude waveplot
    
    Arguments:
    filename -- filepath to the file that you want to see the waveplot for
    
    Returns -- None
    """
    
    # sr is for 'sampling rate'
    # Feel free to adjust it
    x, sr = librosa.load(filename, sr=44100)
    
    # fig, ax = plt.subplots()
    
    plt.figure(figsize=(14, 5))
    plt.ylim(-0.04, 0.04)
    
    plt.yticks(np.arange(-0.06, 0.07, 0.02))
    
    librosa.display.waveplot(x, sr=sr, color='r')
    plt.title("Epoch:" + str(img_num))
    plt.savefig(save_filename)
    
    # plt.show()
    plt.close('all')

def convert_audio_to_spectogram(filename):
    """
    convert_audio_to_spectogram -- using librosa to simply plot a spectogram
    
    Arguments:
    filename -- filepath to the file that you want to see the waveplot for
    
    Returns -- None
    """
    
    # sr == sampling rate 
    x, sr = librosa.load(filename, sr=44100)
    
    # stft is short time fourier transform
    X = librosa.stft(x)
    
    # convert the slices to amplitude
    Xdb = librosa.amplitude_to_db(abs(X))
    
    # ... and plot, magic!
    plt.figure(figsize=(14, 5))
    
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
    plt.colorbar()
    plt.show()
    
# same as above, just changed the y_axis from hz to log in the display func    
def convert_audio_to_spectogram_log(filename):
    x, sr = librosa.load(filename, sr=44100)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'log')
    plt.colorbar()
    plt.show()



# file = os.path.join(BASE_DIR,filename)


# plot_mp3_matplot(file)
# convert_audio_to_spectogram_log(file)
# convert_audio_to_spectogram(file)

json_filename1 = "./uploads/spectrogram_step_1_Num{}.json".format(num)
json_filename2 = "./uploads/spectrogram_step_2_Num{}.json".format(num)

f1 = open(json_filename1)
f2 = open(json_filename2)

data1 = json.load(f1)
data2 = json.load(f2)

noise_list1 = {}
noise_list2 = {}

for i in data1.keys():
    noise_list1[i] = list(map(float,data1[i].split(", ")))

for j in data2.keys():
    noise_list2[j] = list(map(float,data2[j].split(", ")))

# print(noise_list1.keys())
# print(noise_list2.keys())

start1 = 100
start2 = 20

print('Step1:')
for i in noise_list1.keys():
    if int(i) < start1:
        continue
    print('Step1: Processing',i)
    temp_path = os.path.join(BASE_DIR, 'sample.wav')
    wavfile.write(temp_path, 16000, np.asarray(noise_list1[i], dtype=np.int16))
    plot_mp3_matplot(i,temp_path,os.path.join(BASE_DIR, 'step1_png','step1_Num{}_{}.png'.format(num,i)))
    
print('\n\nStep2:')
for i in noise_list2.keys():
    if int(i) < start2:
        continue
    print('Step2: Processing',i)
    temp_path = os.path.join(BASE_DIR, 'sample.wav')
    wavfile.write(temp_path, 16000, np.asarray(noise_list2[i], dtype=np.int16))
    plot_mp3_matplot(i,temp_path,os.path.join(BASE_DIR, 'step2_png','step2_Num{}_{}.png'.format(num,i)))

print('\nPNG Files generated ....\n')