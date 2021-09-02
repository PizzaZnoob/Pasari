from scipy.signal import butter, filtfilt

default_window_size = 300000
default_overlap = 0
default_cutoff = 10000


def filter_audio(data, fs=32000, order=2, cutoff=default_cutoff):
    nyquist_freq = 0.5 * fs
    normal_cutoff = cutoff / nyquist_freq

    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered = filtfilt(b, a, data)
    return filtered


def trim_audio(audio_data, window_size=default_window_size, overlap=default_overlap):
    step_size = window_size - overlap
    if step_size <= 0:
        raise ValueError("Overlap too large!")

    audio_trim = []
    while len(audio_data) > window_size:
        audio_trim.append(audio_data[:window_size])
        audio_data = audio_data[step_size:]

    return audio_trim
