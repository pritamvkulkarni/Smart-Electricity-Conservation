# Pre-execution configuration
This is Config Readme. Please follow the steps below for intended execution of proposed solution.

1) Initial configurations (to use laptop screen as display)
	1.1) Start X launch until an icaon gets displayed in tray.
	1.2) Connect power supply to RPi 2.7/3 and connect ethernet cabel between laptop and pi
	1.3) set ethernet address from laptop configurations setting as: 192.168.2.100 and subnet mask:255.255.255.0 (do not validate nor fill any other entries.) Note : You can set appropiate ip and subnet mask as per your need.
	1.4)run dhcpwiz -> set IP pool from 192.168.2.100 - 105 -> write INI file. -> run until icon gets displayed on the tray.
	1.5)Wait until notification arise from dhcp server saying "assigning IP adress...."
	1.6) Open putty. put IP as 192.168.2.100. Goto SSH -> X11 -> enable X11 forwarding.
2) Login with appropiate credentials on your pi.
3) Run command : lxsession to get GUI session of your pi.   
4) Place the interface.py file in /home/pi directory of raspberry pi so that it appears at boot time only.
5) Place test_sample.py on desktop ( on the path mentioned in interface.py script)
6) Breadboard connections:  pin 3 (o/p) series with resistor(330 ohm) in series with LED anode(long leg) and cathod(short  leg) series with pin 6 (ground).
7) Connect webcam (I used logitech webcam c310) via any of USB port to your pi.
