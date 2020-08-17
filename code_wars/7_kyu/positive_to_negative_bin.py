def from_binary(binary):
    dec = 0
    for b in enumerate(binary[::-1]):
        if b[1]:
            dec += 2**b[0]
    return(dec)

def positive_to_negative(binary):
    for i, b in enumerate(binary):
        if b == 1:
            binary[i] = 0
        else:
            binary[i] = 1
    dec = from_binary(binary)
    print(dec)
    return bin(dec-1)

print(positive_to_negative([0, 0, 1, 0]))