a = int(input('masukan lama pemakaian tv perjam :'))
b = int(input('masukan lama pemakaian kipas perjam :'))
c = int(input('masukan lama pemakaian lampu perjam :'))

print()

tv = int(input('masukan daya tv :'))
kipas = int(input('masukan daya kipas :'))
lampu = int(input('masukan daya lampu : :'))

total_daya_tv = tv * a
total_daya_kipas = kipas * b
total_daya_lampu = lampu * c

total_pemakaian_bulan_tv = total_daya_tv / 1000
total_pemakaian_bulan_kipas = total_daya_kipas / 1000
total_pemakaian_bulan_lampu = total_daya_lampu / 1000

print()
print('total pemakaian per jam: ', total_pemakaian_bulan_tv)
print('total pemakaian per jam: ', total_pemakaian_bulan_kipas)
print('total pemakaian per jam: ', total_pemakaian_bulan_lampu)
print()

total_pemakaian_bulan_tv = total_pemakaian_bulan_tv * 30
total_pemakaian_bulan_kipas = total_pemakaian_bulan_kipas * 30
total_pemakaian_bulan_lampu = total_pemakaian_bulan_lampu * 30

biaya_listrik_tv = total_pemakaian_bulan_tv * 1500
biaya_listrik_kipas = total_pemakaian_bulan_kipas * 1500
biaya_listrik_lampu = total_pemakaian_bulan_lampu * 1500
biaya_listrik_seluruh = biaya_listrik_kipas + biaya_listrik_lampu + biaya_listrik_tv

print('total pemakaian  perbulan:', total_pemakaian_bulan_tv,'kwh')
print('total pemakaian  perbulan:', total_pemakaian_bulan_kipas,'kwh')
print('total pemakaian  perbulan:', total_pemakaian_bulan_lampu,'kwh')
print()
print('harga biaya penggunaan listrik TV sebulan', 'Rp', biaya_listrik_tv)
print('harga biaya penggunaan listrik Kipas sebulam', 'Rp', biaya_listrik_kipas)
print('harga biaya penggunaan listrik Lampu sebulan', 'Rp', biaya_listrik_lampu)
print('harga biaya penggunaan listrik Keseluruhan sebulan', 'Rp', biaya_listrik_seluruh)
