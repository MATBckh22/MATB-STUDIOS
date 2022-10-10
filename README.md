# Building Blocks

## Binary Numbers

### Data Representation

- electronic swtiches - gates
- each switch holds on of two states
    - 1
    - 0
- a bit represents a binary state

### Binary Numbering System

This process includes both external and internal representation.

A single unit of data is called a bit, which holds the value of 1 or 0. Collection of bits represent larger pieces of data. **Eight bits are grouped to be a byte, which is the amount of memory needed to store one alphabetic character.**

- one byte: 256 different symbols or characters.

### Binary Code Calculations

- decimal to binary

```python
def to_binary(n):
    sum = 0
    counter = 0
    for i in str(n)[::-1]:
        sum = sum + int(i)*2**counter
        counter += 1
    print(sum)
    return sum
    
to_binary(101011)
```

- binary to decimal

```python=
def to_decimal(x):
    binary = ''
    while x != 0:
        if x%2 != 0:
            x = (x-1)/2
            binary = binary + '1'
        else:
            x = x/2
            binary = binary + '0'
    print(binary[::-1])
    return binary[::-1]
```

## Digital vs Analog

### Digital

- values for a given object are drawn from a finite set, such as letters or a subset of integers.

### Analog

- continuous sinusoidal waveform format

## Binary Representation of Sound and Images

### Sound

- sampling rate
- Bit depth
- MP3

### Images

- scanning
- Raster graphics
- RGB encoding scheme
- True color

## Data Compression

- Compression rate = size (uncompressed data)/size (compressed data)

- Lossless compressions schemes
    - no information is lost
    - possible to exactly reproduce original data
    
- Lossy compressions schemes
    - possiblity that not all of the information in the original data is complete

## Reliability of Binary Representation

- building a base-10: decimal computer
- Bistable environment

### Binary Storage Devices

- magnetic cores
    - used in 1955-1975 to construct computer memories
- core
    - states used to represent 0 and 1 are based on the **direction** of the magnetic field of the core

- transistor
    - solid-state device has no mechanical or moving parts
    - constructed from semiconductors
    - can be printed on integrated circuit/chip
    
- circuit board
    - chip mount
    - interconnects different chips
    
- mask 
    - 


