zero=['   xx   ',
      ' xx  xx ',
      'xx    xx',
      'xx    xx',
      'xx    xx',
      ' xx  xx ',
      '   xx   ']

jeden=['    xx  ',
       '  xxxx  ',
       ' xx xx  ',
       '    xx  ',
       '    xx  ',
       '    xx  ',
       '  xxxxxx']


dwa=['   xx   ',
     ' xx   xx',
     'xx    xx',
     '    xx  ',
     '   xx   ',
     '  xx    ',
     ' xxxxxxx']


trzy=['   xx   ',
      'xx   xx ',
      '      xx',
      '    xx  ',
      '      xx',
      'xx   xx ',
      '   xx   ']


cztery=['    xxx  ',
        '  xx xx  ',
        ' xx  xx  ',
        'xx   xx  ',
        'xxxxxxxx ',
        '     xx  ',
        '     xx  ']


pięć=['xxxxxxxx',
      'xx      ',
      'xx      ',
      'xxxxxxxx',
      '      xx',
      'xx   xx ' ,
      '  xxxx  ']


sześć=['   xxxx   ',
       ' xx    xx ',
       'xx        ',
       ' xxxxxxx  ',
       'xx      xx',
       ' xx    xx ' ,
       '   xxxx   ']


siedem=['xxxxxxxxx',
        '      xx ',
        '     xx  ',
        '   xx    ',
        '  xx     ',
        ' xx      ',
        'xx       ']


osiem=['   xxxx   ',
       ' xx    xx ',
       'xx      xx',
       '  xxxxxx  ',
       'xx      xx',
       ' xx    xx ' ,
       '   xxxx   ']


dziewięć=['  xxxx  ',
          'xx    xx',
          'xx    xx',
          '  xxxx  ',
          '      xx',
          'xx   xx ',
          '   xx   ']

a = input('Podaj liczbę: ')
for i in range(7):
    tekst_do_wypisania=""
    for j in range (len(a)):
        if a[j]=='0':
            tekst_do_wypisania+=zero[i]
        if a[j]=='1':
            tekst_do_wypisania+=jeden[i]
        if a[j]=='2':
            tekst_do_wypisania+=dwa[i]
        if a[j]=='3':
            tekst_do_wypisania+=trzy[i]
        if a[j]=='4':
            tekst_do_wypisania+=cztery[i]
        if a[j]=='5':
            tekst_do_wypisania+=pięć[i]
        if a[j]=='6':
            tekst_do_wypisania+=sześć[i]
        if a[j]=='7':
            tekst_do_wypisania+=siedem[i]
        if a[j]=='8':
            tekst_do_wypisania+=osiem[i]
        if a[j]=='9':
            tekst_do_wypisania+=dziewięć[i]

        tekst_do_wypisania+='    '
    print(tekst_do_wypisania)