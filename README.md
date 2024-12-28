
## getmyip46 - Get My External IP Address

Retrieve the external ipv4 and/or ipv6 IP address 

## getmyip Command Usage and Options

Install with pip:

```bash
% pip install gitmyip46
```

```bash
% getmyip -h

usage: app.py [-h] [-v] [-4] [-6]

Report external IP address

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -4, --ipv4     Find public IPv4 address (default)
  -6, --ipv6     Find public IPv6 address

getmyip gunville 2024 v1
```

#### Method of IP address detection:

By default `getmyip` automatically detects the public IP address by sending an HTTP request to [ipv4.icanhazip.com](http://ipv4.icanhazip.com) for IPv4. and [ipv4.icanhazip.com](http://ipv6.icanhazip.com) for IPv6.

You can optionally use a different site to autodetect the public ip by setting the environment variable `IPAPIURL` to that URL:
```bash
% IPAPIURL='http://api.ipify.org'
% getmyip
````
You can do the same for IPv6 using the `IPV6APIURL` environment variable.

