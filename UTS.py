harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

total_harga = harga_barang * jumlah_barang

print("Total harga:", total_harga)

uang_dibayar = float(input("Masukkan jumlah uang yang dibayar: "))

if uang_dibayar >= total_harga:
  kembalian = uang_dibayar - total_harga
  print("Kembalian:", kembalian)
else:
  kekurangan = total_harga - uang_dibayar
  print("Uang yang dibayarkan kurang", kekurangan)