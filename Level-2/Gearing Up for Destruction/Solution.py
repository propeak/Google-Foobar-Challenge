from fractions import Fraction
def solution():
    a= [4, 30, 50]
    b = [-1 , -1]
    

    N = len(a) # number of gears

    calculation = -a[0]

    for i in range(1, len(a)-1):
        if i % 2 == 0: 
            calculation = calculation - 2 * a[i]
            
        else:
            calculation = calculation + 2 * a[i]


    if N % 2 == 0: # even pegs
        last_radius = float((calculation + a[N-1]))/3     # test case a=[100, 110]. Convert to float to get fractions   
    else:
        last_radius = float(calculation - a[N-1])

    first_radius = last_radius * 2

    if last_radius < 1:
        return b
    else:
        this_radius = first_radius
        for i in range(len(a)-1):
            next_radius = a[i+1] - a[i] - this_radius
            if next_radius < 1:                
                return b
            else:
                this_radius = next_radius
                
        c = Fraction(first_radius).limit_denominator()
        return [c.numerator, c.denominator]

    
            
