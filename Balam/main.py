import speech_recognition as sr

import helpers.balam_commands as b_c

'''
# Acknoledgement
https: // github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
https://stackoverflow.com/questions/5817209/browse-files-and-subfolders-in-python
'''

r = sr.Recognizer()

def input_type():
    type = str(input("What input command type do you prefer? ")).lstrip()

    if type.lower() == "voice":
        return('voice')
    elif type.lower() == "text":
        return('text')
    else:
        b_c.speak("invalid input command type")
        return input_type()


def check_balam(input_command):
    if 'balam' in input_command:
        return True

    else:
        return wake_up()


def wake_up(input_type = "None"):
    if input_type == "voice":
        # listen for keyword "balam"
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            audio = r.listen(source)
            
        # check for keyword
        try:
            input_command = r.recognize_google(audio)
            return check_balam(input_command)
            
        except:
            return wake_up()
    elif input_type == 'text':
        input_command = str(input("What is your command? ")).lower()
        return check_keyword(input_command, input_command.split(' ', 1)[0], 'text')


def obtain_input():
    # greet user
    b_c.speak("What is your command?")

    # obtain audio from the microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        
    # recognize speech
    try:
        # speech succesfully recognized
        input_command = r.recognize_google(audio)
        return input_command

    except:
        # speech unsuccesfully recognized
        b_c.speak("Error... Could not comprehend")


def check_keyword(input_command, keyword = None, input_type = None):
    if 'open' in input_command[0] or keyword == "open":
        b_c.speak('opening')

        try:
            b_c.open((''.join(input_command.split('open')).lstrip()).replace(' ', '_'))
        except:
            b_c.speak('application not found.')

    elif 'shutdown' in input_command[0] or keyword == "shutdown":
        b_c.speak('shutting down')
        
        b_c.shutdown()

    elif 'sleep' in input_command[0] or keyword == "sleep":
        b_c.speak('goodnight')
        
        b_c.sleep()

    elif 'restart' in input_command[0] or keyword == "restart":
        b_c.speak('error... rererestarting computer')
        
        b_c.restart()
    
    elif 'play' in input_command[0] or keyword == "play":
        b_c.speak('playing, {}'.format(' '.join(input_command.split('play'))))
        
        b_c.play_music(''.join((input_command.replace(' ', '+').split('play'))))

    elif 'what' in input_command[0] or keyword == "what":
        if 'time' in input_command:
            b_c.time()

    elif 'search' in input_command[0] or keyword == "search":
        b_c.search(''.join(input_command.split('search')).lstrip())

    elif 'exit' in input_command[0] or keyword == "exit":
        exit()
    else:
        b_c.speak("Error... Could not comprehend")
    
    # Restart asiistant // Loop until exit
    command_prompt_assistant(input_type)


def command_prompt_assistant(input_type):
    if input_type == 'text':
        wake_up(input_type)
    
    else:
        if wake_up(input_type):
            check_keyword(obtain_input(), input_type=input_type)


if __name__ == "__main__":

    command_prompt_assistant(input_type())