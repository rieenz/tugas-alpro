durasi_pemakaian_tv = int(input('masukan lama pemakaian tv :'))
durasi_pemakaian_kipas = int(input('masukan lama pemakaian kipas :'))
durasi_pemakaian_lampu = int(input('masukan lama pemakaian lampu :'))

tv = int(input('masukan daya tv :'))
kipas = int(input('masukan daya kipas :'))
lampu = int(input('masukan daya lampu : :'))
hargakwh = 1500

total_daya_tv = tv * durasi_pemakaian_tv
total_daya_kipas = kipas * durasi_pemakaian_kipas
total_daya_lampu = lampu * durasi_pemakaian_lampu

total_pemakaian_bulan_tv = total_daya_tv / 1000
total_pemakaian_bulan_kipas = total_daya_kipas / 1000
total_pemakaian_bulan_lampu = total_daya_lampu / 1000

total_pemakaian_bulan_tv = total_pemakaian_bulan_tv * 30
total_pemakaian_bulan_kipas = total_pemakaian_bulan_kipas * 30
total_pemakaian_bulan_lampu = total_pemakaian_bulan_lampu * 30

biaya_listrik_tv = total_pemakaian_bulan_tv * 1500
biaya_listrik_kipas = total_pemakaian_bulan_kipas * 1500
biaya_listrik_lampu = total_pemakaian_bulan_lampu * 1500
biaya_listrik_seluruh = biaya_listrik_kipas + biaya_listrik_lampu + biaya_listrik_tv

print('pemakaian daya tv perjam: ', total_pemakaian_bulan_tv)
print('pemakaian daya kipas perjam: ', total_pemakaian_bulan_kipas)
print('pemakaian daya lampu perjam: ', total_pemakaian_bulan_lampu)

print('pemakaian daya tv perbulan:', total_pemakaian_bulan_tv,'kwh')
print('pemakaian daya kipas perbulan:', total_pemakaian_bulan_kipas,'kwh')
print('pemakaian daya lampu perbulan:', total_pemakaian_bulan_lampu,'kwh')

print('harga biaya penggunaan listrik TV sebulan', 'Rp', biaya_listrik_tv)
print('harga biaya penggunaan listrik Kipas sebulam', 'Rp', biaya_listrik_kipas)
print('harga biaya penggunaan listrik Lampu sebulan', 'Rp', biaya_listrik_lampu)
print('harga biaya penggunaan listrik Keseluruhan sebulan', 'Rp', biaya_listrik_seluruh)
