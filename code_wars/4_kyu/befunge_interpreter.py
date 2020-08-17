def interpret(code):
    output = ""
    stack = []
    for n in list(code):
        if n.isdigit():
            stack.insert(0, int(n))
        elif n == '+':
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a+b)
        elif n == '-':
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, b-a)
        elif n == '*':
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a*b)
        elif n == '/':
            a = stack.pop(0)
            b = stack.pop(0)
            if a==0:
                stack.insert(0, 0)
            else:
                stack.insert(0, int(b/a))
        elif n == '%':
            a = stack.pop(0)
            b = stack.pop(0)
            if a==0:
                stack.insert(0, 0)
            else:
                stack.insert(0, int(b%a))
        elif n == '!':
            v = stack.pop(0)
            if v==0:
                stack.insert(0, 1)
            else:
                stack.insert(0, 0)
        print(stack)
    return output
interpret("74-")
#print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'), '123456789')
