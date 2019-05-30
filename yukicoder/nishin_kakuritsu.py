
kakuritsu = 100
for i in range(1, 12 * 10):
    kakuritsu = kakuritsu / 4 * 3
    year = i // 12 + 1
    month = i % 12
    print(str(year) + "年" + str(month) + "ヵ月 " + str(round(kakuritsu, 2)) + "%")
