from api import Tscb
from recorder import Recorder

api = Tscb()
recorder = Recorder(44100, 10)

print("Type 'end' to end")

while (True):
  s = input('> ')
  splitter = None

  if s.startswith('init '):
    api.setup(s[5:])

  elif s == 'purge':
    api.purge()

  elif s == 'transcribe':
    print(api.transcribe())

  elif s == 'record':
    recorder.record()
  
  elif s == 'end':
    break
  
  else:
    print('Feature not supported')