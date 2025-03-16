# External Wi-Fi Dongle

Firstly, your adapater needs to support monitor mode (as well as packet injection)

Add this: "dtoverlay=disable-wifi" to your /boot/firmware/config.txt. It disables the internal Wi-Fi and the external adaptor should work. Then do a reboot 

- Not all Wi-Fi adapater drivers are supported (nor installed on the Pi) out of the box. 

- If you have a Pi Zero, ensure the USB Wi-Fi dongle is connected to the DATA PORT (the one in the middle) and not the POWER ONLY PORT. You will most likely need a USB OTG Adapter to connect the dongle. 

- Once you get this working, you can disable the "fix-services" plugin on the pwnagotchi as you shouldn't experience another blind bug (unless you switch back to the onboard Wi-Fi)

Scripts

* Untested - [script](https://github.com/Terminatoror/pwnagotchi-auto-antenna) to let you hotswap external wifi 

* Another untested WIP [script](https://github.com/unagisan69/pwnagotchi-external-wifi-plugin) to do a similar thing 

Credit

* https://pwnagotchi.org/modifications/index.html#usb-antenna

