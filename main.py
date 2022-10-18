#!/usr/bin/python3
import tarfile
import os
from datetime import date


def log_packer(directory='var/log'):
    filename = '{}/{}.tar.gz'.format(directory, str(date.today()))
    tar = tarfile.open(filename, 'w')
    for file in os.listdir(directory):
        if file.endswith('.log'):           #rename this if you need it(or delete this if you want to pack all files)
            tar.add('{}/{}'.format(directory, file))
            os.remove('{}/{}'.format(directory, file))
    tar.close()


def main():
    log_packer()                           #add argument here if you need to use other directory


if __name__ == '__main__':
    main()
