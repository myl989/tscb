This application can be used to help convert a piece of audio into text. It has a command-line format. (Full API to be added)

To use, first place the audio file in a WAV format into the `resources` folder. Then, run `init [file_name].wav` to initialize the transcriber. Finally, run `transcribe` to transcribe the text. To transcribe another piece of text, run `purge`, and replace the .wav file, and repeat the processes.

List of commands in *`Tscb`*:
**`init [file_name].wav`**
Initialises the audio by splitting it into 1-minute-sized chunks.

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
Records a file of the selected frequency and recording length to the `resources` folder.