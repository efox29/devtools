# Dev Tools

These are collections of tools that can help with development.

## pycrc32.py

Calculates the crc32 of a file. Most linux systems have built in crc32 check but this allows some level or portability across systems. 

### Usage
`python pycrc32.py filename`

where `filename` is the file you want to calc the crc32 of.


## bitpos.py
**Requires** Python3

Converts decimal and hex to binary with each bit identified.

### Usage

For the most effective use, add this folder to your PATH so that the tools but altneratively, you can use python3 to call it or execute the script directly with ./bitpos.py

`python3 bitpos.py -d 1234`

Output:
```
            Bit Position            
10 9  8   7  6  5  4   3  2  1  0   
------------------------------------
1  0  0   1  1  0  1   0  0  1  0   
```

`./bitpos.py -x deadbeef`

Output:
```
                                              Bit Position                                              
31 30 29 28  27 26 25 24  23 22 21 20  19 18 17 16  15 14 13 12  11 10 9  8   7  6  5  4   3  2  1  0   
--------------------------------------------------------------------------------------------------------
1  1  0  1   1  1  1  0   1  0  1  0   1  1  0  1   1  0  1  1   1  1  1  0   1  1  1  0   1  1  1  1   
```

`./bitpos.py -x 0x1234`

Output:
```
               Bit Position                
12  11 10 9  8   7  6  5  4   3  2  1  0   
-------------------------------------------
1   0  0  1  0   0  0  1  1   0  1  0  0   
```

