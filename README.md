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

apt-get install -y openssh-server git

reboot

On reboot, login as virl. Enter the following commands

git clone https://github.com/Snergster/virl-bootstrap.git

cd virl-bootstrap

If you have gotten preseed keys please put them both into the preseed_keys directory

sudo -s

./virl-bootstrap.py

###cp ./vsettings.ini /home/virl/settings.ini

###Edit /home/virl/settings.ini as required

###sudo -s

###cd virl-bootstrap

###Edit extra.conf for your correct id and salt server

###cp extra.conf /etc/salt/minion.d

###service salt-minion restart

After steps 1-7

Get your salt key accepted on server.  Skip if preseed was done.

Execute step 8 until that the result is 'True'

###salt-call state.sls zero

exit

cd /home/virl

cp vsettings.ini settings.ini

Edit /home/virl/settings.ini as required,  Ensure changes made in bootstrap are reflected in settings.ini

####python ./vinstall.py salt

vinstall salt

vinstall first

Verify that the IP addresses in /etc/network/interfaces match those outlined in settings.ini

sudo reboot

Log in to the server as VIRL, Run the remaining steps as 'virl'

###python /usr/local/bin/vinstall all

vinstall all

The following command will download the VM images and register them. This can be lengthy

sudo salt-call state.sls router-vms

sudo reboot