def rgb(r, g, b):
    Hex = ""
    Hexdecimal_alphabets = "ABCDEFG"
    Hex1 = int(r/16)
    Hex3 = int(g/16)
    Hex5 = int(b/16)
    Hex2 = int(r%16)
    Hex4 = int(g%16)
    Hex6 = int(b%16)
    Hex_converted1 = ""
    Hex_converted2 = ""
    Hex_converted3 = ""
    Hex_converted4 = ""
    Hex_converted5 = ""
    Hex_converted6 = ""
    if Hex1 >= 10 and Hex1 <= 255:
        hexdecimal1 = Hex1 - 10
        Hex_converted1 = Hexdecimal_alphabets[hexdecimal1]
        Hex = Hex + Hex_converted1
    elif Hex1 < 0:
        Hex1 = 0
        Hex = Hex + str(Hex1)
    elif Hex1 > 255:
        Hex1 = 255
        Hex = Hex + str(Hex1)
    else:
        Hex = Hex + str(Hex1)
    if Hex2 >= 10 and Hex2 <= 255:
        hexdecimal2 = Hex2- 10
        Hex_converted2 = Hexdecimal_alphabets[hexdecimal2]
        Hex = Hex + Hex_converted2
    elif Hex2 < 0:
        Hex2 = 0
        Hex = Hex + str(Hex2)
    elif Hex2 > 255:
        Hex2 = 255
        Hex = Hex + str(Hex2)
    else:
        Hex = Hex + str(Hex2)
    if Hex3 >= 10 and Hex3 <= 255:
        hexdecimal3 = Hex3 - 10
        Hex_converted3 = Hexdecimal_alphabets[hexdecimal3]
        Hex = Hex + Hex_converted3
    elif Hex3 < 0:
        Hex3 = 0
        Hex = Hex + str(Hex3)
    elif Hex3 > 255:
        Hex3 = 255
        Hex = Hex + str(Hex3)
    else:
        Hex = Hex + str(Hex3)
    if Hex4 >= 10 and Hex4 <= 255:
        hexdecimal4 = Hex4 - 10
        Hex_converted4 = Hexdecimal_alphabets[hexdecimal4]
        Hex = Hex + Hex_converted4
    elif Hex4 < 0:
        Hex4 = 0
        Hex = Hex + str(Hex4)
    elif Hex4 > 255:
        Hex4 = 255
        Hex = Hex + str(Hex4)
    else:
        Hex = Hex + str(Hex4)
    if Hex5 >= 10 and Hex5 <= 255:
        hexdecimal5 = Hex5 - 10
        Hex_converted5 = Hexdecimal_alphabets[hexdecimal5]
        Hex = Hex + Hex_converted5
    elif Hex5 < 0:
        Hex5 = 0
        Hex = Hex + str(Hex5)
    elif Hex5 > 255:
        Hex5 = 255
        Hex = Hex + str(Hex5)
    else:
        Hex = Hex + str(Hex5)
    if Hex6 >= 10 and Hex6 <= 255:
        hexdecimal6 = Hex6 - 10
        Hex_converted6 = Hexdecimal_alphabets[hexdecimal6]
        Hex = Hex + Hex_converted6
    elif Hex6 < 0:
        Hex6 = 0
        Hex = Hex + str(Hex6)
    elif Hex6 > 255:
        Hex6 = 255
        Hex = Hex + str(Hex6)
    else:
        Hex = Hex + str(Hex6)
    return Hex

rgb(200,15,0)