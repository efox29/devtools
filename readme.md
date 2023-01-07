# Dev Tools

These are collections of tools that can help with development.

## pycrc32.py

Calculates the crc32 of a file or cli inputs. Most linux systems have built in crc32 check but this allows some level or portability across systems 

### Usage
```
python pycrc32.py -f FILENAME_PATH
```

where `FILENAME_PATH` is the file you want to calc the crc32 of.

example: `python pycrc32.py -f ../firmware/myapp.bin`

```
python pycrc32.py -d DECIMAL_NUMBER
```
where `DECIMAL_NUMBER` is any decimal number

example: `python pycrc32.py -d 12345678`

```
python pycrc32.py -s "STRING"
```
where `STRING` is any string.

example: `python pycrc32.py -s "hello world!"`

```
python pycrc32.py -x HEX
```
where `HEX` is any hex starting with `0x`

example: `python pycrc32.py -x 0xdeadbeef`

### NOTE: The following non file arguments were tested with https://emn178.github.io/online-tools/crc32.html

The file input was tested using unix crc32.



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


## epoch.sh
Converts linux epoch time to a date.

### Usage
`epoch.sh 1645002299`

Output:
```
Wed Feb 16 04:04:59 EST 2022
```

## mouse.py
Movies the mouse 1 pixel to the left and right and clicks. Keeps the computer from going idle.

