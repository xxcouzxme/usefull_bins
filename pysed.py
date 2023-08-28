#!/usr/bin/python3
import glob
from os import fdopen, remove
from tempfile import mkstemp
from shutil import move, copymode
import os.path

path = '/home/nvergizov/nginx_conf.back/'
path_list = glob.glob(path + '*')
start = 0
to_replace = str.strip('ssl_certificate         /etc/nginx/ssl/default.pem;')
to_replace2 = str.strip('ssl_certificate_key     /etc/nginx/ssl/default.pem;')
replacement = str.strip('''ssl_certificate         /etc/letsencrypt/live/testfact2.ru/fullchain.pem;
                ssl_certificate_key     /etc/letsencrypt/live/testfact2.ru/privkey.pem;''')
replacement2 = str.strip('ssl_trusted_certificate /etc/letsencrypt/live/testfact2.ru/chain.pem;')
num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

def replace(file_path, line_was, line_become):
    fd, abs_path = mkstemp()
    with fdopen(fd,'w') as new_file:
        with open(file_path,'r') as old_file:
            for line in old_file:
                new_file.write(line.replace(line_was, line_become))
    copymode(file_path, abs_path)
    remove(file_path)
    move(abs_path, file_path)


while start < num_files:
    item_path = path_list[start]
    replace(str(item_path),to_replace,replacement)
    start += 1

while start < num_files:
    item_path = path_list[start]
    replace(str(item_path),to_replace2,replacement2)
    start += 1