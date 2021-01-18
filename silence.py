from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence
import os
import scipy.io.wavfile as wav

#split emotions, silence, pronounciation, filler words use glob
    
def getPauses(folder):
    (source_rate, source_total) = wav.read(folder+"/audio.wav")
    totalTime = len(source_total)/float(source_rate)

    sound_file = AudioSegment.from_wav(folder+"/audio.wav")

    audio_chunks = split_on_silence(sound_file, min_silence_len=1000, silence_thresh=-32)
    if(len(os.listdir(folder))==3):
        for i, chunk in enumerate(audio_chunks):

            out_file = folder+"/section_{0}.wav".format(i)
            chunk=chunk.set_channels(1)
            chunk.export(out_file, format="wav")
    return (((len(audio_chunks)-1)/totalTime)*60)
