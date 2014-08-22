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

9 python ./vinstall salt

10. salt-call state.sls host

verify /etc/networking/interfaces is how you like it

11. reboot

# rest of the steps done as virl

12. vinstall all

13. sudo salt-call state.sls images

14. reboot for good measure and your done
