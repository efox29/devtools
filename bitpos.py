#!/usr/bin/env python3
import sys
import getopt

def find_bits(number):
    # how many bits are there
        output = bin(value)
        bit_lenth = len(output)-2  
        # create table spacing
        header = ""
        row_data = ""
        for x in reversed(range(0,bit_lenth)):
            if x % 4:
                gap_offset = 0
            else:
                gap_offset = 1
            gap = 3 + gap_offset
            header = header+f"{x:<{gap}}"
            row_data = row_data + f"{ bool(value & (1 << x)):<{gap}}"
        
        title = 'Bit Position'
        print(f'decimal:{int(number)}')
        print(f'Hex:{hex(number)}')
        print(f'Binary:{bin(number)}')
        print(f'')
        print(f"{title:^{len(header)}}")
        print(header)
        print(f"-"*len(header))
        print(row_data)


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
        
           
        
