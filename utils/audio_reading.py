import soundfile as sf
import os
import glob
from preprocessing import trim_audio, filter_audio

audio_folder = os.path.join(os.path.dirname(__file__), "../data/train_short_audio")


def read_audio_by_class(class_name):
    class_data = []
    for audio_file in glob.glob(os.path.join(audio_folder, class_name, "*")):
        audio = read_audio_file(audio_file)
        class_data += trim_audio(audio)

    return class_data


def read_audio_file(path: str):
    """
    Reads the content of the specified audio path
    :param path: the path of the audio file
    :return:
    """
    data, samplerate = sf.read(path)
    return filter_audio(data)
