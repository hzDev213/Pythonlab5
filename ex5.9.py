payPerYear = 10000
payPrecentPerYear = 0.05
year = 0
payPerFourYear = 0
while year < 10:
    year += 1
    payPerYear *= 1 + payPrecentPerYear
    print("year", year, round(payPerYear, 2), "$")

payPerTenYear = payPerYear * (1 + payPrecentPerYear)
for i in range(1, 5):
    payPerFourYear += payPerTenYear * (1 + payPrecentPerYear)

print("Cost of 4 years", round(payPerFourYear, 2), "$")
