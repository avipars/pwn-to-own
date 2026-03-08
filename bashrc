# optional, to append these to the end of your bashrc file vs nano .bashrc, then once added save and close nano and then run this "source .bashrc"
# purpose: allows you to bulk install and uninstall plugins 

# Start Custom Functions

pdisable() {

    if [ "$#" -eq 0 ]; then
        echo "Error: No plugin names provided to disable."
        return 1
    fi

    # oddly, you can disable a non-existent plugin, the command ends up adding another line to the config.toml file
    for plugin in "$@"; do
        sudo pwnagotchi plugins disable "$plugin"
    done
}

penable() {
    
    if [ "$#" -eq 0 ]; then
        echo "Error: No plugin names provided to enable."
        return 1
    fi

    for plugin in "$@"; do
        sudo pwnagotchi plugins enable "$plugin"
    done
}


# running any of the following commands only take effect after reboot (ex: pinstall auto-tune probeReq fix_region sorted_pwn)

pinstall() {

    if [ "$#" -eq 0 ]; then
        echo "Error: No plugin names provided to install."
        return 1
    fi

    for plugin in "$@"; do
        sudo pwnagotchi plugins install "$plugin"
    done
}

puninstall() {

    if [ "$#" -eq 0 ]; then
        echo "Error: No plugin names provided to uninstall."
        return 1
    fi

    for plugin in "$@"; do
        sudo pwnagotchi plugins uninstall "$plugin"
    done
}


# now you can run "puninstall ext1 ext2" and so on via ssh terminal, to uninstall a bunch of plugins at once (and it works similarly for pinstall)
