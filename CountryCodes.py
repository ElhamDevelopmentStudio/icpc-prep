test_case = int(input())

x = []

for _ in range(test_case):

    countriesList = 0
    countries = input().strip()
    for i in range(0, len(countries), 2):
        t = countries[i:i+2]
        countriesList += 1

    x.append(countriesList)

for _ in x:
    print(_)
    