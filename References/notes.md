
https://vbinds.ch/sites/default/files/PDFs/SP20-Abdullah-SoKFaults.pdf

See a demo here https://mosis.eecs.utk.edu/advpulse.html and read the related paper. 

https://mosis.eecs.utk.edu/publications/li2020advpulse.pdf

https://sen-chen.github.io/img_cs/pdf/oakland2021_fakebob.pdf



#### 13-08-2021 (1.5+1.5+1.5=4.5 hours)

### SOK paper:

Neural networks are prone to adversarial attacks. 

ASR - automatic speech recognition

VPSes - voice processing systems - based on neural networks mostly

Image classification neural networks are vulnerable and done lots of work in the direction

Contributions:

1. VPS threat models: framework for attack models
2. Categorization of existing work
3. Experimental testing of transferability

Background:

1. Psychoacoustics: contributes to the way human brain perceives the audio - loudness is non-linear - visual cues, pitch separation, intensity  
2. Voice processing systems: ASR - automatic speech recognition, SI - speaker identification system. Pipeline :
   1. preprocessing: segments of audio containing human speech are identified using voice-activity detection algorithms - G.729 - then low pass filter to remove high frequencies - net result is Removal of noise 
   2. feature extraction: filtered audio - 20ms frames to capture transitions - Mel frequency Cepstral Coefficient (MFCC) model:
      1. DTFT: time domain to frequency domain representation conversion - fine grain understanding of audio's frequency composition
      2. Mel Filtering: Non linear effect - scales intensities of frequencies - mk= 2595 log(1+|Fk|/700) - assigns higher weight to frequencies between - 100Hz and 8kHz
      3. Log scaling: scaled by log function
      4. DCT: decompose into cosine components - components with most info is retained
   3. Inference: features are passed to probabilistic model - neural networks
      1. CNN: each layer is made up of set of filters that are convolved with layers input
      2. RNN: CNN but with variable sized input and variable sized output. Ideal for audio where size varies. Contextual information - important for VPSes 
   4. Decoding: make output more reader friendly - beam search
   5. Alternative configurations
3. Speaker identification: identification vs verification. Similar to ASR till the last stage. inferences is omitted.
4. Adversarial machine learning in VPSes: poisoning training set or evasion attacks at test time.
   1. Example: use perturbation imperceptible to humans 
   2. Crafting adversarial samples: gradient based optimization. has access to models gradients. 
   3. Transferability: holds in image domain. 



Attacks against VPSes: there are several key differences from image domain hence discuss pipeline first

1. preprocessing pipeline: rely on feature extraction components that are not learned from training data. Use signal processing techniques for evasion. less model dependent.
2. sequential models: propagate patterns identified in prior time. unrolling

Attack threat model taxonomy: 

1. Goals: untargeted, targeted - specific response

2. Types: 

   1. Optimization attacks: Direct if information about weights of model is available to compute gradients, indirect if weights are not available hence estimated by querying the model
   2. Signal Processing attacks: Exploit discrepancies between human ear and feature extraction algorithm. less model dependent
   3. Miscellaneous: limitation of hardware (mic) replay attack, homophones - similar sounding words without context

3. Adversarial knowledge: VPS components:

   1. task: problem trained to solve
   2. preprocessing: knowledge of algorithm and weights
   3. feature extraction: feature extraction parameters
   4. inference: weights, types, number of layers, architecture
   5. Decoding: decoding algos, beam search - parameters

   depending on this knowledge types:

   1. white box: knowledge of all categories.
   2. grey box: only a subset of categories. 
   3. black box: no information. just task is known
   4. no box: no knowledge at all

