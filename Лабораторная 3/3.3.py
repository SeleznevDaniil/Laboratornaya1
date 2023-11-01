def count_letters(text=input().casefold()):
    slovar = {}
    for letter in text:
        if letter not in slovar:
            slovar[letter] = 0
        slovar[letter] += 1
    return slovar
print(count_letters())
def calculate_frequency(priem = dict(input())):
    summa = sum(priem.values())
    slovar_2 = {}
    for x in priem:
        slovar_2[x] = priem[x]/summa
    return slovar_2
print(calculate_frequency())