print("program perhitungan NDP-NNP")
GDP = float(input('masukkan nilai GDP : '))
GNP = float(input('masukkan nilai GNP : '))
depreciation = float(input('masukkan nilai depresiasi : '))
sales_tax = float(input('masukkan pajak penjualan : '))
earnings = float(input('masukkan pendapatan : '))
personal_income_tax = float(input('masukkan personal income tax : '))

NDP = GDP - depreciation
print("NDP : ", NDP)
NNP = GNP - depreciation
print("NNP : ", NNP)
national_income = NNP - sales_tax
print('national income : ', national_income)
personal_income = national_income - earnings
print('personal income : ', personal_income)
disposable_personal_income = personal_income - personal_income_tax
print('disposable personal income : ', disposable_personal_income)
