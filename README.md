# Backup Files:


Run this in your SSH window (to the pi):

sudo tar -czvf pwny-backup.tar.gz /root/brain.json /root/handshakes/ /root/peers/ /etc/pwnagotchi/ /usr/local/share/pwnagotchi/custom-plugins/

And to pull the new file (from pi to windows):

scp pi@10.0.0.2:/home/pi/pwny-backup.tar.gz C:\temp 

If your pi has a different username, then change PI to your username... and you can point the donwload to go to another directory by changing from C:\temp to elsewhere
