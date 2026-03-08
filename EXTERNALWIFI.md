# External Wi-Fi Dongle

Firstly, your adapater needs to support monitor mode (as well as packet injection). I used this [one](https://s.click.aliexpress.com/e/_c3xqzDOX) which works well and supports 5ghz bands too, it has okay range and is quite affordable! There are plenty of other ones on the market that may even work better but are much more expensive.  

For an adapter that does work out of the box, and you don't care about the Pi internal wifi module add "dtoverlay=disable-wifi" to your /boot/firmware/config.txt. It disables the internal Wi-Fi and the external adaptor should work. Then do a reboot. 

Not all Wi-Fi adapater drivers are supported (nor installed on the Pi) out of the box. For certain popular chipsets, there may be workarounds to getting it recognized and working nonetheless, but for beginners it is a pain (I know from personal experience)! 

If it isn't recognized and ready out of the box: 

* You should use ```lsusb -v``` to find information about your chipset and then you can try to google it and see if there is a driver or simple solution 

* My adapter was in a CD Driver mode initially, and using this [script](scripts/external.sh) I was able to switch modes and get it working. I had to run this script each time I plugged in the wifi adapter.

    - On the otherhad, you can install a 3rd party modified driver (but who knows if the code is safe) 
    
    - Or create a ```usb_modeswitch.d``` file in the right directory to apply the changes automatically (from CD Driver to regular WiFi Adapter), then you still need to enable monitor mode and wait till the pwnagotchi service sees it (or if you are impatient, restart the pwnagotchi service and then it will bring up the external adapater quickly itself). 

        * TODO add documentation on usb_modeswitch.d, but for now just google it!


If you have a Pi Zero (or Zero 2), ensure the USB Wi-Fi dongle is connected to the DATA PORT (the one in the middle) and not the POWER ONLY PORT. You will most likely need a USB OTG Adapter to connect the dongle. 


- Once you get this working, you can disable the "fix-services" plugin on the pwnagotchi as you shouldn't experience another blind bug (unless you switch back to the onboard Wi-Fi)

Scripts

* Untested - [script](https://github.com/Terminatoror/pwnagotchi-auto-antenna) to let you hotswap external wifi 

* Another untested WIP [script](https://github.com/unagisan69/pwnagotchi-external-wifi-plugin) to do a similar thing 

Credit

* https://pwnagotchi.org/modifications/index.html#usb-antenna


[Advanced users only] withouut disabling the internal wifi adapter... you can access both wireless interfaces on the pi at the same time and then change the interface names, and have more flexibility. 