# to be run on the pwnagotchi
iwconfig
#  run lsusb -v to get verbose details about your external wifi usb gadget, then find the publisher and vendor values to replace below
sudo usb_modeswitch -p 1a2b -v 0bda -K # change after P to publisher value, and after V to vendor value
sudo rfkill unblock all
sudo systemctl restart  pwnagotchi
sudo ifconfig wlan0 up
sudo airmon-ng start wlan0


lsusb
iw list
