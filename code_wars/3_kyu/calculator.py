class Calculator(object):
  def evaluate(self, string):
    exp = string.split()
    while '/' in exp or '*' in exp or '+' in exp or '-' in exp:
        for i, c in enumerate(exp):
            if c=='/':
                exp[i-1] = int(exp.pop(i-1)) / int(exp.pop(i))
                break
            elif c=='*':
                exp[i-1] = int(exp.pop(i-1)) * int(exp.pop(i))
                break
        if not '/' in exp or '*' in exp:
            for i, c in enumerate(exp):
                if c=='+':
                    exp[i-1] = int(exp.pop(i-1)) + int(exp.pop(i))
                    break
                elif c=='-':
                    exp[i-1] = int(exp.pop(i-1)) - int(exp.pop(i))
                    break
    return int(exp[0])

print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
"2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"
"2 + 12 / 3 - 6 / 3 * 3 + 8"
"2 + 4 - 6 + 8"
