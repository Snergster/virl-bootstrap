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

You are now presented with a menu. Proceed through the steps sequentially.

NOTE - if you abort the menu sequence and restart, you MUST re-enter the information into the menu fields once more.

Step 1 - Change salt master from salt-master.cisco.com 

- You may have received instructions to use a specific 'salt master', if so, enter the salt master hostname here. If you enter this step, you MUST enter a value. The fields must NOT be blank!

Step 2 - Change salt id from virl or salt domain from virl.info

- You may have received instructions to use a specific 'salt id' and 'salt domain', if so, enter the provided values here. If you enter this step, you MUST enter a value. The fields must NOT be blank!

Step 3 - Change hostname or domain name

- Set the hostname and domain name for your server here, for example, virl-1.mynet.com. If you enter this step, you MUST enter a value. The fields must NOT be blank!

Step 4 - Write out extra.conf

- MUST perform this step even if you have not made any changes in steps 1-3

Step 5 - Change http proxy

- If you are behind a proxy, please set this here

Step 6 - install salt without preseed keys

- If you have NOT been provided with a 'preseed' key, select 6, otherwise skip to Step 7

Step 7 - install salt with preseed keys in /home/virl/virl-bootstrap/preseed_keys

- If you have been provided with a 'preseed' key set and have please the keys in the preseed_keys directory, the select 7.

After steps 6 or 7, software will be installed and configured. You must see the following message returned before proceeding to Step 8:

salt-minion start/running, process ####
 *  INFO: Running daemons_running()
 *  INFO: Salt installed!

Step 8 - Test if you are connected to salt-master

- Ensure that you received a return value 'True' before trying to proceed. If you do not, you need to contact your administrator to confirm that you have the correct key and the key has been accepted.

Step 9 - Install virl installer and settings

- Ensure that the step completed and reports no 'Failed' values

Step 10 - Edit settings.ini

- Modify the content of the settings.ini to meet you needs. The hostname and domain name values will already contain the values you entered in Step 3. HTTP proxy will contain the values entered in Step 5. Main areas to check are as follows:

-- using dhcp on the public port?
-- Static IP, public_network, public_netmask, public_gateway
-- ntp_server
-- first nameserver 
-- second nameserver
-- l2_network (CIDR format),l2_mask, l2_network_gateway, l2_start_address, l2_end_address, l2_address (address/netmask)
-- l2_network2 (CIDR format), l2_mask2, l2_network_gateway2, l2_start_address2, l2_end_address2, l2_address2 (address/netmask)
-- l3_network (CIDR format), l3_mask, l3 network gateway, l3_floating_start_address, l3_floating_end_address, l3_address (address/netmask)
-- ramdisk
-- location region
-- guest account
-- desktop

NOTE - ensure that you have reachability to your ntp server. If you are using DHCP, you do not need to alter the 'first nameserver' and 'second nameserver' fields. If you are using static IP addressing, ensure that you have reachability to your nameservers.

- Save your settings.ini changes (CTRL^O) and exit (CTRL^X)

NOTE - if you abort the menu sequence and restart, you MUST re-enter the information into the menu fields (Steps 1 to 5) once more.

Step 11 - Exit

- Software will now be configured

NOTE - if you abort the menu sequence and restart, you MUST re-enter the information into the menu fields (Steps 1 to 5) once more.

Verify that the IP addresses in /etc/network/interfaces match those outlined in settings.ini

sudo reboot

Log in to the server as VIRL, Run the remaining steps as 'virl'

vinstall all

The following command will download the VM images and register them. This can be lengthy

sudo salt-call state.sls router-vms

Complete the installation by rebooting the system.

sudo reboot

On reboot, log in as 'virl' and issue the command:

virl_health_status

Ensure that the following lines are present in the output:

RabbitMQ status:
[{pid,####},

OpenStack identity service for STD is available
OpenStack image service for STD is available
OpenStack compute service for STD is available
OpenStack network service for STD is available

OpenStack services: (ALL SERVICES REPORT 'ENABLED' 'UP'):

nova-consoleauth
nova-scheduler
nova-conductor
nova-cert
nova-compute

STD server on url http://localhost:##### is listening, server version x.x.x.x
UWM server on url http://localhost:##### is listening, server version x.x.x.x

{u'autonetkit-cisco-version': u'VIRL Configuration Engine #.#.#',
 u'autonetkit-version': u'autonetkit #.#.#',