import zlib
import os
import sys
import argparse

"""code taken from stackoverflow"""
def crc32(fpath):
    """With for loop and buffer."""
    crc = 0
    with open(fpath, 'rb', 65536) as ins:
        """we find out how many 65k chunks we need"""
        for x in range(int((os.stat(fpath).st_size / 65536)) + 1):
            """get the crc for that chunk and pass in the previous crc"""
            crc = zlib.crc32(ins.read(65536), crc)
    crc = '%08x' % (crc & 0xFFFFFFFF)
    print(crc)
    # return '%08x' % (crc & 0xFFFFFFFF) # this masks out the any additional bits


def crc32_string(val):
    crc = 0
    crc = zlib.crc32(val,crc)
    print('%08x' % (crc & 0xFFFFFFFF))

def int_to_bytes(number: int) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

parser = argparse.ArgumentParser(description="finds the crc32 of a file or input string")
parser.add_argument('-f','--file',type=str,help='file to apply crc32')
parser.add_argument('-s','--string',type=str,help='hex string')
parser.add_argument('-d', '--decimal',type=int,help="hello ")
parser.add_argument('-x','--hex', type=lambda x: int(x,0),help="sdfsd")
args = parser.parse_args()

if args.string is not None:
    input_bytes = bytes(args.string,'ascii')
elif args.decimal is not None:
    input_bytes = int_to_bytes(args.decimal)
elif args.hex is not None:
    input_bytes = int_to_bytes(args.hex)
elif args.file is not None:
    crc32(args.file)
    exit()

crc32_string(input_bytes)

