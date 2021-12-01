import zlib
import os
import sys


def crc32(fpath):
    """With for loop and buffer."""
    crc = 0
    with open(fpath, 'rb', 65536) as ins:
        for x in range(int((os.stat(fpath).st_size / 65536)) + 1):
            crc = zlib.crc32(ins.read(65536), crc)
    return '%08x' % (crc & 0xFFFFFFFF)
try:
    file = sys.argv[1]
except:
    print("error: Need to provide a file to CRC")
    exit()


crc = crc32(file)

print(f'crc:\n{crc}')