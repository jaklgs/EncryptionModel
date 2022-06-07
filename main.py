# Apply encryption algorithms through the command line

import argparse
from encryption_models import Rsa, Key

# top level parser
parser = argparse.ArgumentParser(prog='ENCRYPT')
subparser = parser.add_subparsers(help='subcommand to choose encryption type', dest="subcommand")

# RSA parser
parser_rsa = subparser.add_parser('rsa', help='The RSA algorithm')
parser_rsa.add_argument('-m', '--message', type=int, help='Message that is being encoded/decoded')

group_rsa = parser_rsa.add_mutually_exclusive_group()
group_rsa.add_argument('-e', '--encode', action='store_true', help='Encode the message')
group_rsa.add_argument('-d', '--decode', action='store_false', help='Decode the message')

parser_rsa.add_argument('-p1', '--prime1', type=int, required=False, help='The first secret prime number')
parser_rsa.add_argument('-p2', '--prime2', type=int, required=False, help='The second secret prime number')
parser_rsa.add_argument('-c', '--coprime', type=int, required=True, help='Relative prime')
parser_rsa.add_argument('-p', '--product', type=int, required=False, help='Product of two secret primes')

rsa_args = parser_rsa.parse_args()

if __name__ == "__main__":
    if rsa_args.encode:
        print(Rsa.encode(rsa_args.message, Key(0, 0, rsa_args.coprime, rsa_args.product)))
    else:
        print(Rsa.decode(rsa_args.message, Key(rsa_args.prime1, rsa_args.prime2,
                                               rsa_args.coprime, rsa_args.prime1 * rsa_args.prime2)))
