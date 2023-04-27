# SmartDoorbell-link-to-Telegram-API
This is a smartdoorbell that will send a notification and picture of the guest to the home owner's telegram app

Hardware needed for this
-raspberry pi (anywhere between 3 or 4 for best performance)
-speaker (in my case I used a usb/jack speaker, GPIO configured speaker also works just change the program to cater to that speaker's needs)
-camera (same I used usb speaker, you can use a GPIO camera here to)
-wires
-ethernet cable (to connect the system to the internet you need a cable or you can just add the wifi's address direcctly to the raspian OS installed)
-push button

there are tutorials and schematics on the internet on how to configure these hardwares into the raspberry pi and comes with it are the libraries needed for said hardwares in order to work with the pi

Software needed
-raspberry pi imager
-telegram

Telegram
make a bot in telegram using the "Botfather" and save the token to use in the system. To look for your account ID search for userinfobot to see your user info

The program should be able to send a picture to the home owner's telegram account when the program detects that a push button is pressed. The home owner then would have the option to send back a voice message to the program for the guest with the telegram's voice message functionality

