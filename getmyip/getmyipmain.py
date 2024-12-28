copyright='gunville 2024'
import argparse

from getmyip import getMyIP

version=f'getmyip {copyright} v1'


def parse_args():
    """ process command line arguments """

    parser = argparse.ArgumentParser(
        description='Report external IP address',
        epilog=version,
        allow_abbrev=False
    )

    parser.add_argument(
        '-v', '--version', 
        action='version', 
        version=version
    )

    parser.add_argument(
        '-4', '--ipv4', 
        help='Find public IPv4 address (default)', 
        action='store_true',
        default=False
    )

    parser.add_argument(
        '-6', '--ipv6',
        help='Find public IPv6 address',
        action='store_true',
        default=False
    )

    args = parser.parse_args()

    return args


def getmyip():
    """ discover public IP and update cloudflare record """

    args = parse_args()
    
    if args.ipv4 or not args.ipv6:
        print(getMyIP(ipv6=False))
    if args.ipv6:
        print(getMyIP(ipv6=True))


if __name__ == "__main__":
    getmyip()


