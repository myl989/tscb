import sounddevice as sd
import wavio as wv

class Recorder():
  def __init__(self, frequency, recordinglength):
    """
    Makes a recorder class for recording audio.
    :param frequency: The desired sampling frequency of the audio in Hz
    :param recordinglength: The length of the recording in seconds
    """
    self.freq = frequency
    self.rlen = recordinglength
    self.num = 0
    self.folder = "resources"
    self.prefix = "r"
  
  def setPrefix(self, p):
    self.prefix = p
  
  def setFolder(self, f):
    self.folder = f

  def setRecordingLength(self, length):
    self.rlen = length

  def record(self):
    recording = sd.rec(int(self.rlen * self.freq), samplerate = self.freq, channels = 2)
    sd.wait()
    wv.write(self.folder + "/" + self.prefix + self.num + ".wav", recording, self.freq, sampwidth = 2)
    self.num = self.num + 1
