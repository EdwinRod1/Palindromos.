def palindromo2(st):

    n = len(st)

    i = 0

    j = n - 1

    while i < n // 2:

        if st[i] != st[j]:

            return False

        i += 1

        j -= 1

    return True

palabra = input("Escribe una palabra: ")

print(palindromo2(palabra))
