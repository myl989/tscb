Transcription tutorial:

To use, first place the audio file in a WAV format into the `resources` folder. Then, run `init [file_name].wav` to initialize the transcriber. Finally, run `transcribe` to transcribe the text. To transcribe another piece of text, run `purge`, and replace the .wav file, and repeat the processes. You can customize the source or buffer directory using setter methods.

List of commands in *`Tscb`*:
**`init [file_name].wav`**
Initialises the audio by splitting it into 1-minute-sized chunks. This is to comply with the Google API's regulations.

**`transcribe`**
Transcribes to text using Google Transcribe API.

**`purge`**
Deletes the audio chunks.

**`end`**
Exits the program.

This project also contains a recorder.

List of commands in *`Recorder`*:
**`init [frequency] [recordinglength]`**
Creates a *`Recorder`* instance with the desired sampling frequency in Hz and length of recording in seconds.

**`record`**
Records a file of the selected frequency and recording length to the `resources` folder. Returns the file name.

The *`Rtel`* class stands for "record transcribe evaluate loop", a class for push-to-talk voice recognition.

List of commands in *`Rtel`*:
**`init`**
Creates a *`Rtel`* instance.

**`passTo [function]`**
The transcribed text is passed to this function. The default passTo is print.

**`setExitCommand [command]`**
If the transcribed text is equal to this text, the loop ends.

**`purgeSetting [setting]`**
Sets what the program will do with the generated audio files. See the constants section below for the settings.

**`exitComandHandelingMethodSetting [setting]`**
Sets how the the exit command will be handled. See the constants section below for the settings.

**`lengthInput [function]`**
This function will be called every loop to find the length of the next recording. The default lengthInput is input.

**`exitInput [function]`**
This optional function allows exiting the loop from external programs. The function is called every loop and the loop is exited if function() returns a truthy value.

**`injectTranscriber [transcriber]`**
Sets the transcriber instance to use. A default transcriber is used if never set.

**`injectRecorder [recorder]`**
Sets the recorder instance to use. A default recorder is used if never set.

List of settings constants for the purgeSetting:

**`KEEP` (default)**
Do not purge any buffered audio files.

**`PURGE_ON_EXIT`**
The buffered audio files will be purged when the loop ends.

**`PURGE_AFTER_TRANSCRIBED`**
The buffered audio files will be purged after each transcription.

List of settings constants for the exitComandHandelingMethodSetting:

**`EXIT_IMMEDIATELY` (default)**
When the exit command is detected, exit immediately.

**`PASS_THEN_EXIT`**
Always pass the command to passTo first before deciding to exit.
