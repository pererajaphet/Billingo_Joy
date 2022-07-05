import glob, os
import AudioModifications as am
import librosa as lr
import soundfile as sf

#This is a script to make multiple modifications for audio augmentations of the pronounciations of 4 words 
#Just change the path of the folder where the data is and you are good to go
#Each folder contains a Good and a Wrong pronounciations folders where the audios in .wav are.

# #For the word FLOWER
# #The GOOD ones
path_of_the_directory = '/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good'
object = os.scandir(path_of_the_directory)
i=0
for n in object :
    if n.is_dir() or n.is_file():
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/add_noise_good{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/shifted4_good{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/shifted6_good{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/shifted3_24_good{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/cut_good{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Good/stretched{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
    i+=1
object.close()

# #The WRONG ones
path_of_the_directory = '/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong'
object = os.scandir(path_of_the_directory)
i=0
for n in object :
    if n.is_dir() or n.is_file():
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/add_noise_wrong{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/shifted4_wrong{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/shifted6_wrong{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/shifted3_24_wrong{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/cut_wrong{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Flower/Wrong/stretched_wrong{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
    i+=1
object.close()

#For the word BANANA
#The GOOD ones
i=0
os.chdir("/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good")
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/add_noise_good{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/shifted4_good{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/shifted6_good{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/shifted3_24_good{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/cut_good{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Good/stretched{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1

#The WRONG ones
i=0
os.chdir('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong')
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/add_noise_wrong{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/shifted4_wrong{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/shifted6_wrong{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/shifted3_24_wrong{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/cut_wrong{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Banana/Wrong/stretched_wrong{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1


#For the word GARDEN
#The GOOD ones
i=0
os.chdir('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good')
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/add_noise_good{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/shifted4_good{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/shifted6_good{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/shifted3_24_good{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/cut_good{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Good/stretched{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1


#The WRONG ones
i=0
os.chdir('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong')
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/add_noise_wrong{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/shifted4_wrong{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/shifted6_wrong{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/shifted3_24_wrong{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/cut_wrong{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Garden/Wrong/stretched_wrong{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1


#For the word MONKEY
#The GOOD ones
i=0
os.chdir('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good')
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/add_noise_good{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/shifted4_good{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/shifted6_good{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/shifted3_24_good{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/cut_good{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Good/stretched{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1


#The WRONG ones
i=0
os.chdir('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong')
for n in glob.glob("*.wav"):
        y,sr=lr.load(n)
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/add_noise_wrong{}.wav'.format(i),am.add_white_noise(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/shifted4_wrong{}.wav'.format(i),am.pitch_scale_1(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/shifted6_wrong{}.wav'.format(i),am.pitch_scale_2(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/shifted3_24_wrong{}.wav'.format(i),am.pitch_scale_3(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/cut_wrong{}.wav'.format(i),am.time_cut(y),sr, subtype='PCM_24')
        sf.write('/Users/asma/Desktop/S9/Master_Projet/WavAudios/Monkey/Wrong/stretched_wrong{}.wav'.format(i),am.time_stretch(y),sr, subtype='PCM_24')
        i+=1






