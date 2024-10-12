# optional, to add these to the end of your bashrc file

pinstall() {
    sudo pwnagotchi plugins install "$1"
}
puninstall() {
    sudo pwnagotchi plugins uninstall "$1"
}
