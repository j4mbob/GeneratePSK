#!/usr/bin/env python3

try:
    import argparse
    import sys
    import hashlib
    import binascii

except ImportError:
	print('error importing modules')
	exit(1)

class GeneratePSK():
    #calculates a WPA PSK based on the passphrase and the SSID 

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Generate WPA PSK",conflict_handler='resolve')
        parser.add_argument('ssid', help='<ssid>')
        parser.add_argument('passphrase', help='<passphrase>')
        parseargs = vars(parser.parse_args(None if sys.argv[1:] else ['-h']))

        return parseargs['ssid'],parseargs['passphrase']

    def generate(self,ssid,passphrase):
        print('SSID:' + ' ' + ssid)
        print('PASSPHRASE:' + ' ' + passphrase)
        dk = hashlib.pbkdf2_hmac('sha1', str.encode(passphrase), str.encode(ssid), 4096, 32)
        print('CALCULATED PSK:' + ' ' + binascii.hexlify(dk).decode("UTF-8"))

if __name__ == "__main__":
    g = GeneratePSK()
    ssid,passphrase = g.parse_args()

    g.generate(str(ssid),str(passphrase))

