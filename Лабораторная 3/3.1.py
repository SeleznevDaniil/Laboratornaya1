def poisk(spisok=input().split(), tovar=input()):
    if tovar in spisok:
        index = spisok.index(tovar)
        return index
    else:
        return None
print(poisk())