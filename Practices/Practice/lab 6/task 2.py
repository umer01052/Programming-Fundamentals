i=1
while i<=100:
    print(i)
    if i==100:
        d='Hundred'
        print(f'The Number{i} in English is {d}')
    else:
        if i>=20 :
            y=i//10
            z=i%10
            if y==2:
                y='twenty'
            elif y==3:
                y='thirty'
            elif y==4:
                y='fourty'
            elif y==2:
                y='fifty'
            elif y==6:
                y='sixty'
            elif y==7:
                y='seventy'
            elif y==8:
                y='eighty'
            elif y==9:
                y='ninety'
            if z==0:
                z=''
            elif z==1:
                z='one'
            elif z==2:
                z='two'
            elif z==3:
                z='three'
            elif z==4:
                z='four'
            elif z==5:
                z='five'
            elif z==6:
                z='six'
            elif z==7:
                z='seven'
            elif z==8:
                z='eight'
            elif z==9:
                z='nine'
            print(f' The Number {i} in Englih is {y} {z}')
        if i<=20:
            if i==1:
                s='one'
            elif i==2:
                s='Two'
            elif i==3:
                s='Three'
            elif i==4:
                s='Four'
            elif i==5:
                s='five'
            elif i==6:
                s='six'
            elif i==7:
                s='seven'
            elif i==8:
                s='eight'
            elif i==9:
                s='nine'
            elif i==10:
                s='ten'
            elif i==11:
                s='Eleven'
            elif i==12:
                s='Twelve'
            elif i==13:
                s='Thirteen'
            elif i==14:
                s='Fourteen'
            elif i==15:
                s='fifteen'
            elif i==16:
                s='sixteen'
            elif i==17:
                s='seventeen'
            elif i==18:
                s='eighteen'
            elif i==19:
                s='nineteen'
            elif i==20:
                s='twenty'
            print(f' The Number {i} In English is {s}')
          
        
        
    i=i+1
