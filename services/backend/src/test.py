def solve_runes(runes: str):
    seps = ('--', '*', '+')
    digits = [i for i in runes.split(sep='=')]
    for i in seps:
        if i in digits[0]:
            for x in digits[0].split(sep=i):
                digits.append(x)
            digits.pop(0)
            break

    def check():
        s = '??'
        for _ in range(5):
            if s in digits:
                return True
            s += '?'
        for i in digits:
            if len(i) > 1 and (i[0] == '?' or i[0:2] == '-?'):
                return True
        return False
    
    for i in range(0, 10):
        if (str(i) in runes) or (i == 0 and check()):
            continue
        new: str = runes.replace('?', str(i))
        expression = list(new.split(sep='='))
        if eval(expression[0]) == int(expression[1]):
            return i
    return -1

print(solve_runes("1+1=?"),         2, "Answer for runes = '1+1=?' ")
print(solve_runes("123*45?=5?088"), 6, "Answer for runes = '123*45?=5?088' ")
print(solve_runes("-5?*-1=5?"),     0, "Answer for runes = '-5?*-1=5?' ")
print(solve_runes("19--45=5?"),    -1, "Answer for runes = '19--45=5?' ")
print(solve_runes("??*??=302?"),    5, "Answer for runes = '??*??=302?' ")
print(solve_runes("?*11=??"),       2, "Answer for runes = '?*11=??' ")
print(solve_runes("??*1=??"),       2, "Answer for runes = '??*1=??' ")
print(solve_runes("?38???+595???=833444"), 2, "Answer for runes = '?38???+595???=833444' ")
print(solve_runes("?*123?45=?"), 0, "Answer for runes = '?*123?45=?' ")