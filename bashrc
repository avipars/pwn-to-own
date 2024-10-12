# optional, to add these to the end of your bashrc file

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

