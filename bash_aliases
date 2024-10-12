# make a file here: `nano ~/.bash_aliases` and then paste the following... after you save and close, run `source  ~/.bash_aliases` to apply changes

# Avi Alias
alias pupdate='sudo pwnagotchi plugins update'
alias plist='sudo pwnagotchi plugins list'
alias pplug='/usr/local/share/pwnagotchi/available-plugins'
alias pconf='/etc/pwnagotchi/config.toml'
alias nconf='sudo nano /etc/pwnagotchi/config.toml'
alias papply='systemctl restart pwnagotchi'
alias pstat='sudo systemctl status pwnagotchi'
alias pstat='cd /var/tmp/pwnagotchi/sessions/'
alias phand='cd  /home/pi/handshakes/'


#from others
alias pwnlog='tail -f -n300 /var/log/pwn*.log | sed --unbuffered "s/,[[:digit:]]\{3\}\]//g" | cut -d " " -f 2-'
alias pwnver='python3 -c "import pwnagotchi as p; print(p.__version__)"'



