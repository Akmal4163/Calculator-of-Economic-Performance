print("PROGRAM PENGHITUNGAN DEFLATOR PDB")
PDB_Nominal = float(input('masukkan nilai PDB nominal : '))
PDB_Riil = float(input('masukkan nilai PDB riil : '))

deflator_PDB = (PDB_Nominal / PDB_Riil) * 100
print('deflator PDB : ', deflator_PDB)
