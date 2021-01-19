# Frukah
This is a Frida/Gui tool is used for dynamic analysis of android applications.  The tool allows you to inject/hook javascript to various java methods. This will allow you to follow/modify the applications logic. This tool is normally used for pentesting applications.  

This tool does require Frida and PySimpleGui. Go to(https://frida.re/docs/android/) to install Frida use pip to install PySimpleGui

At the moment, this application will only work on Android Studio Emulator. Future releases will work on any mobile device and any thick client (.exe)

To start using:

1. Open a virtiual device in Android
2. Open the app (e.g., DIVA) you want to Hook/Frukah into
3. Enter the App name such as for DIVA it will be jakhar.aseem.diva or click on "Show Avail Apps" to see loaded applicaitns
4. Click on "Hook App"
5. Select moduels you want to Hook/Frukah such as Database, File Access, Shared Preferences , and HTTP

