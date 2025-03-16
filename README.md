# Tips and tricks for pwnagotchi (pi0w and 2.8.9 Jayofelony's build)

Code snippets are [here](SNIPPETS.md)

How to use an usb wifi dongle [here](EXTERNALWIFI.md)

Have fun with stats [here](STATS.md)

### Plugins

#### Directories

in the config file, set: 
```bash
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"

/etc/pwnagotchi/custom_plugins  # your custom plugins are here by default, whether they are enabled or not
```
in the config file, you can add or remove repositories that have plugins installed by modifying this array:

```bash
main.custom_plugin_repos = [   "https://github.com/evilsocket/pwnagotchi-plugins-contrib/archive/master.zip",

]

```

make sure that each element in the array ends with /archive/master.zip or something similar, otherwise the plugin may not be loaded properly

You can make your own repo with plugins, or just copy a plugin you like directly to this directory /etc/pwnagotchi/custom_plugins just as well (and then enable it) 

```/usr/local/share/pwnagotchi/available-plugins``` # plugins that are available to be installed - if you used a repo and did update... those plugins would appear here


#### Bluetooth pairing

##### For older builds of the pwnagotchi only 

The 4th section of this [guide](https://github.com/Xyl0se/Pwnagotchi-new-guerilla-guide#42-pair-pwnagotchi-with-phone-important
) is perfect and still works besides for paired-devices on my Pi zero 2w. 

via SSH: 

```bash
ssh pi@10.0.0.2
sudo su
bluetoothctl
scan on
discoverable on
untrust *device adress*  #run this command a few times
remove *device adress*   #run this command a few times
paired-devices #make sure list is empty, if not- run previous command until it is empty
pair *device adress* #*In short time (maybe not immediately) you will be prompted on the phone to allow connection from your pwnagotchi hostname- pair*
trust *device adress*

# optional to run 
connect *device address*
exit
```

On android, you need to enable Blueooth Tethering on top of bluetooth you would normally. This is found in the Mobile Hotspot and Tethering settings page. 

Android also prefers IP addresses in the 192.168.44.x range.

Pairing multiple devices (of same or different types) is also feasible. It turns out that the [bt-tether plugin](https://github.com/jayofelony/pwnagotchi/blob/f36d4aea7735037eb401de8e12e5e24a8a676300/pwnagotchi/plugins/default/bt-tether.py#L163)  doesn't even check/verify what 'android-phone' or 'ios-phone' is... Meaning, any arbitrary text can replace that in your config!

For example:

```main.plugins.bt-tether.devices.blah.enabled = true```

is valid, but certainly less descriptive. Of course, the 'blah' keyword wouldneed to remain consistent across of all the bt-tether settings applied to that device. 

##### For more recent builds

Refer to this [guide](https://pwnagotchi.org/customization/bt-tethering/index.html)