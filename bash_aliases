# make a file here: `nano ~/.bash_aliases` and then paste the following... after you save and close, run `source  ~/.bash_aliases` to apply changes

# Avi Alias
alias pupdate='sudo pwnagotchi plugins update'
alias plist='sudo pwnagotchi plugins list'
alias pplug='ls /usr/local/share/pwnagotchi/available-plugins'
alias pconf='cat /etc/pwnagotchi/config.toml'
alias nconf='sudo nano /etc/pwnagotchi/config.toml'
alias papply='systemctl restart pwnagotchi'
alias pstat='sudo systemctl status pwnagotchi'
alias psess='cd /var/tmp/pwnagotchi/sessions/'
alias phand='cd /home/pi/handshakes/'
alias pshut='sudo shutdown -h now'
alias prestart='sudo shutdown -r now'
alias piconf='cat /boot/firmware/config.txt'
alias npiconf='sudo nano /boot/firmware/config.txt'