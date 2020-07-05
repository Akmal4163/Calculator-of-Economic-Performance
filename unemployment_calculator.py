print("UNEMPLOYED MEASURING PROGRAMS")

number_of_employed = float(input("masukkan jumlah yang dipekerjakan : "))
number_of_unemployed = float(input("masukkan jumlah penganggur : "))
adult_population = float(input('masukkan adult population: '))
labor_force = number_of_employed + number_of_unemployed
print('jumlah tenaga kerja : ', labor_force)
unemployment_rate = (number_of_unemployed / labor_force) * 100
print("tingkat pengangguran :", unemployment_rate)
labor_force_participation_rate = (labor_force/adult_population)*100
print("tingkat partisipasi angkatan kerja : ",labor_force_participation_rate)