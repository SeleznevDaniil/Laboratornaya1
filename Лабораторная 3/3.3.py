def count_letters(text = input()):
    slovar = {}
    for letter in text:
        if letter not in slovar:
            slovar[letter] = 0
        slovar[letter] += 1
    return slovar
print(count_letters())
def calculate_frequency(priem = input()):
    count = 0
    for x in priem:
        if isinstance(priem[x], list):
            count += len(priem[x])
    slovar_2 = {}
    for bukva in priem:
        slovar_2[bukva] = priem.get("bukva")/count
    return slovar_2
print(calculate_frequency())