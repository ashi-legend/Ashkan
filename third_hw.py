balance=1000
while True:
    print('1.mojoudi')
    print('2.variz')
    print('3.bardasht')
    print('4.khorouj')
    choice=input('یک عدد انتخاب کنید:')
    if choice=='1':
        print(balance)
    elif choice=='2':
        try:
            amt=float(input('مبلغ واریزی:'))
            balance=balance+amt
            print(balance,'موجودی جدید')
        except ValueError:
            print('لطفا عدد وارد کن')
    elif choice=='3':
        try:
            amt=float(input('مبلغ برداشتی:'))
            if amt>balance:
                print('وجودی کافی نیست')
            else:
                balance=balance-amt
                print('موجودی باقی مانده:',balance)
        except ValueError:
            print('لطفا عدد وارد کن')
    elif choice=='4':
        print('khorouj')
        break
    else:
        print('گزینه نامعتبر')
        continue







