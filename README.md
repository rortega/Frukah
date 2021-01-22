# Frukah
This is a Frida/Gui tool used for dynamic analysis of android applications.  The tool allows you to inject/hook javascript to various java methods. This will allow you to follow/modify the applications logic. This tool is normally used for pentesting mobile/android applications.  

This tool does require Frida and PySimpleGui. Go to(https://frida.re/docs/android/) to install Frida use pip to install PySimpleGui

At the moment, this application will only work on Android Studio Emulator. Future releases will work on any mobile device and any thick client (.exe)

To start using:

1. Open a virtiual device in Android - Make sure Frida Server is running
2. Open the app (e.g., DIVA) you want to Hook/Frukah into
3. In Command line enter "$python3 frukah.py"
4. In Frukah enter the App name. Such as for DIVA it will be "jakhar.aseem.diva" or click on "Show Avail Apps" to see loaded applications
5. Click on "Hook App"
6. Select modules/classes you want to Hook/Frukah such as Database, File Access, Shared Preferences, and HTTP

![image](https://raw.githubusercontent.com/rortega/Frukah/main/Screen%20Shot%202021-01-19%20at%2011.25.44%20AM.png)
