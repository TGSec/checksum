import os.path as path
import hashlib
import argparse

def stringfy_list(list):
    string = ''
    last = len(list) - 1
    for n, item in enumerate(list):
        string = string + item
        if n == last:
            string = string + '.'
        else:
            string = string + ', '
    return string

parser = argparse.ArgumentParser(description='Encrypts a file using a hash algorithm. Cool for chechsums.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='Check license.txt for license terms of usage.\nCreated by: thegamerbr1\nTelegram: @thegamerbr1\nSkype: xthegamerbr1x') #Command-line argument parser

parser.add_argument('algorithm', help='the hash algorithm to be used.')
parser.add_argument('file_path', help='path to the file to be encrypted.')

args = parser.parse_args()

if not path.isfile(args.file_path): #If file doesnt exist
    print('Error: specified file "{}" doesn\'t exist.'.format(args.file_path))
    exit()

available = hashlib.algorithms_available

available_str = ''

if args.algorithm not in available:
    print('Error: specified algorithm not available. Supported algorithms for your platform include: {}'.format(stringfy_list(available)))
    exit()

file = open(args.file_path, 'rb')

hashfunc = hashlib.new(args.algorithm)

hashfunc.update(file.read())

print(hashfunc.hexdigest())