4. Adversarial capabilities:

   1. Constraint on input manipulations: 
      1. granularity: phoneme, word, sentence
      2. types of audio: inaudible - ultrasound, Noise, clean
   2. Access to the model: 
      1. queries: number of queries
      2. output: probability distribution vs final label
      3. attack medium: 
         1. over line: waveform audio file - lossless transmission
         2. over air: playing attack on speaker and hope to record
         3. over telephony network: over the telephony network undergo codec compression, packer loss, jitter, static interference
         4. over others: compression with MPEG- audio layer III (mp3)
      4. Distance: larger distance - greater degradation
      5. acoustic environment: noisy environments
      6. acoustic equipment: passing over variety of equipment - codecs, mics, speakers - certain frequencies might be attenuated or intensified

Existing attack classification:

1. targeted white box attacks: 
2. Clean attacks and mediums: clear to humans, limited success over email, few work over air - 41, 74, 77
3. signal processing attacks vs rest: greater promising, black box - less queries - clean target attack not done
4. attacks against SIs: similar pipeline in ASRs and SIs hence less specialized work in SIs
5. Indirect optimization attacks: one word granularity - repeatedly querying the model - black box settings - only over line use and not on other mediums - 
6. Optimization attacks do not guarantee success:  stuck at local minima
7. model agnostic attacks: 





Defense and detection taxonomy: 

1. Attacker type: non adaptive - no knowledge of targets defense strategy, adaptive - full knowledge of defense strategy
2. Adversarial cost: resources, distortion
3. Stochastic modeling: 
4. Additional hardware
5. distance
6. Attack type
7. audio file
8. medium

Defenses and detection classification

1. adversarial training: train using adversarial examples improving decision boundary - label leaking - losing accuracy of model after training over adversarial examles
2. Liveness detection: identify source as human or mechanical. 
3. future direction

Discussion

1. lack of transferability for optimization attacks: works in signal processing attacks. 
2. Defenses for VPSes: 
3. VPSes pipeline
4. Lack of poisoning and Privacy attacks: 
5. Defenses mechanism
6. Lack of audio intelligibility metrics





25-08-2021 (2 + hrs )

### advPulse paper:

abstract: Existing focus on attack with prior knowledge. 

1. can not anticipate
2. no synchronization - time

1. Introduction:

   1. speech content and speaker recognition
   2. Existing attacks:
      1. modifying entire input - same duration
      2. synchronization 
      3. prior knowledge
   3. proposed - 
      1. short duration - 0.5sec
      2. no synchronization required - insert anywhere
      3. input agnostic universal - arbitrary input to desired label
   4. what:
      1. penalty based universal adversarial perturbation generation algorithm - optimize over entire time delay distribution - robust to any delay
      2. environmental sound mimicking technique
      3. over-the-air environments distortion
      4. 89 & 90 % accuracy

2. Related Work:

   Ed

3. Background:

   1. Problem Formalization - perturbation - delta E[-1,1]**l n is sample
   2. Threat Model

4. Design

   1. Synchronization free subsecond targeted adversarial perturbation
      1. minimize dBx(delta), subject to argmax(f(x+delta))=yt - relative loudness of the perturbation comparing to the audio input - minimize objective function



#### Information collection:

1. use paperwithcodes
2. chrome extension

### 16th September 2021

