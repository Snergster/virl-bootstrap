virl-bootstrap
==============

couple files to get salted and configured

prereq: 
install 14.4.1
default user virl
going to need at least python installed and get base upgrades done. 
sudo -s
apt-get update
apt-get dist-upgrade -y
apt-get install python
reboot
login as virl
clone this repo
cd virl-bootstrap

1. sudo ./install_salt.sh

2. move vsettings to /home/virl/settings.ini

3. customize /home/virl/settings.ini

3. sudo -s

3.5 edit extra.conf for your correct id and salt server
3.6 cp extra.conf /etc/salt/minion.d

4. service salt-minion restart

5. get your salt key accepted on server

6. salt-call state.sls zero

6.5 vinstall salt

7. salt-call state.sls host

**verify /etc/networking/interfaces is how you like it

8. reboot

# rest of the steps done as virl

9. vinstall all

10. sudo salt-call state.sls images

11. reboot for good measure and your done