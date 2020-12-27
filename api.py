import os
import os.path
from splitaudio import SplitWavAudio
import speech_recognition as sr

class tscb():

  def __init__(self):
      self.tmp = None

  def setup(self, f):
    """
    Initialises the audio by splitting it into 1-minute-sized chunks.
    :param f: The location of the transcription
    """
    try:
      splitter = SplitWavAudio('resources', f)
    except:
      print('Please enter an valid audio file name.')
    self.tmp = splitter.multiple_split(1)
    print(self.tmp)
  
  def purge(self):
    """
    Deletes the audio chunks.
    """
    for root, dirs, files in os.walk("resources/tmp"):
      for file in files:
        os.remove(os.path.join(root, file))
    self.tmp = None

  def transcribe(self):
    """
    Transcribes to text using Google Transcribe API.
    """
    r = sr.Recognizer()
    str = ''
    if self.tmp == None:
      print('Be sure to initialize the file first!')
    else:
      for file in self.tmp:
        audio_file = sr.AudioFile(file)
        with audio_file as source:
          audio = r.record(source)
        str += r.recognize_google(audio)
    return str
