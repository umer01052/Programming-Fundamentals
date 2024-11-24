def main():
    a = int ( input ('Enter A: '))
    b = int ( input ('Enter B: '))
    c = int ( input ('Enter C: '))
    if a == 0:
        print ('Equation is linear having only one root:  {-c/b}')
        
    disc =  (b**2) - 4 * a * c
    if disc < 0:
        print ('Roots are imaginary')
        
    disc=disc**0.5
    d = 2 * a
    x1 = ( -b + disc ) / d
    x2 = ( -b - disc ) / d
    print ('X1:', x1)
    print ('X2:', x2)

main()
