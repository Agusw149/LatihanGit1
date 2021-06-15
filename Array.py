print("******************************************************************")
print("PROGRAM STUDI    : ILMU KOMPUTER ")
print("MATA KULIAH      : STRUKTUR DATA ")
print("KELAS            : 15.2A.31      ")
print("TIM KELOMPOK 3                   ")
print("             1. DIMAS RAMADHAN AGUSTINA      (15200384)")
print("             2. AGUS WAHYUDI                 (15200095)")
print("             3. LAKSMONO ADZANI              (15200170)")
print("             4. GHIFARUL AZHAR               (15200234)")
print("******************************************************************")

# By Coddingan Agus Wahyudi
# Array List Matriks
# Jumlah Kolom
kolom= int(input("Masukkan Jumlah Kolom : "))

# Jumlah Baris
baris= int(input("Masukkan Jumlah Baris : "))

# Array Matriks 1
x=[]

# Array Matriks 2
y=[]

# Array Matriks Total
# List * baris dan kolom agar jumlah baris dan kolom di sesuaikan dengan jumlah yang diinput
z=[0]* baris
for i in range (kolom):
    z[i] = [0]* kolom

print("")

# Input ke dalam Matriks X
# Perulangan Bersarang For
# Perulangan Berdasarkan Kolom
for i in range (kolom):
    line=[]
    print("Baris Ke - "+str(i))
    # Perulangan Berdasarkan Baris
    for i in range (baris):
        line.append(int(input("Masukkan Bilangan : ")))
    x.append(line)

# Output Matriks X
for line in x :
    print(line)
print("")


# Input ke dalam Matriks Y
# Perulangan Bersarang For
# Perulangan Berdasarkan Kolom
for i in range (kolom):
    lines=[]
    print("Baris Ke - "+str(i))
    # Perulangan Berdasarkan Baris
    for i in range (baris):
        lines.append(int(input("Masukkan Bilangan : ")))
    y.append(lines)

# Output Matriks Y
for line in y :
    print(lines)
print("")

# Penjumlahan
# Perulangan Kolom Dengan Jumlah Kolom Yang Di Matriks X
for kolomz in range (len(x)):
    # Perulangan Baris Dengan Jumlah Baris Yang Di Matriks X
    for linez in range (len(x[0])):
        # Memasukkan Hasil Penjumalahan Matriks X dan Y ke Z
        z[kolomz][linez] = x[kolomz][linez] + y[kolomz][linez]

# Output nya......
print("=============================================================================")
print("TOTAL")
for i in z :
    print(i)
