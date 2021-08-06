# Balam Assistant
**Balam** is a voice/ command-line that you can command to play music or videos, ask the time, open application, search the web, and also command it to make your computer
shutdown, restart, or go to sleep.

## How does Balam works?
The idea is simple. Balam asks the user for their preffered input type, which can either be:
- voice
- text

### How does voice input command works?
If your chosen input command type is voice, it listens thru your microphone for the keyword **"Balam"** to wake up the voice assistant, and after that you can now proceed
to command **Balam**.

### How does text input command works?
If your chosen input command type is text, the next steps will be pretty straightforward. It will ask you immediately for your command without needing to wake up **Balam**.

### What are the commands in available in Balam?
These are the available commands in Balam:
#### Open + ""
Opens an application or program installed in the computer.
#### What + ""
The what command as of now, only consists of one sub-commmand.
- Time - says the time
#### Search + ""
Searches the web for the given keyword.
#### Shutdown
Shutdown your computer.
#### Restart
Restart your computer.
#### Sleep
Make your computer go to sleep.

Note: Make sure that the main-command is the first word followed by ""

## Possible Improvements
As all applications this one can also be improved. Possible improvements:
- Have an interactive GUI.
- Make the voice input handle noise in the background better.
- Additional sub-commands for the main-command **"What"**.
- Have a way to setup application better and more efficiently for the main-command **"Open"**.

## Requirements
To run the python program the following must be satisfied:
- Windows 10
- Internet Connection
- Python 3.7+

The following python libraries must also be installed:
- speech_recognition
- pywhatkit
- pandas
- pyttsx3

## How to launch Balam?
1. Make sure that the requirements are satisfied.
2. Download Balam.zip
3. Extract Balam.zip
4. Open windows terminal, cmd, or the like.
5. Change directory to where the program is located.
6. Setup the program using <span style="background-color: grey">setup.py</span>.
7. Run the program using <span style="background-color: grey">main.py</span>.
8. Enjoy.

## Note
- running in debug mode may cause errors in **open** command
- if you're using **voice** input, make sure that background noise is minimal, and voice is clear

## Video Demo
For more information on how to use the program, refer to the link:
https://www.youtube.com/watch?v=q_fYePEESLAE
