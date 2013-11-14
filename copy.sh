#!/bin/sh
sshpass -p 'linuxcnc' scp -r * linuxcnc@192.168.1.23:~/linuxcnc/configs/ARM/BeagleBone/alex-Bridge/gui/
sshpass -p 'linuxcnc' ssh linuxcnc@192.168.1.23 'chmod +x ~/linuxcnc/configs/ARM/BeagleBone/alex-Bridge/gui/qmlgui.py'