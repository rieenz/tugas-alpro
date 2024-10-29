a = int(input('masukan lama pemakaian tv perjam :'))
b = int(input('masukan lama pemakaian kipas perjam :'))
c = int(input('masukan lama pemakaian lampu perjam :'))

harga = 1500

tv = 15
kipas = 10
lampu = 5

total_pemakaian_tv = tv * a
total_pemakaian_kipas = kipas * b
total_pemakaian_lampu = lampu * c

print('total pemakaian per jam: ', total_pemakaian_tv)
print('total pemakaian per jam: ', total_pemakaian_kipas)
print('total pemakaian per jam: ', total_pemakaian_lampu)

total_pemakaian_bulan_tv = total_pemakaian_tv * 30
total_pemakaian_bulan_kipas = total_pemakaian_kipas * 30
total_pemakaian_bulan_lampu = total_pemakaian_lampu * 30

print('total pemakaian  perbulan:', total_pemakaian_bulan_tv,'watt')
print('total pemakaian  perbulan:', total_pemakaian_bulan_kipas,'watt')
print('total pemakaian  perbulan:', total_pemakaian_bulan_lampu,'watt')

total_harga_pemakaian_tv= total_pemakaian_bulan_tv * harga 
total_harga_pemakaian_kipas= total_pemakaian_bulan_kipas * harga 
total_harga_pemakaian_lampu= total_pemakaian_bulan_lampu * harga  

print("Total harga pemakaian: Rp.", total_harga_pemakaian_tv)
print("Total harga pemakaian: Rp.", total_harga_pemakaian_kipas)
print("Total harga pemakaian: Rp.", total_harga_pemakaian_lampu)
