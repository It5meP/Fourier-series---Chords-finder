import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks, windows

def frequency_to_note(frequency):
    A4 = 440.0
    note_names = [ 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    if frequency == 0:
        return "No Note"
    semitones = 12 * np.log2(frequency / A4)
    note_index = int(round(semitones)) % 12
    octave = int(round(semitones)) // 12 + 4
    return f"{note_names[note_index]}{octave}"

file_path = r" "
sample_rate, samples = wavfile.read(file_path)
samples = samples / np.max(np.abs(samples))

window = windows.hamming(len(samples))
samples_windowed = samples * window
fft_result = np.abs(fft(samples_windowed))
frequencies = np.fft.fftfreq(len(samples), 1/sample_rate)

positive_freqs = frequencies[:len(frequencies)//2]
positive_fft = fft_result[:len(fft_result)//2]

min_freq = 400
max_freq = 1800

indices = (positive_freqs >= min_freq) & (positive_freqs <= max_freq)
filtered_freqs = positive_freqs[indices]
filtered_fft = positive_fft[indices]

height_threshold = 150
peaks, _ = find_peaks(filtered_fft, height=height_threshold)

print("Peak Indices in Filtered Data:", peaks)
print("Peak Frequencies:", filtered_freqs[peaks])
print("Peak FFT Amplitudes:", filtered_fft[peaks])

notes = [frequency_to_note(filtered_freqs[peak]) for peak in peaks]

unique_notes = sorted(set(notes))
print("The notes in the chord are:", unique_notes)

plt.plot(filtered_freqs, filtered_fft)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Chords (Filtered)')
plt.xlim(min_freq, max_freq)
plt.show()
