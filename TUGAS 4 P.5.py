total = 0
jumlah_data = int(input("masukan jumlah data :"))
for i in range (jumlah_data) :
    data = float(input(f"masukan data ke-{i + 1}: "))
    total += data
rata_rata = total / jumlah_data
print(f"Rata-rata dari {jumlah_data} data adalah : {rata_rata}")