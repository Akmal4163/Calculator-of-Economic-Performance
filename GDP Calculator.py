print("=========GDP CALCULATOR==========")
# input data
C = float(input("Masukkan Nilai Konsumsi : "))
I = float(input("masukkan nilai investasi : "))
G = float(input("masukkan nilai belanja pemerintah : "))
X = float(input("masukkan nilai ekspor : "))
M = float(input("masukkan nilai import : "))
GDP = float(input("masukkan nilai GDP : "))
# penyelesaian data
choices = str(input("Masukkan Rumus yang dikerjakan : "))
if choices == "GDP":
    GDP = C + I + G + (X - M)
    print("The GDP is : ",GDP)
elif choices == "konsumsi":
    C = GDP - I + G + (X - M)
    print("Nilai konsumsi adalah :",C)
elif choices == "Investasi" :
    I = GDP - C + G + (X - M)
    print("Nilai investasi adalah :", I)
elif choices == "belanja pemerintah" :
    G = GDP - C + I + (X - M)
    print("Nilai belanja pemerintah adalah :", G)
elif choices == "ekspor":
    X = GDP - C + I + M
    print("Nilai ekspor adalah :", X)
elif choices == "impor":
    M = GDP - C + I + X
    print("Nilai impor adalah :", M)
else :
    print("sorry, we dont have this keywords")