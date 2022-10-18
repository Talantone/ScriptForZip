#!/usr/bin/python3
import tarfile
import os
from datetime import date


def log_packer(directory='var/log'):
    filename = '{}/{}.tar.gz'.format(directory, str(date.today()))
    tar = tarfile.open(filename, 'w')
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            tar.add('{}/{}'.format(directory, file))
            os.remove('{}/{}'.format(directory, file))
    tar.close()


def main():
    log_packer()


if __name__ == '__main__':
    main()
