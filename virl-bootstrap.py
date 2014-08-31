#!/usr/bin/python
__author__ = 'ejk'

import subprocess
from os import path

salt_master = 'salt-master.cisco.com'
salt_name = 'virl'
salt_append_domain = 'virl.info'
while_exit = 0
cwd = path.realpath('./')

while not while_exit:
    print (30 * '-')
    print ("   V I R L - I N S T A L L - M E N U")
    print (30 * '-')
    print ("1. Change salt master from {0} ".format(salt_master))
    print ("2. Change salt id from {0} ".format(salt_name))
    print ("3. Change salt domain from {0} ".format(salt_append_domain))
    print ("4. Write out extra.conf")
    print ("5. install salt without preseed keys")
    print ("6. install salt with preseed keys in {0}".format(cwd + 'preseed_keys'))
    print ("7. Exit")
    print (30 * '-')

    choice = raw_input('Which step are you on [1-7] : ')

    choice = int(choice)

    if choice == 1:
        salt_master = raw_input('Salt master [%s] ' % salt_master)
    if choice == 2:
        salt_name = raw_input('Salt name [%s] ' % salt_name)
    if choice == 3:
        salt_append_domain = raw_input('Salt domain name [%s] ' % salt_append_domain)
    if choice == 4:
        if not path.exists('/etc/salt/minion.d'):
            subprocess.check_output(['mkdir', '-p', '/etc/salt/minion.d'])
        with open(("/etc/salt/minion.d/extra.conf"), "w") as extra:
            extra.write("""master: {salt_master}\n""".format(salt_master=salt_master))
            extra.write("""id: {salt_name}\n""".format(salt_name=salt_name))
            extra.write("""append_domain: {salt_append_domain}\n""".format(salt_append_domain=salt_append_domain))

    if choice == 5:
        subprocess.call(['sh', '/home/virl/virl-bootstrap/install_salt.sh'])
    if choice == 6:
        subprocess.call(['sh', '/home/virl/virl-bootstrap/install_salt.sh', '-k', (cwd + 'preseed_keys')])
    if choice == 7:
        while_exit = 1

