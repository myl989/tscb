from api import tscb

api = tscb()

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
  
  elif s == 'end':
    break
  
  else:
    print('Feature not supported')