1. SokFaults:
   1. Codebase for trasferbility benchmarks [AsrAttackSok/Transferbility_of_AEs: SoK.](https://github.com/AsrAttackSok/Transferbility_of_AEs)
2.  Advpulse:
   1. Ran the examples on google voice detection 
      1. Observations: Most of the case system did not respond, Correct response 
   2. Requested the codebase and further info to reproduce the results

2. ATTACK ON PRACTICAL **SPEAKER VERIFICATION** SYSTEM USING UNIVERSAL ADVERSARIAL PERTURBATIONS : 

   1. Weiyi Zhang , Shuning Zhao, Le Liu, Jianmin Li Xingliang Cheng, Thomas Fang Zheng , Xiaolin Hu

   2. May 2021 - ICASSP 2021

   3. Code available [zhang-wy15/Attack_practical_asv: ICASSP 2021 accepted paper (github.com)](https://github.com/zhang-wy15/Attack_practical_asv)

   4. Summary:

      1. Assumptions: whitebox for ASV but no knowledge of audio replay check and Speech recognition model

      2. ![image-20210916131136536](C:\Users\91930\AppData\Roaming\Typora\typora-user-images\image-20210916131136536.png)

      3. Tackles: Audio replay check (RIR), Universal-text independent, Fools identity.

      4. Experimental setup: 

         1. Dataset- LibriSpeech clean dataset
         2. replay detection - ASVspoof2019 first place winner model
         3. Speech content check - Google cloud speech to text API
         4. Speaker identification - 2020 DNN Model - arXiv:2003.11982, 2020.

      5. Results: 

         1. Identification - 100% attack success rate with 
         2. content check - 3.55% **extra** word error rate
         3. replay detection - 67.7% success - previous studies had 37.7%

         

3. Practical Adversarial Attacks Against Speaker Recognition Systems

   1. Zhuohang Li, Cong Shi Rutgers , Yi Xie Rutgers , Jian Liu ,Bo Yuan , Yingying Chen

   2. Same authors as AdvPulse

   3. March, 2020, Hot mobile-2020

   4. Summary:

      1. Assumptions

      2. Tackles - integrates RIR - for over the air ![image-20210916140851630](C:\Users\91930\AppData\Roaming\Typora\typora-user-images\image-20210916140851630.png)

      3. Experimental setup

         1. Identification model: X-vector, the state-of-the-art deep neural network (DNN)
         2. 

         

         

      4. Results

         1. ![image-20210916141649247](C:\Users\91930\AppData\Roaming\Typora\typora-user-images\image-20210916141649247.png)
         2. ![image-20210916141723054](C:\Users\91930\AppData\Roaming\Typora\typora-user-images\image-20210916141723054.png)

   5. 

Ways to go: speaker verification, over the air (RIR), 

4. Fakebob:
   1. NES - natural evolution strategy based gradient estimation?
   2. 





Meeting notes:

advpulse - not possible real world

Defense side - good defense

need to know attack system

2 attacks - find them on some models

mp3 compression - paper - 



### 30th September 2021

1. Initialize attack in practical
2. Mailed 
3. HPC access



signal processing

signal processing vs model optimiization

feature extraction - intekll

implement and eval

[Know your enemy. How you can create and defend against… | by Oscar Knagg | Towards Data Science](https://towardsdatascience.com/know-your-enemy-7f7c5038bdf3)

[1706.06083.pdf (arxiv.org)](https://arxiv.org/pdf/1706.06083.pdf)



  export http_proxy=10.10.78.62:3128
  export ftp_proxy=10.10.78.62:3128
  export https_proxy=10.10.78.62:3128

export SSL_CERT_FILE=$HOME/CCIITD-CA.crt



export LD_LIBRARY_PATH=/home/apps/anaconda3_2018/4.6.9/lib:$LD_LIBRARY_PATH

qsub -I -P cse -l select=1:ncpus=2:ngpus=1:mem=4G -l walltime=12:00:00

qsub -I -P cse -l select=1:ncpus=1:ngpus=1:mem=4G -l walltime=00:03:00

or
qsub -I -P cse -l select=2:ncpus=8:ngpus=1:mem=24G:centos=skylake -l walltime=6:00:00



python3 attack.py --config config/attack_config.yaml 

1. Data preparation
2. Pretrained model
3. Generate splits
4. 2 step attack



1. understand why this attack was successful
2. Features they are feeding to cnn - NFTC - 48 freatues
3. Behavioral changes when noise is added 
4. Movement of feature changes - plot changes
5. Most prominent features
6. Understand these 5 basics before creating defense
7. most important weights

Simple noise addition wont work

1. Transformer (machine learning model)
2. adversarial training
3. 

**WHY IT WORKS IS THE KEY**

