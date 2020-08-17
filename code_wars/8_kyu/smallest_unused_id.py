##DONE##
def next_id(arr):
    c = 0
    while True:
        if not c in arr:
            return c
        c+=1
