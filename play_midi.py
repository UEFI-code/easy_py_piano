import mido
import sounddevice as sd
from tone import Tone
import time
import numpy as np

tone_gen_list = []

def callback(outdata, frames, time, status):
    wave = np.zeros_like(outdata)
    for tone_gen in tone_gen_list:
        wave += tone_gen.get_chunk(frames)[:, None]
    outdata[:] = wave

sd_out = sd.OutputStream(channels=1, blocksize=2048, callback=callback, samplerate=44100)
sd_out.start()

def press_multiple_keys(freq):
    # search for existing tone generator which playing is false
    tone = None
    for tone_gen in tone_gen_list:
        if tone_gen.playing == False:
            tone = tone_gen
            break
    if tone is None:
        print(f"Creating new Tone generator for freq: {freq}")
        tone = Tone(duration=10.0)
        tone_gen_list.append(tone)
    tone.down(freq=freq)
    tone.now_play_freq = freq

def release_multiple_keys(freq):
    for tone_gen in tone_gen_list:
        if tone_gen.now_play_freq == freq:
            print(f"Releasing freq: {freq}")
            tone_gen.up()
            tone_gen.now_play_freq = None
            break

# Read MIDI file
def play_midi_beep(file_path):
    mid = mido.MidiFile(file_path)
    tempo = 50000  # Default tempo (microseconds per beat)
    for msg in mid.play():
        if msg.type == 'note_on' and msg.velocity > 0:
            freq = int(440 * (2 ** ((msg.note - 69) / 12)))
            press_multiple_keys(freq)
            print(f"Down freq: {freq} for note {msg.note} ({freq:.2f} Hz)")
            time.sleep(tempo / 1_000_000)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            freq = int(440 * (2 ** ((msg.note - 69) / 12)))
            release_multiple_keys(freq)
            print(f"Up freq: {freq} for note {msg.note} ({freq:.2f} Hz)")
            time.sleep(tempo / 1_000_000)
        elif msg.type == 'set_tempo':  # Update tempo
            tempo = msg.tempo

press_multiple_keys(440)  # Press A4 (440 Hz)
time.sleep(2)
press_multiple_keys(523.25)  # Press C5 (523.25 Hz)
time.sleep(2)
release_multiple_keys(440)  # Release A4
time.sleep(3)
release_multiple_keys(523.25)  # Release C5
time.sleep(3)

while True:
    play_midi_beep('laputa.mid')
    play_midi_beep('ddlc_main.mid')
    play_midi_beep('harunoumi.mid')