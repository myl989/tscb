from api import Tscb
from recorder import Recorder

'''
Parameters used for settings on how the exitcommand will be handeled.
0 indicates exiting immediately.
1 indicates doing the passto action first and then exiting.
'''
EXIT_IMMEDIATELY = 0
PASS_THEN_EXIT = 1

class Rtel:
  def __init__(self):
    '''
    Makes a Rtel application.
    '''
    self.num = 0
    self.passto = print #function
    self.exitcommand = None  #string
    self.purgesetting = 0
    self.exitcmdhandlesetting = 0
    self.exitinput = None #function
    self.lengthinput = input #function
    self.recorder = Recorder(44100, 10)
    self.transcriber = Tscb()
  
  def passTo(self, function):
    """
    Sets the function to pass the transcribed string to.
    :param function: The function to execute with the transcribed string as the parameter. The default passTo is print.
    """
    self.passto = function
  
  def setExitCommand(self, exitcommand):
    """
    Sets the exit command. It is optional.
    :param exitcommand: If the transcribed result is ever this, the loop exits. 
    """
    self.exitcommand = exitcommand
  
  def exitComandHandelingMethodSetting(self, setting):
    self.exitcmdhandlesetting = setting

  def purgeSetting(self, setting):
    self.purgesetting = setting

  def lengthInput(self, function):
    """
    Sets the input source of the length.
    :param function: The function that is called every loop. int(function()) will be then length of the source. The default lengthInput is input.
    """
    self.lengthinput = function

  def exitInput(self, function):
    """
    Sets a function to exit the program externally. It is optional.
    :param function: The function that is called every loop. function() should return a boolean value, which if is true, the loop will stuff.
    """
    self.exitinput = function

  def injectTranscriber(self, transcriber):
    '''
    The transcriber instance to use. A default instance is used if not specified.
    '''
    self.transcriber = transcriber

  def injectRecorder(self, recorder):
    '''
    The recorder instance to use. A default instance is used if not specified.
    '''
    self.recorder = recorder
  
  def run(self):
    while True:
      if self.exitinput is not None:
        if self.exitinput():
          break
      length = int(self.lengthinput())
      self.recorder.setRecordingLength(length)
      f = self.recorder.record()
      self.transcriber.setup(f)
      s = self.transcriber.transcribe()
      if self.exitcommand is not None and self.exitcmdhandlesetting == EXIT_IMMEDIATELY:
        if s == self.exitcommand:
          break
      self.passto(s)
      if self.exitcommand is not None and self.exitcmdhandlesetting == PASS_THEN_EXIT:
        if s == self.exitcommand:
          break
      self.transcriber.purge() 