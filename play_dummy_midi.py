import json
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

press_multiple_keys(440)  # Press A4 (440 Hz)
time.sleep(2)
press_multiple_keys(523.25)  # Press C5 (523.25 Hz)
time.sleep(2)
release_multiple_keys(440)  # Release A4
time.sleep(3)
release_multiple_keys(523.25)  # Release C5
time.sleep(3)

key_event_data = json.load(open("midi_event.json", "r"))
for event in key_event_data:
    for d in event["down"]:
        press_multiple_keys(d)
    for u in event["up"]:
        release_multiple_keys(u)
    time.sleep(0.05)