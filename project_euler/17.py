def to_letters(n):
    nums = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand'
    }
    s = ""
    if n >= 1000:
        n -= 1000
        s += "one thousand"

    hundreds = 0
    while n >= 100:
        hundreds += 1
        n -= 100
    if hundreds > 0:
        s += f"{nums[hundreds]} hundred"

    if n==10:
        n -= 10
        if s != "":
            s += " and ten"
        else:
            s += "ten"
    tens = 1
    while n>=20:
        tens += 1
        n -= 10
    if tens > 1:
        if s != "":
            s += f" and {nums[tens*10]}"
        else:
            s += f"{nums[tens*10]}"
        n -= 10
    teens = 0
    while n>10 and n<20:
        teens += 1
        n -= 1
    if teens > 0:
        n = 0
        if s != "":
            s += f" and {nums[teens+10]}"
        else:
            s += f"{nums[teens+10]}"

    ones = 0
    while n>0:
        ones += 1
        n -= 1
    if ones > 0:
        if s != "":
            s += f" {nums[ones]}"
        else:
            s += f"{nums[ones]}"
    return(s)

tot = 0

for i in range(1, 1001):
    s = to_letters(i)
    print(s)
    length = len(s) - s.count(" ") - s.count("-")
    tot += length

print(tot)
tot = 0

for i in range(1, 6):
    s = to_letters(i)
    print(s)
    length = len(s) - s.count(" ") - s.count("-")
    tot += length

print(tot)
