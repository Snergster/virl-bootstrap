virl-bootstrap
==============

couple files to get salted and configured

prereq: 

install 14.4.1

default user virl

Login into your VIRL system and enter the following commands

sudo -s

apt-get update

apt-get dist-upgrade -y

apt-get install -y python git

reboot

On reboot, login as virl. Enter the following commands

git clone https://github.com/Snergster/virl-bootstrap.git

cd virl-bootstrap

sudo ./install_salt.sh

cp ./vsettings.ini /home/virl/settings.ini

Edit /home/virl/settings.ini as required

sudo -s

cd virl-bootstrap

Edit extra.conf for your correct id and salt server

cp extra.conf /etc/salt/minion.d

service salt-minion restart

Get your salt key accepted on server

salt-call test.ping

Ensure that the result is 'True'

salt-call state.sls zero

python ./vinstall.py salt

salt-call state.sls host

Verify that the IP addresses in /etc/network/interfaces match those outlined in settings.ini

sudo reboot

Log in to the server as VIRL, Run the remaining steps as 'virl'

python /usr/local/bin/vinstall all

The following command will download the VM images and register them. This can be lengthy

sudo salt-call state.sls images

sudo reboot