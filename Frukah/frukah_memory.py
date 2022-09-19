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

jscode = """
  var ranges = Process.enumerateRangesSync({protection: 'r--', coalesce: true});
  var range;
 function processNext(){
  range = ranges.pop();
  if(!range){
				console.log('Ending the memory search')
				return;
			}
 Memory.scan(range.base, range.size, "%s", {
				onMatch: function(address, size){
                        console.log('--------------------------------------------------');
						console.log('[+] Pattern found at: ' + address.toString());
                        console.log('--------------------------------------------------');
                        let start = "0x"+String(Math.abs(%d).toString(16));
                        let num = address-start;
                        var mem_content = Memory.readByteArray(ptr( num ), %d);

                         console.log(mem_content);
					},
				onError: function(reason){
						console.log('[!] There was an error scanning memory');
					},
				onComplete: function(){
						processNext();
					}
				});
 }
  processNext()
"""

jscode_overwrite = """
  var ranges = Process.enumerateRangesSync({protection: 'r--', coalesce: true});
  var range;
 function processNext(){
   console.log('overwrite........')
        //0x33,0x34,0x2e,0x31
        var arrayPtr = ptr(%s)
        Memory.writeByteArray(arrayPtr, [%s]);

 }
  processNext()
"""


def search_memory(values):
    print(values) # in.app.name in.search.string in.pre.pos in.mem.size
    hex_search_pattern = ' '.join(r'{:02X}'.format(ord(chr)) for chr in values['in.search.string'])
    print(hex_search_pattern)
    print(values['in.app.name'])
    try:
        process = frida.get_usb_device().attach(int(values['in.app.name']))
        script = process.create_script(jscode % (hex_search_pattern,int(values['in.pre.pos']),int(values['in.mem.size'])))
        script.on('message', on_message)
        print('[*]')
        script.load()
        time.sleep(2)
    except BaseException as e:
        #print(f"Unexpected {err=}, {type(err)=}")
        print(e)
        print("Enter a PID number for the app. ")
        print("Enter a number for Preview Position (0-5)")
        print("Enter a number for Memory Size (10-1000).")
    except:
        print('error2')

def overwrite_memory(values):
    print('overwrite....;)')
    print(values['in.ow.address'])
    print(values['in.ow.content'])
    print('aaa')
    try:
        process = frida.get_usb_device().attach(int(values['in.app.name']))
        hex_pattern = ''.join(str(hex(ord(chr)))+',' for chr in values['in.ow.content'])[:-1]
        script = process.create_script(jscode_overwrite % (values['in.ow.address'],hex_pattern))
        script.on('message', on_message )
        print('[*] overwrote' + values['in.ow.address'] +"  Hex:" +hex_pattern )
        script.load()
        time.sleep(2)
    except BaseException as e:
            #print(f"Unexpected {err=}, {type(err)=}")
        print(e)
    except:
        print('error2')


def thread_function(scriptToLoad,name):
    jscode = JSCode()
    process = frida.get_usb_device().attach(TargetApp)
    script = process.create_script(jscode.getScript(scriptToLoad))
    script.on('message', on_message)
    script.load()
    time.sleep(2)

layout = [
        [sg.Button('Show Avail Apps',key='en.apps')],
        [sg.Text('Enter the App PID'),sg.InputText(key='in.app.name',size=(12)),sg.Button('Hook App',key='h.app')],
        [sg.Output(size=(120, 40),key='output')],
        [sg.Text(size=(80,1), key='-LINE-OUTPUT-')],
        [
             [sg.Text('Search String:'),
             sg.InputText(key='in.search.string'),
             sg.Button('Search',key='b.search'),
             sg.Text('Preview Position:'),
             sg.InputText(default_text='0',size=(3),key='in.pre.pos'),
             sg.Text('Memory Size:'),
             sg.InputText(default_text='50',size=(3),key='in.mem.size') ],

        ],
        [sg.Text('-------------------------------------------------------------------------------------Memory Overwrite------------------------------------------------------------------------------------')],

        [
             [sg.Text('Address:'),
             sg.InputText(key='in.ow.address',size=(20)),
             sg.Text('Content:'),
             sg.InputText(key='in.ow.content',size=(20)),

             sg.Button('Overwrite Memory',key='b.overwrite'), ],

        ],

        [sg.Button('Trace',key='h.trace')],
        ]
window = sg.Window('Frukah Memory ;)').Layout(layout)

while True:
    button, values = window.Read()
    #print(button, values)
    if button is None or button == 'Exit':
        break
    elif button == 'h.app':
        print("Hooking target app -->" + values['in.app.name'])
        if values['in.app.name'] == "":
            sg.Print('Please enter target application before starting...')
        else:
            TargetApp = values['in.app.name']
    elif button == 'en.apps':
        proc = subprocess.run(["frida-ps -Ua"], shell=True,stdout=PIPE,stderr=PIPE)
        strx = proc.stdout
        sg.Print(strx.decode("utf-8"))
    elif button == 'h.trace':
        x = threading.Thread(target=thread_command, args=("HTTP",))
        x.start()
    elif button == 'b.search':
        print('searching....;)')
        search_memory(values)
    elif button == 'b.overwrite':
        overwrite_memory(values)
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
