#!/usr/bin/python
__author__ = 'ejk'

import subprocess
from os import path
from time import sleep

salt_master = 'salt-master.cisco.com'
salt_name = 'virl'
salt_append_domain = 'virl.info'
while_exit = 0
cwd = path.realpath('./')
proxy = 'None'
hostname = 'virl'
domain = 'virl.info'

while not while_exit:
    print (30 * '-')
    print ("   V I R L - I N S T A L L - M E N U")
    print (30 * '-')
    print ("1. Change salt master from {0} ".format(salt_master))
    print ("2. Change salt id from {0} or salt domain from {1}".format(salt_name, salt_append_domain))
    print ("3. Change hostname from {0} or domain name {1}".format(hostname, domain))
    print ("4. Write out extra.conf")
    print ("5. Change http proxy from {0}".format(proxy))
    print ("6. install salt without preseed keys")
    print ("7. install salt with preseed keys in {0}".format(cwd + '/preseed_keys'))
    print ("8. Test if you are connected to salt-master")
    print ("9. Install virl installer and settings")
    print ("10. Edit /etc/virl.ini")
    print ("11. Exit")
    print (30 * '-')

    choice = raw_input('Which step are you on [1-11] : ')

    choice = int(choice)

    if choice == 1:
        salt_master = raw_input('Salt master [%s] ' % salt_master) or 'salt-master.cisco.com'
    if choice == 2:
        salt_name = raw_input('Salt name [%s] ' % salt_name) or 'virl'
        salt_append_domain = raw_input('Salt domain name [%s] ' % salt_append_domain) or 'virl.info'
    if choice == 3:
        hostname = raw_input('System hostname [%s] ' % hostname) or 'virl'
        domain = raw_input('System Domain name [%s] ' % domain) or 'virl.info'
    if choice == 4:
        if not path.exists('/etc/salt/virl'):
            subprocess.check_output(['mkdir', '-p', '/etc/salt/virl'])
        if not path.exists('/etc/salt/minion.d'):
            subprocess.check_output(['mkdir', '-p', '/etc/salt/minion.d'])
        with open(("/etc/salt/minion.d/extra.conf"), "w") as extra:
            extra.write("""master: {salt_master}\n""".format(salt_master=salt_master))
            extra.write("""id: {salt_name}\n""".format(salt_name=salt_name))
            extra.write("""append_domain: {salt_append_domain}\n""".format(salt_append_domain=salt_append_domain))
            extra.write("""master_type: failover \n""")
            extra.write("""verify_master_pubkey_sign: True \n""")
            extra.write("""master_shuffle: True \n""")
            extra.write("""master_alive_interval: 180 \n""")
            ##TODO waiting for salt to put this back in
            # extra.write("""grains_dirs:\n""")
            # extra.write("""  - /etc/salt/virl\n""")

    if choice == 5:
        proxy = raw_input('Http proxy [%s] ' % proxy) or 'None'
        if not proxy == 'None':
            if not path.exists('/etc/salt'):
                subprocess.check_output(['mkdir', '-p', '/etc/salt'])
            with open(("/etc/salt/grains"), "w") as grains:
                grains.write("""proxy: True\n""")
                grains.write("""http proxy: {proxy}\n""".format(proxy=proxy))
        else:
            with open(("/etc/salt/grains"), "w") as grains:
                grains.write("""proxy: False\n""")

    if choice == 6:
        subprocess.call(['mkdir', '-p','/etc/salt/pki/minion'])
        subprocess.call(['cp', './master_sign.pub /etc/salt/pki/minion', '-k'])
        subprocess.call(['sh', '/home/virl/virl-bootstrap/install_salt.sh'])
    if choice == 7:
        subprocess.call(['mkdir', '-p','/etc/salt/pki/minion'])
        subprocess.call(['cp', './master_sign.pub /etc/salt/pki/minion', '-k'])
        subprocess.call(['sh', '/home/virl/virl-bootstrap/install_salt.sh', '-k', (cwd + '/preseed_keys')])
    if choice == 8:
        subprocess.call(['salt-call', 'test.ping'])
    if choice == 9:
        subprocess.call(['salt-call', 'state.sls', 'zero'])
    if choice == 10:
        if not path.exists('/etc/virl.ini'):
            subprocess.call(['cp', './vsettings.ini', '/etc/virl.ini'])
        subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'salt_master', salt_master])
        subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'salt_id', salt_name])
        subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'salt_domain', salt_append_domain])
        if not proxy == 'None':
            subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'proxy', 'True'])
            subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'http_proxy', proxy])
        else:
            subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'proxy', 'False'])
        if not hostname == 'virl' or not domain == 'virl.info':
            subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'hostname', hostname ])
            subprocess.call(['crudini', '--set','/etc/virl.ini', 'DEFAULT',
                         'domain', domain])
        subprocess.call(['/usr/bin/nano', '/etc/virl.ini'])

    if choice == 11:
        if path.isfile('/etc/salt/grains'):
            subprocess.call(['rm', '/etc/salt/grains'])
        subprocess.call(['/usr/local/bin/vinstall', 'salt'])
        sleep(5)
        subprocess.call(['/usr/local/bin/vinstall', 'first'])
        while_exit = 1
