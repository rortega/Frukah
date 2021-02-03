import PySimpleGUI as sg
import time
import sys
import frida, sys
from JSCode import JSCode
from JSCode import Script
import subprocess
from subprocess import PIPE
import time
import threading

TargetApp = ""

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def thread_command(script):
    proc = ['frida-ps','-D','emulator-5554','-a']
    p = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
    retval = p.wait(5)
    return (retval, output)
script_0 = None;

def load_script(script):
    print("Script loaded..")
    jscode = JSCode()
    process = frida.get_usb_device().attach('jakhar.aseem.diva') # App DIVA used for testing purposes
    script = process.create_script(jscode.getScript(script))
    script.on('message', on_message)
    script.load()

def unload_script(script):
    JSCode.load_script()

def thread_function(scriptToLoad,name):
    jscode = JSCode()
    process = frida.get_usb_device().attach(TargetApp)
    script = process.create_script(jscode.getScript(scriptToLoad))
    script.on('message', on_message)
    script.load()
    time.sleep(2)

layout = [
        [sg.Text('Enter the App Name:')],
        [sg.InputText(),sg.Button('Show Avail Apps',key='en.apps')],
        [sg.Button('Hook App',key='h.app')],
        [sg.Checkbox('DataBase',key='en.db',enable_events=True),
         sg.Checkbox('File Access',key='en.fa',enable_events=True),
         sg.Checkbox('Shared Pref',key='en.sp',enable_events=True),
         sg.Checkbox('HTTP',key='en.http',enable_events=True),

        ],
        [sg.Output(size=(100, 40),key='output')],
        [sg.Text(size=(40,1), key='-LINE-OUTPUT-')],
        [sg.B('Clear Screen',key='ClearOutput')],[sg.Button('Trace',key='h.trace')],
        ]
window = sg.Window('Frukah').Layout(layout)

while True:
    button, values = window.Read()
    print(button, values)
    if button is None or button == 'Exit':
        break
    elif button == 'h.app':
        print("Hooking target app -->" + values[0])
        if values[0] == "":
            sg.Print('Please enter target application before starting...')
        else:
            TargetApp = values[0]
    elif button == 'en.db':
        print(".......Hooking to Database.......")
        x = threading.Thread(target=thread_function, args=("DBAccess","DB",))
        x.start()
    elif button == 'en.fa':
        print(".......Hooking to File Access.......")
        x = threading.Thread(target=thread_function, args=("FileAccess","FA",))
        x.start()
    elif button == 'en.sp':
        print(".......Hooking to Shared Preferences.......")
        x = threading.Thread(target=thread_function, args=("SharedPrefAccess","SP",))
        x.start()
    elif button == 'en.http':
        print(".......Hooking to HTTP/S Requests.......")
        x = threading.Thread(target=thread_function, args=("HTTP","SP",))
        x.start()
    elif button == 'en.apps':
        proc = subprocess.run(["frida-ps -Ua"], shell=True,stdout=PIPE,stderr=PIPE)
        strx = proc.stdout
        sg.Print(strx.decode("utf-8"))
    elif button == 'h.trace':
        x = threading.Thread(target=thread_command, args=("HTTP",))
        x.start()
    elif button == 'ClearOutput':
        window.FindElement('output').Update('')
    elif button == 'loadScript':
        load_script(script_0)
    elif button == 'unloadScript':
        x = threading.Thread(target=thread_function, args=("xxxxxxx",))
        x.start()

############Refrences####################################
#https://github.com/PySimpleGUI/PySimpleGUI/issues/258
#https://erev0s.com/blog/frida-code-snippets-for-android/
#https://ceres-c.it/frida-android-keystore/
#https://www.trustedsec.com/blog/mobile-hacking-using-frida-to-monitor-encryption/
