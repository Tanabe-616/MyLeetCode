def reverse(self, x: int) -> int:
    x = str(x)       
    x = list(x)
    y = ""
    if x[0] == '-':
        y += x[0]
    x.reverse()
    for i in x:
        if i == '-':
            break
        y += i
    y = int(y)
    if y > 2**(31) - 1:
        return 0
    if y < -2**31:
        return 0
    return y

x = 321
p = reverse(x)
print(p)