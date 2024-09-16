print('Forneça ao programa duas datas distintas para que o programa verificar qual delas veio primeiro: ')
input('ENTENDI: ')
dia1,mes1,ano1,hr1,min1 = input().split()

data1 = ano1*10000000 + mes1 * 10000 + dia1* 100 + hr1

dia2,mes2,ano2,hr2,min2 = input().split()

data2 = ano2*10000000 + mes2 * 10000 + dia2* 100 + hr2

if data1 < data2:
    print('Data 1 veio antes')
else:
    print('Data 2 veio antes')

  20240620
# aaaammdd----

  202406201055
# aaaammddhhmm
