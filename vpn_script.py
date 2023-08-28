import os, argparse, random
import subprocess

flags = argparse.ArgumentParser()

#-u USERNAME -p PASSWORD -s SIZE
flags.add_argument("-u", "--username", help="Username")
flags.add_argument("-p", "--password", help="Password")
flags.add_argument("-s", "--size", help="Size", type=int)
args = flags.parse_args()
dict = vars(args)

#gen VPN_IPSEC_PSK=
rand = subprocess.getoutput('openssl rand -base64 ' + str(dict['size'])) 
print(rand)

#run docker command
env =('--env \"VPN_USER=' + str(dict['username'])+ '\"'+ ' --env \"VPN_PASSWORD=' + str(dict['password'])+ '\"' + ' --env \"VPN_IPSEC_PSK=' + str(rand) + '\"') 
print(env)
print('''docker run --name ipsec-vpn-server \
        '''+ env +''' \
        --env-file ~/workspace/docker/vpn/env \
        --restart=always \
        -p 500:500/udp \
        -p 4500:4500/udp \
        -v /lib/modules:/lib/modules:ro \
        -d --privileged \
        hwdsl2/ipsec-vpn-server  ''')