loanAmount = int(input("Enter the loan amount: "))
Number_of_years = int(input("Enter the number of years: "))
print(
    format("Interest Rate", "15s"),
    format("Monthly Payment", "18s"),
    format("Total Payment", "15s"),
)

for rate in range(40, 85):
    rate = rate / 8

    monthRate = rate / 1200  # * Переводим годовой процент в ежемесячный

    monthPayment = (
        loanAmount * monthRate / (1 - (1 + monthRate) ** (-Number_of_years * 12))
    )

    totalPayment = monthPayment * Number_of_years * 12

    print(
        format(rate, "7.3f"),
        format(monthPayment, "15.2f"),
        format(totalPayment, "21.2f"),
    )
