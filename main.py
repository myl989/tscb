import os
import os.path
from splitaudio import SplitWavAudio
import speech_recognition as sr

print(sr.__version__)
r = sr.Recognizer()

files = None

while (True):
  s = input('> ')
  splitter = None

  if s.startswith('init '):
    try:
      splitter = SplitWavAudio('resources', s[5:])
    except:
      print('Please enter an valid audio file name.')
    files = splitter.multiple_split(1)
    print(files)

  elif s == 'purge':
    for root, dirs, files in os.walk("resources/tmp"):
      for file in files:
        os.remove(os.path.join(root, file))

  elif s == 'transcribe':
    str = ''
    if files == None:
      print('Be sure to initialize the file first!')
    else:
      for file in files:
        audio_file = sr.AudioFile(file)
        with audio_file as source:
          audio = r.record(source)
        str += r.recognize_google(audio)
    print(str)
  
  elif s == 'end':
    break
  
  else:
    print('Feature not supported')

#audio_file = sr.AudioFile('Alex.wav')

#with audio_file as source:
   #audio = r.record(source)

#print(type(audio))
#print(r.recognize_google(audio))