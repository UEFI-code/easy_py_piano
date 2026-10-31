import sounddevice as sd
from tone import Tone

sample_rate = 44100
chuck_size = 2048
tone_1 = Tone(frequency=440.0, amplitude=0.5, sample_rate=sample_rate, duration=10.0)

def callback(outdata, frames, time, status):
    outdata[:] = tone_1.get_chunk(frames)[:, None]

sd_out = sd.OutputStream(channels=1, blocksize=chuck_size, callback=callback, samplerate=sample_rate)
sd_out.start()
while True:
    cmd = input('Enter command down(d)/up(u)/exit(e): ')
    if cmd == 'd':
        tone_1.down()
    elif cmd == 'u':
        tone_1.up()
    elif cmd == 'e':
        break