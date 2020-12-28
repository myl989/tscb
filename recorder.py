import sounddevice as sd
import wavio as wv

class Recorder():
  def __init__(self, frequency, recordinglength):
    """
    Makes a recorder class for recording audio.
    :param frequency: The desired frequency of the audio
    :param recordinglength: The length of the recording in seconds
    """
    self.freq = frequency
    self.rlen = recordinglength
    self.num = 0

  def record(self):
    recording = sd.rec(int(self.rlen * self.freq), samplerate = self.freq, channels = 2)
    sd.wait()
    wv.write("resources/r" + self.num + ".wav", recording, self.freq, sampwidth = 2)
    self.num = self.num + 1
