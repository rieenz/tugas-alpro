a = int(input('masukan lama pemakaian tv perjam :'))
b = int(input('masukan lama pemakaian kipas perjam :'))
c = int(input('masukan lama pemakaian lampu perjam :'))

tv = int(input('masukan daya tv :'))
kipas = int(input('masukan daya kipas :'))
lampu = int(input('masukan daya lampu : :'))

total_pemakaian_tv = tv * a / 1000
total_pemakaian_kipas = kipas / 1000
total_pemakaian_lampu = lampu / 1000

print('total pemakaian per jam: ', total_pemakaian_tv)
print('total pemakaian per jam: ', total_pemakaian_kipas)
print('total pemakaian per jam: ', total_pemakaian_lampu)

total_pemakaian_bulan_tv = total_pemakaian_tv * 30
total_pemakaian_bulan_kipas = total_pemakaian_kipas * 30
total_pemakaian_bulan_lampu = total_pemakaian_lampu * 30

print('total pemakaian  perbulan:', total_pemakaian_bulan_tv,'kwh')
print('total pemakaian  perbulan:', total_pemakaian_bulan_kipas,'kwh')
print('total pemakaian  perbulan:', total_pemakaian_bulan_lampu,'kwh')




