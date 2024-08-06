# Tips and tricks for pwnagotchi (pi0w and 2.8.9 Jayofelony's build)


## Backup Files:


Run this in your SSH window (to the pi):

sudo tar -czvf pwny-backup.tar.gz /root/brain.json /root/handshakes/ /root/peers/ /etc/pwnagotchi/ /usr/local/share/pwnagotchi/custom-plugins/

And to pull the new file (from pi to windows):

scp pi@10.0.0.2:/home/pi/pwny-backup.tar.gz C:\temp 

If your pi has a different username, then change PI to your username... and you can point the donwload to go to another directory by changing from C:\temp to elsewhere




## Config

sudo nano /etc/pwnagotchi/config.toml #open the cofig file in text editor

If you have the web-ui on and webcfg enabled, you can edit config there too!


### Plugins

#### Directories:

in the config file, set: 

main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"

/etc/pwnagotchi/custom_plugins  # your custom plugins are here by default, whether they are enabled or not

in the config file, you can add or remove repositories that have plugins installed by modifying this array:

main.custom_plugin_repos = [   "https://github.com/evilsocket/pwnagotchi-plugins-contrib/archive/master.zip",

]

make sure that each element in the array ends with /archive/master.zip or something similar, otherwise the plugin may not be loaded properly

You can make your own repo with plugins, or just copy a plugin you like directly to this directory /etc/pwnagotchi/custom_plugins just as well (and then enable it) 

#### Useful commands: 

sudo pwnagotchi plugins list #shows available plugins

sudo pwnagotchi plugins update #reuqires internet

sudo pwnagotchi plugins install whatever #installs plugin called whatever

sudo pwnagotchi plugins whatever enable #change whatever to the plugin name you want to enable (many are disabled by default even after install)

sudo pwnagotchi plugins whatever disable

### Handshakes:

Normally stored in /root/handshakes/

but via the config file, many users have put it here: /home/pi/handshakes/ 



### Session stats

Stored here by default: /var/tmp/pwnagotchi/sessions/



