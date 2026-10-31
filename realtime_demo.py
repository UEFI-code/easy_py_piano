import sounddevice as sd
from tone import Tone

tone_1 = Tone(duration=10.0)

def callback(outdata, frames, time, status):
    outdata[:] = tone_1.get_chunk(frames)[:, None]

sd_out = sd.OutputStream(channels=1, blocksize=2048, callback=callback, samplerate=tone_1.sample_rate)
sd_out.start()
while True:
    cmd = input('Enter command down(d)/up(u)/exit(e): ')
    if cmd == 'd':
        tone_1.down()
    elif cmd == 'u':
        tone_1.up()
    elif cmd == 'e':
        break