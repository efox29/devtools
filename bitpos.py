#!/usr/bin/env python3
import sys
import getopt

import shutil

def find_bits(number):
    # get terminal size
    termsize = shutil.get_terminal_size()
    max_width = termsize.columns
    bits_per_line = max_width // 4  # assuming each bit occupies about 4 characters
    # how many bits are there
    output = bin(number)
    bit_length = len(output) - 2
    # split into chunks for each line
    chunks = [bit_length - i * bits_per_line for i in range(bit_length // bits_per_line, -1, -1)]
    for chunk_start in chunks:
        # create table spacing
        header = ""
        row_data = ""
        for x in reversed(range(max(0, chunk_start - bits_per_line), chunk_start)):
            if x % 4 == 0:
                gap_offset = 1
            else:
                gap_offset = 0
            gap = 4 + gap_offset
            header += f"{x:>{gap}}" if x < 10 else f"{x:>{gap-1}}"
            row_data += f"{bool(value & (1 << x)):>{gap}}" if x < 10 else f"{bool(value & (1 << x)):>{gap-1}}"

        title = 'Bit Position'
        print(f'decimal:{int(number)}')
        print(f'Hex:{hex(number)}')
        print(f'Binary:{bin(number)}')
        print(f'')
        print(f"{title:^{len(header)}}")
        print(header)
        print(f"-" * len(header))
        print(row_data)
        print()




try:
    opts, args = getopt.getopt(sys.argv[1:],"hx:b:d:")
except getopt.GetoptError:
    print("No")
    sys.exit(2)

for opt, arg in opts:    
    if opt[0] == "-h":
        print("python bit_tools -number_format number")
        sys.exit()
    elif opt == "-x":               
        value = int(arg,16)          
        find_bits(value)  
    elif opt =='-d':
        value = int(arg,10)           
        find_bits(value)
        
           
        
