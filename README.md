# 🎹 EASY PIANO TONE GENERATOR

> **A tiny synth. A questionable piano. An unreasonable amount of vibes.**

Press a number.

The speakers begin to glow.

A humble sine wave, wrapped in a little decay, launches directly into your ears.

This is not a Steinway.

This is not a professional instrument.

This is a tiny piano-tone experiment built in Python where **if it makes a sound, it wins**.

## ⚡ FEATURES

- 🎵 Generate notes live with sine waves
- 🔊 Output audio in real time through `sounddevice`
- 🫧 Add a simple volume decay / release effect
- 🎛️ Stack multiple notes together and theoretically create chords
- 🎹 Play a C major scale with the number keys
- 📼 Read and play MIDI events
- 📈 Visualize the audio waveform (because waveforms look cool)

## 🚀 GET STARTED

### 1. Install the dependencies

```bash
pip install numpy sounddevice mido matplotlib
```

### 2. Launch the real-time piano

```bash
python realtime_demo.py
```

Once it is running, enter:

| Input | Action |
| --- | --- |
| `1` - `7` | Play the C major scale (C4 to B4) |
| `u` | Release the current note and let it decay |
| `q` | Quit |

Example:

```text
Play note (1-7), release (u), or quit: 1
Play note (1-7), release (u), or quit: u
```

## 🧪 OTHER EXPERIMENTS

### Watch a note's waveform

```bash
python tone.py
```

This opens a live waveform window, plays A4 (440 Hz), and lets you watch it slowly disappear.

### Play recorded keyboard events

```bash
python play_dummy_midi.py
```

This reads [`midi_event.json`](./midi_event.json) from the repository and turns its `down` / `up` events into sound.

### Play MIDI files

```bash
python play_midi.py
```

`play_midi.py` expects MIDI files whose names match the paths in the script (by default, it looks for `laputa.mid`, `ddlc_main.mid`, and `harunoumi.mid`). These files are not included in the repository, so bring your own.

## 🧠 HOW THE MAGIC WORKS

The core formula is beautifully simple:

```text
sound = sine wave × decay envelope
```

`Tone` generates a waveform from a frequency and outputs it in chunks through the audio callback. When a note is released, its volume drops quickly so it does not haunt the background forever.

No sample library.

No mysterious black box.

Just sine, speakers, and a volume knob that probably should not be turned this far.

## 🛠️ PROJECT STATUS

**Experimental / gloriously unfinished**

This is a small audio experiment, not a complete piano application. Behavior may vary across operating systems, audio devices, and drivers. If you hear nothing, check your system output device, Python audio permissions, and `sounddevice` installation.

## ⚠️ DISCLAIMER: DO NOT USE FOR IMPORTANT STUFF

This project is **not designed, tested, certified, or approved** for:

- 🚫 Military use
- 🚫 Medical use
- 🚫 Aviation or aerospace use
- 🚫 Life-critical, safety-critical, or mission-critical systems

Do not use this software to control, monitor, diagnose, navigate, stabilize, or otherwise operate anything where a bug could hurt people, damage property, or ruin an extremely expensive day.

Use it for experiments, music, noise, and questionable home-lab decisions only. Improper use may cause unexpected behavior, broken speakers, existential regret, or — in the most technically unverifiable outcome — **a one-way trip to hell**.

## 📜 LICENSE

No separate license has been declared yet. Treat this as an open experimental playground: read the code, modify it, and make it produce even stranger sounds.

---

### Made with Python, sine waves, and dangerously optimistic acoustics.
