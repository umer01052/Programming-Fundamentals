i=1
while i<=99:
    if i>=10:
        print(i)
        y=i//10
        z=i%10
        print([y,z])
        sum=z+y
        print( 'The sum is',sum)
        if sum>=10:
            r=sum//10
            s=sum%10
            print([r,s])
            sum_1=r+s
            print( 'The sum 1 is',sum_1)
            
    else  :
        print([i])
    i=i+1
    
