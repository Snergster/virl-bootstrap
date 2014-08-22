virl-bootstrap
==============

couple files to get salted and configured

prereq: 

install 14.4.1

default user virl

sudo -s

apt-get update

apt-get dist-upgrade -y

apt-get install -y python git

reboot

login as virl

git clone https://github.com/Snergster/virl-bootstrap.git

cd virl-bootstrap

1. sudo ./install_salt.sh

2. cp ./vsettings.ini /home/virl/settings.ini

3. customize /home/virl/settings.ini

3. sudo -s

cd virl-bootstap

4 edit extra.conf for your correct id and salt server

5 cp extra.conf /etc/salt/minion.d

6. service salt-minion restart

7. get your salt key accepted on server

8. salt-call state.sls zero

9 python ./vinstall.py salt

10. salt-call state.sls host

Verify that the IP addresses in /etc/network/interfaces match those outlined in settings.ini

11. sudo reboot

Log in to the server

Run the remaining steps as 'virl'

cd virl-bootstrap

12. python ./vinstall.py all

13. sudo salt-call state.sls images

14. reboot for good measure and your done
