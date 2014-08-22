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
apt-get install git
clone this repo
cd virl-bootstrap

1. sudo ./install_salt.sh

2. move vsettings to /home/virl/settings.ini

3. customize /home/virl/settings.ini

3. sudo -s

4 edit extra.conf for your correct id and salt server

5 cp extra.conf /etc/salt/minion.d

6. service salt-minion restart

7. get your salt key accepted on server

8. salt-call state.sls zero

9 vinstall salt

10. salt-call state.sls host

verify /etc/networking/interfaces is how you like it

11. reboot

# rest of the steps done as virl

12. vinstall all

13. sudo salt-call state.sls images

14. reboot for good measure and your done
