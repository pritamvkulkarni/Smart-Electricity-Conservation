<h2> Pre-execution configuration </h2>
This is Config Readme. Please follow the steps below for intended execution of proposed solution.

1. Initial configurations (for remote forwarding of your PI GUI)
	1. Start **X launch** until an icon gets displayed in taskbar tray.
	1. Connect power supply to *RPi 2.7/3* and create a LAN using ethernet cable between your machine and PI
	1. Set IP address from machine configurations setting as: 192.168.2.100 and subnet mask:255.255.255.0 (do not validate nor fill any other entries.) Note : You can set appropiate ip and subnet mask as per your need.
	1. Run **dhcpwiz** -> set IP pool from 192.168.2.100 - 105 -> write *INI file*. -> Run.
	1. Wait until notification arise from dhcp server saying *assigning IP adress....*
	1. Open putty. put IP as 192.168.2.100. Goto SSH -> X11 -> enable X11 forwarding.
2. Login with appropiate credentials on your pi.
3. Run *lxsession* command to get GUI session of your pi.   
4. Place the *interface.py* file in */home/pi* directory of raspberry pi to get interface frame prompt when pi boots completely.
5. Place test_sample.py on respective path ( on the path mentioned in interface.py script)
6. Breadboard connections:  Pin 3 (o/p) series with *resistor(330 ohm)* in series with *LED anode(long leg)* and *cathod(short  leg)* series with pin 6 (ground).
7. Connect webcam (I used *Logitech webcam C310*) via any of USB port to your pi.
8. Once you are able to access Raspberry Pi console, install Python package used for Raspberry Pi GPIO programming **RPi.GPIO**. It is already installed in Raspbian, the default operating system for Pi. 
   If not, you can install it using :
   * sudo pip install RPi.GPIO
