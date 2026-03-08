# Useful snippets

Make sure to understand before running as well as changing usernames, directories where relevant

### Backup

* Run this in your SSH window (to the pi):

    ```sudo tar -czvf pwny-backup.tar.gz /root/brain.json /root/handshakes/ /root/peers/ /etc/pwnagotchi/ /usr/local/share/pwnagotchi/custom-plugins/```

    if you moved your handshakes file to ```/home/pi/handshakes/```, change it accordingly. Additionally, if you are on Jay's new images without AI, you can remove ```/root/brain.json``` from the command above
  
* And to pull the new file (from pi to windows):

    ```scp pi@10.0.0.2:/home/pi/pwny-backup.tar.gz C:\temp``` 

* If your pi has a different username, then change pi to your username... and you can point the donwload to go to another directory by changing from C:\temp to elsewhere


## PCAPs

Assuming your PCAPs are in: ```/home/pi/handshakes```, you can check via the ```config.toml``` file under ```bettercap.handshakes```

If they are in ```/root/handshakes/```, you can modifyy the scripts accordingly.

* Zip all your PCAPs to 1 file

    ```bash
    sudo zip -r pcaps.zip /home/pi/handshakes
    ```

* (Optional) Grab the file metadata as well (last modified, permissions, etc.)

    ```bash
    cd /home/pi/handshakes
    ls -la > metadata.txt
    ```
  
* Send the file to another computer (run this command from the recieving computer terminal)
Make sure to allow EVERYONE to write ot that folder 

    ```bash
    scp pi@10.0.0.2:/home/pi/handshakes/pcaps.zip  C:\temp
    ```

* Alternatively, you can use file globbing and scp to grab all ```.pcaps``` or all files in a given directory

    All files
    ```bash
    scp pi@10.0.0.2:/home/pi/handshakes/*  C:\temp 
    ```
    
    pcap only
    ```bash
    scp pi@10.0.0.2:/home/pi/handshakes/*.pcap  C:\temp 
    ```
* With Linux or WSL, run this to convert pcaps to a crackable format (after installing hcxtools)

    ```bash
    hcxpcapngtool *.pcap -o candidates.hc22000 -E essid.wordlist
    ```

* If you are new to hashcat on windows, consider creating a ```hashcat.bat``` file 

    ```bash
    @echo off
    REM where this is the directory of hashcat
    pushd "C:\Program Files\hashcat" 
    hashcat.exe %*
    popd
    ```

    Now add ```C:\Program Files\hashcat``` to your PATH, and you can call ```hashcat.bat``` from anywhere to get it running

* Run this on a computer with mergecap installed (comes with wireshark)

    ```bash
    mergecap -a -V -w allpcap.pcap C:\temp\pcaps\*.pcap
    ```

* Remove your old PCAPs (on the pi)

    ```bash
    sudo rm /home/pi/handshakes/*
    ```


## Config

* Edit the config file in nano (you can change it to VIM or whatever)

    ```bash
    sudo nano /etc/pwnagotchi/config.toml
    ```

* Restart pwnagotchi service (good to do after modifying the config file)

    ```bash
    systemctl restart pwnagotchi
    ```

    or via 
     ```bash
    pwnkill
    ```

* Check service status

    ```bash
    sudo systemctl status pwnagotchi
    ```

## Plugins

* List all available plugins

    ```bash
    sudo pwnagotchi plugins list
    ```

    or a shortcut if you added via bash_aliases

    ```bash
    plist
    ```
    
* Upgrade plugin(s)

    ```bash
    sudo pwnagotchi plugins upgrade
    ```

    without an argument, it will search for new versions of all your plugins and try to upgrade them all [source code](https://github.com/jayofelony/pwnagotchi/blob/6808063e9b46d3b6e3d7c0e26cb94b9b752bfddb/pwnagotchi/plugins/cmd.py#L16). You can add a regex filter as the argument to only update plugins wit names matching your filter


    or a shortcut if you added via bash_aliases (with no arguments)

    ```bash
    pupgrade
    ```


* Update plugin database

    ```bash
    sudo pwnagotchi plugins update
    ```

    or a shortcut if you added via bash_aliases

    ```bash
    pupdate 
    ```

* Install plugin x (change x to whatever plugin name you want)

    ```bash
    sudo pwnagotchi plugins install x
    ```

    or a shortcut if you added via bashrc

    ```bash
    pinstall x 
    ```

    and you can even install multiple plugins in one go via the shortcut

    ```bash
    pinstall x y 
    ```


* Uninstall plugin x

    ```bash
    sudo pwnagotchi plugins uninstall x
    ```

    or a shortcut if you added via bashrc

    ```bash
    puninstall x 
    ```

    and you can even uninstall multiple plugins in one go via the shortcut

    ```bash
    puninstall x y 
    ```

* Disable plugin x

    ```bash
    sudo pwnagotchi plugins disable x
    ```

    or a shortcut if you added via bashrc

    ```bash
    pdisable x 
    ```

    and you can even disable multiple plugins in one go via the shortcut

    ```bash
    pdisable x y 
    ```

* Enable plugin x

    ```bash
    sudo pwnagotchi plugins enable x
    ```

    or a shortcut if you added via bashrc

    ```bash
    penable x 
    ```

    and you can even enable multiple plugins in one go via the shortcut

    ```bash
    penable x y 
    ```

* Edit plugin x

    ```bash
    sudo pwnagotchi plugins edit x
    ```

   It will try to use vim by default, unless yopu add a environment variable EDITOR with nano or another one

## session-stats 

Scripts/Code relating to using this plugin

* Zip your session-stats data

    ```bash
    sudo zip -r stats.zip /var/tmp/pwnagotchi/sessions
    ```

* Send your stats file to another machine (run this command from the recieving computer terminal)

    ```bash
    scp pi@10.0.0.2:/var/tmp/pwnagotchi/sessions/stats.zip  C:\temp
    ```

* Remove your old session-stats files

    ```bash
    sudo rm /var/tmp/pwnagotchi/sessions/*
    ```

## wpa-sec

* See all "uploaded" pcap file names to wpa-sec (this is what your plugin thinks got uploaded but may not match https://wpa-sec.stanev.org/?my_nets)

    ```bash
    sudo cat /root/.wpa_sec_uploads
    ```

* Remove those recorded files (locally only, wpa-sec plugin will then try to re-upload all your PCAPS)

    ```bash
    sudo rm /root/.wpa_sec_uploads
    ```
