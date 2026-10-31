import numpy as np
import matplotlib.pyplot as plt

class Tone:
    def __init__(self, frequency=440.0, amplitude=0.5, sample_rate=44100, duration=5.0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.sample_rate = sample_rate
        self.ts = np.arange(int(sample_rate * duration)) / sample_rate
        self.sine_table = self.amplitude * np.sin(2 * np.pi * self.frequency * self.ts)
        self.reduce_line = 1 / (1 + 3 * self.ts)
        self.signal = self.sine_table * self.reduce_line
        self.playing = False
        #plt.plot(self.ts, self.signal)

    def down(self):
        self.chunk_idx = 0
        self.playing = True

    def get_chunk(self, chunk_size):
        if not self.playing: return np.zeros(chunk_size)
        chunk = self.signal[self.chunk_idx:self.chunk_idx + chunk_size]
        if chunk.size < chunk_size:
            self.playing = False # over
            chunk = np.pad(chunk, (0, chunk_size - chunk.size), 'constant')
        self.chunk_idx += chunk_size
        return chunk

    def up(self):
        self.playing = False

if __name__ == "__main__":
    chunk_size = 2048
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(0, chunk_size/44100)
    ax.set_ylim(-1, 1)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Tone Waveform")
    ax.grid(True)
    line, = ax.plot([], [], lw=1.5)

    tone = Tone()
    tone.down()
    
    x = tone.ts[:chunk_size]
    while tone.playing:
        chunk = tone.get_chunk(chunk_size)
        line.set_data(x, chunk)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.01)