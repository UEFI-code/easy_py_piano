import sounddevice as sd
from tone import Tone

tone_1 = Tone(duration=10.0)

def callback(outdata, frames, time, status):
    outdata[:] = tone_1.get_chunk(frames)[:, None]

sd_out = sd.OutputStream(channels=1, blocksize=2048, callback=callback, samplerate=tone_1.sample_rate)
sd_out.start()

note_freqs = {
    '1': 261.63,
    '2': 293.66,
    '3': 329.63,
    '4': 349.23,
    '5': 392.00,
    '6': 440.00,
    '7': 493.88,
}

while True:
    cmd = input('Play note (1-7), release (u), or quit (q): ').strip()
    if cmd in note_freqs:
        tone_1.down(freq=note_freqs[cmd])
    elif cmd == 'u':
        tone_1.up()
    elif cmd == 'q':
        break