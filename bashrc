# optional, to add these to the end of your bashrc file vs nano .bashrc, then once added save and close nano and then run this "source .bashrc"

#Start Custom Functions
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

# now you can run "puninstall ext1 ext2" and so on, to uninstall a bunch of plugins at once (and it works similarly for pinstall)