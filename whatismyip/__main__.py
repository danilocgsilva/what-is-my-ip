from whatismyip.Wimi import Wimi
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ipv6",
        "-6",
        action='store_true',
        help="Asks for ipv6 address"
    )
    args = parser.parse_args()

    if args.ipv6:
        iptype = 'ipv6'
    else:
        iptype = 'ipv4'


    print(
        Wimi().get_ip(iptype)
    )