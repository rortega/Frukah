#https://github.com/PySimpleGUI/PySimpleGUI/issues/258
import PySimpleGUI as sg
import time
import sys
import frida, sys
from JSCode_Class import JSCode_Class
from CreateCode import CreateCode
import subprocess
from subprocess import PIPE
import time
import threading
import random

TargetApp = ""
TargetClass = ""
script_0 = None;

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
counter = 0
generated_script = ""

def generate_script_from_response(message,data):
    global counter
    global generated_script
    counter = counter + 1
    generated_script = generated_script + CreateCode.getScript(message['payload'],str(counter)) #returns method for each active class


def thread_function(scriptToLoad,targetClass):
    jscode = JSCode_Class()
    process = frida.get_usb_device().attach(TargetApp)
    script = process.create_script(jscode.getScript(scriptToLoad,targetClass))
    script.on('message', generate_script_from_response)
    script.load()
    print("-.------finished-----.-")
    printCoffee()
    time.sleep(1)

def printCoffee():
    num = random.randrange(1,len(JSCode_Class.quote)-1)
    print(JSCode_Class.quote[num])



layout = [
        [sg.Text('Enter the App Name:')],
        [sg.InputText(),sg.Button('Show Modules',key='en.mod')],
        [sg.Text('Enter Class Search:')],
        [sg.InputText(),sg.Button('Show Classes',key='en.app'),sg.Button('Generate Code',key='gen.meth')],

        [sg.Text('Enter Class Name:')],
        [sg.InputText(),sg.Button('Show Methods',key='en.meth')],



        [sg.Output(size=(100, 40),key='output')],
        [sg.Text(size=(40,1), key='-LINE-OUTPUT-')],
        [sg.B('Clear Screen',key='ClearOutput')],

        ]

window = sg.Window('Frukah - Classes').Layout(layout)


while True:
    button, values = window.Read()
    print(button, values)

    if button is None or button == 'Exit':
        break
    elif button == 'en.app':

        printCoffee()
        print("Hooking target app -->" + values[0])
        if values[0] == "":
            print('Please enter a target application before starting...')
        else:
            print(values)
            TargetApp = values[0]
            x = threading.Thread(target=thread_function, args=("ClassInfo",values[1],))
            x.start()
    elif button == 'en.mod':
        printCoffee()
        print("Retrieving Modules -->" + values[0])
        TargetApp = values[0]
        x = threading.Thread(target=thread_function, args=("EnumModules",values[0],))
        x.start()
    elif button == 'gen.meth':
        printCoffee()
        print("Generated code for listed classes -->" + values[1])
        TargetApp = values[0]
        x = threading.Thread(target=thread_function, args=("GetMethodsFromClassName",values[1],))
        x.start()
        print("Generating Frida Script. Generating will take a minute...")
        printCoffee()
        time.sleep(5)
        printCoffee()
        print("take a coffee break on me...still generating")
        printCoffee()
        time.sleep(6)
        printCoffee()
        print("take a coffee break on me...still generating")
        time.sleep(7)


        file = open('./'+values[1]+'.js','w')
        file.write('Java.perform(function () { \n' +generated_script+ '\n });')
        file.close()
        print('\nCode complete. File saved to ./{0}.js'.format(values[1]))
        print('Use the generated code enter the following commands : ')
        print('###Hooking before starting the app###')
        print('frida -U --no-pause -l {0}.js -f {1}'.format(values[1],values[0]))
        print('###Basic frida hooking - Launch app first then Hook###')
        print('frida -U {0} -l {1}.js'.format(values[0],values[1]))


    elif button == 'ClearOutput':
        window.FindElement('output').Update('')
