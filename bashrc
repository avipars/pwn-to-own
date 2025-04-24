# optional, to append these to the end of your bashrc file vs nano .bashrc, then once added save and close nano and then run this "source .bashrc"
# purpose: allows you to bulk install and uninstall plugins 

# Start Custom Functions

# the following only take effect after reboot
pinstall() {
    for plugin in "$@"; do
        sudo pwnagotchi plugins install "$plugin"
    done
}

puninstall() {
    for plugin in "$@"; do
        sudo pwnagotchi plugins uninstall "$plugin"
    done
}

pdisable() {
    # oddly, you can disable a non-existent plugin, the command ends up adding another line to the config.toml file
    for plugin in "$@"; do
        sudo pwnagotchi plugins disable "$plugin"
    done
}

penable() {
    for plugin in "$@"; do
        sudo pwnagotchi plugins enable "$plugin"
    done
}

# now you can run "puninstall ext1 ext2" and so on via ssh terminal, to uninstall a bunch of plugins at once (and it works similarly for pinstall)
