import numpy as np
import matplotlib.pyplot as plt

class Tone:
    def __init__(self, sample_rate=44100, duration=5.0):
        self.sample_rate = sample_rate
        self.ts = np.arange(int(sample_rate * duration)) / sample_rate
        self.reduce_line = 1 / (1 + self.ts ** 2)
        self.playing = False

    def down(self, freq=440.0, amp=0.5):
        self.chunk_idx = 0
        self.sine_table = amp * np.sin(2 * np.pi * freq * self.ts)
        self.signal = self.sine_table * self.reduce_line
        self.playing = True

    def get_chunk(self, chunk_size):
        if not self.playing: return np.zeros(chunk_size)
        chunk = self.signal[self.chunk_idx:self.chunk_idx + chunk_size]
        if chunk.size < chunk_size:
            chunk = np.pad(chunk, (0, chunk_size - chunk.size), 'constant')
            self.playing = False # over
        self.chunk_idx += chunk_size
        return chunk

    def up(self):
        self.playing = False

if __name__ == "__main__":
    chunk_size = 2048
    tone = Tone()

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(0, chunk_size/44100)
    ax.set_ylim(-1, 1)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Tone Waveform")
    ax.grid(True)
    line, = ax.plot([], [], lw=1.5)

    x = tone.ts[:chunk_size]
    tone.down(freq=440.0, amp=0.5)
    while tone.playing:
        chunk = tone.get_chunk(chunk_size)
        line.set_data(x, chunk)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.01)