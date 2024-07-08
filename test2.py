soDien = int(input())

if 0 <= soDien <= 50:
    giaTien = 1678 * soDien
elif 51 <= soDien <= 100:
    giaTien = 1678 * 50 + 1734 * (soDien - 50)
elif 101 <= soDien <= 200:
    giaTien = 1678 * 50 + 1734 * 50 + 2014 * (soDien - 100)
elif 201 <= soDien <= 300:
    giaTien = 1678 * 50 + 1734 * 50 + 2014 * 100 + 2536 * (soDien - 200)
elif 301 <= soDien <= 400:
    giaTien = 1678 * 50 + 1734 * 50 + 2014 * 100 + 2536 * 100 + 2834 * (soDien - 300)
else:
    giaTien = 1678 * 50 + 1734 * 50 + 2014 * 100 + 2536 * 100 + 2834 * 200 + 2927 * (soDien - 400)

print(giaTien) 