##DONE##
def quarter_of(month):
    for i in range(1, 5):
        if month>3*(i-1) and month<=3*i:
            return i

print(quarter_of(8))