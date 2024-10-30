a = int(input('masukan lama pemakaian tv perjam :'))
b = int(input('masukan daya tv :'))
harga = int(input('harga kwh :'))

hasil = a * b
tv = hasil / 1000

harga_total_tv = tv * 1500

print('harga total tv perjam: Rp', harga_total_tv)

bulan = harga_total_tv * 30
print('harga total tv bulan: Rp', bulan)

a = int(input('masukan lama pemakaian kipas perjam :'))
b = int(input('masukan daya kipas :'))
harga = int(input('harga kwh :'))

hasil = a * b
kipas = hasil / 1000

harga_total_kipas = kipas * 1500

print('harga total kipas perjam: Rp', harga_total_kipas)

bulan = harga_total_kipas * 30
print('harga total kipas bulan: Rp', bulan)

a = int(input('masukan lama pemakaian lampu perjam :'))
b = int(input('masukan daya lampu :'))
harga = int(input('harga kwh :'))

hasil = a * b
lampu = hasil / 1000

harga_total_lampu = lampu * 1500

print('harga total lampu perjam: Rp', harga_total_lampu)

bulan = harga_total_lampu * 30
print('harga total lampu bulan: Rp', bulan)
