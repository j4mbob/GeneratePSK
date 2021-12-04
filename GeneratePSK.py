#!/usr/bin/env python3

try:
    import argparse
    import sys
    import hashlib
    import binascii

except ImportError:
    print('error importing modules')
    print('please install argparse sys hashlib binascii via pip3 install')
    exit(1)

class GeneratePSK():
#calculates a WPA PSK based on the passphrase and the SSID 

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Generate WPA PSK",conflict_handler='resolve')
        parser.add_argument('ssid', help='<ssid>')
        parser.add_argument('passphrase', help='<passphrase>')
        parser.add_argument('--silent', action='store_true', required=False, help='Just output calculated PSK')
        parseargs = vars(parser.parse_args(None if sys.argv[1:] else ['-h']))

        if parseargs['silent']:
            self.silent = True

        return parseargs['ssid'],parseargs['passphrase']

    def generate(self,ssid,passphrase):
        dk = hashlib.pbkdf2_hmac('sha1', str.encode(passphrase), str.encode(ssid), 4096, 32)

        if hasattr(self, 'silent'):
            print('0x00' + binascii.hexlify(dk).decode("UTF-8"))    
        else:
            print('SSID:' + ' ' + ssid)
            print('PASSPHRASE:' + ' ' + passphrase)
            print('CALCULATED PSK:' + ' ' + '0x00' + binascii.hexlify(dk).decode("UTF-8"))

if __name__ == "__main__":
    g = GeneratePSK()
    ssid,passphrase = g.parse_args()

    g.generate(str(ssid),str(passphrase))

