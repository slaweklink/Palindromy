print("Podaj przykład zdania do sprawdzenia: ")
zdanie = input()

zdanie = zdanie.split()
zdanie = "".join(zdanie)

zdanie_nawspak = zdanie[::-1]

if zdanie == zdanie_nawspak:
    print("Jest to palindrom")
else:
    print("Nie jest to palindrom")
