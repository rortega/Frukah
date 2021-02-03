import PySimpleGUI as sg
import subprocess
from subprocess import PIPE
import time
import threading



proc = subprocess.run(["adb shell pm list packages"], shell=True,stdout=PIPE,stderr=PIPE)
strx = proc.stdout

names = strx.decode("utf-8").split("\n")


layout = [  [sg.Text('Listbox with search')],
            [sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_')],
            [sg.Listbox(names, size=(80,40), enable_events=True, key='_LIST_')],
            [sg.Output(size=(79, 6),key='output')],
            [sg.Button('Chrome'),sg.Button('Download'), sg.Button('Exit')]]


window = sg.Window('Download 2 Download APK').Layout(layout)

selectedItem = ""
# Event Loop
while True:
    event, values = window.Read()

    if event is None or event == 'Exit':                # always check for closed window
        break
    if values['_INPUT_'] != '':                         # if a keystroke entered in search field
        search = values['_INPUT_']
        new_values = [x for x in names if search in x]  # do the filtering
        window.Element('_LIST_').Update(new_values)     # display in the listbox
    else:
        window.Element('_LIST_').Update(names)          # display original unfiltered list

    if event == '_LIST_' and len(values['_LIST_']):     # if a list item is chosen
        selectedItem = values['_LIST_']
        print('Selected:'+ values['_LIST_'][0])
        print('Click Download 2 Dowload APK...')
    if event == 'Download':
        apkPath = "adb shell pm path " + selectedItem[0][8:]
        proc = subprocess.run(apkPath, shell=True,stdout=PIPE,stderr=PIPE)
        strx = proc.stdout
        download = "adb pull " + strx.decode("utf-8")[8:-1] + " ./Downloads/"
        subprocess.run(download, shell=True)
        print("Downloaded to ./Downloads in local directory as base.apk")
        #change your locaion of dex to jar
        getJarFromApk = "sh ./dex2jar/d2j-dex2jar.sh -f -o ./Downloads/"+selectedItem[0][8:]+"_jar.jar ./Downloads/base.apk"
        subprocess.run(getJarFromApk, shell=True)
        print("Converted APK to Jar....you can now open it with a tool like JD-GUI to view source")
        subprocess.run("apktool d ./Downloads/base.apk -o ./Downloads/{0}".format(selectedItem[0][8:]), shell=True,stdout=PIPE,stderr=PIPE)
        print("Decompiled code to ./Downloads/{0}".format(selectedItem[0][8:]))


window.Close()
