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

* Send the file to another computer (run this command from the recieving computer terminal)
Make sure to allow EVERYONE to write ot that folder 

    ```bash
    scp pi@10.0.0.2:/home/pi/handshakes/pcaps.zip  C:\temp
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

* Check service status

    ```bash
    sudo systemctl status pwnagotchi
    ```

## Plugins

* List all available plugins

    ```bash
    sudo pwnagotchi plugins list
    ```
    
* Update all plugins

    ```bash
    sudo pwnagotchi plugins update
    ```

* Install plugin x (change x to whatever plugin name you want)

    ```bash
    sudo pwnagotchi plugins install x
    ```

* Uninstall plugin x

    ```bash
    sudo pwnagotchi plugins uninstall x
    ```

* Disable plugin x

    ```bash
    sudo pwnagotchi plugins disable x
    ```

* Enable plugin x

    ```bash
    sudo pwnagotchi plugins enable x
    ```


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

* See all "uploaded" pcap file names to wpa-sec

    ```bash
    sudo cat /root/.wpa_sec_uploads
    ```

* Remove those recorded files (locally only)

    ```bash
    sudo rm /root/.wpa_sec_uploads
    ```
