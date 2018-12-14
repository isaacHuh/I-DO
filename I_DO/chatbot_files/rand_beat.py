import numpy
import random
import wave, sys, pyaudio

all_files = ["G_chord.wav", "C_chord.wav", "Am_chord.wav" , "E_chord.wav" , "Dm_chord.wav" , "Em_chord.wav" , "F_chord.wav" , "G7_chord.wav" , "B7_chord.wav" , "Bm_chord.wav" , "idk_chord.wav" , "A_chord.wav" , "D_chord.wav"]
infiles = []
for i in range(len(all_files)):
	rand_num = random.randint(0,(len(all_files)-1))
	infiles.append('audio_files/' + all_files[rand_num]) 

outfile = "i_do_beat.wav"
#this makes the file where it will play the sound
data = []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])

add_num = random.randint(3,(len(data)-1))
for i in range(add_num):
	output.writeframes(data[i][1])

output.close()

#https://people.csail.mit.edu/hubert/pyaudio/docs/

CHUNK = 1024

wf = wave.open(outfile, 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()