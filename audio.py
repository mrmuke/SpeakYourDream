from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence

input_file = 'example.wav'

sound_file = AudioSegment.from_wav(input_file)

silence_array = detect_silence(sound_file, min_silence_len = 3000, silence_thresh=-32)

print(silence_array)

"""
audio_chunks = split_on_silence(sound_file, min_silence_len=1000, silence_thresh=-32)

for i, chunk in enumerate(audio_chunks):

    out_file = "audio/{0}.wav".format(i)
    print("exporting")
    print(out_file)
    chunk.export(out_file, format="wav")
"""