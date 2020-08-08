import copy
from fractions import Fraction

def sol():
    #a = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    a = [
        [0]
    ]
    
    N = len(a)
    sum = 0
    non_terminal = []
    terminal = []
    f_inverse = [] #I - Q where Q i non terminal, this is same as F inverse matrix
    r_matrix = []
    len_nt = 0 #number of non terminal states

    #express a in form of probablities
    for i in range(N):
        sum = 0
        
        for j in range(N):
            sum += a[i][j]
            if j == N-1:
                if sum == 0:
                    terminal.append(i) #make note of index of terminal states
                else:
                    non_terminal.append(i) #make note of index of non terminal states
                    for k in range(N):
                        a[i][k] = a[i][k] / float(sum)
    
    len_nt = len(non_terminal)
    if len_nt == 0: #no non-terminal states exist. a contains only terminal states
        final = []
        for i in range(len(terminal)):
            final.append(1) #all terminal states have probability of one
        final.append(1) #adding common denominator 1
        return final
    
    for i in range(len_nt): #Do F_inverse = I-Q
        empty_list = []
        for j in range(len_nt):
            if i == j:
                empty_list.append(1 - a[non_terminal[i]][non_terminal[j]])
            else:
                empty_list.append(0 - a[non_terminal[i]][non_terminal[j]])
            
        f_inverse.append(empty_list)
    
    
    for i in range(len_nt):
        p = []
        for j in range(len(terminal)):
            p.append(a[non_terminal[i]][terminal[j]])
        r_matrix.append(p)
        
    f = inverse(f_inverse, len(f_inverse))
    fr_matrix = []
    for i in range(len(f)): #for f rows and columns are always equal
        p = []
        for j in range(len(r_matrix[0])):
            sum_fr = 0
            for k in range(len(r_matrix)):
                sum_fr += f[i][k]* r_matrix[k][j]
            p.append(sum_fr)

        fr_matrix.append(p)

    lcm_list = []
    num_list = []
    lcm = 0
    for j in range(len(fr_matrix[0])):
        frac = Fraction(fr_matrix[0][j]).limit_denominator()
        num_list.append(int(frac.numerator))
        lcm_list.append(int(frac.denominator))

    lcm = find_lcm(lcm_list)
    
    for i in range(len(lcm_list)):
        d = lcm / lcm_list[i]
        num_list[i] = num_list[i] * d

    num_list.append(lcm)
    return num_list    
  
def find_lcm(m):
    n = copy.deepcopy(m)
    min_list = min(n)
    max_list = max(n)
    min_index = n.index(min(n))    

    while(min_list != max_list):
        n[min_index] += m[min_index]
        min_list = min(n)
        max_list = max(n)
        min_index = n.index(min(n))

        all_min = [i for i in range(len(n)) if n[i] == min_list] #find all the minimums
        min_index = max(all_min) #if more than 1 minimum, update

    return n[0]  
        
def swap(augmented_m, i, c):
    for j in range(len(augmented_m * 2)):
        a = []
        a = copy.deepcopy(augmented_m[i][j])
        augmented_m[i][j] = augmented_m[i+c][j]
        augmented_m[i+c][j] = a

def inverse(m, order):
    augmented_m = []
    for i in range(order):
        row = []
        for j in range( 2 * order):
            if j < order:
                row.append(m[i][j])
            elif j == i + order:
                row.append(1)
            else:
                row.append(0)
        augmented_m.append(row)

    temp = []
    for i in range(order):
        temp.append(augmented_m[i][0]) #get all first column elements
    max_element = max(temp) 
    
    for i in range(order):
        if augmented_m[i][i] == 0: #check if this is 0
            c = 1
            if i + c == order: #means i is the last row
                c = -1 #swap with prev row
                while (i-c >= 0) and (augmented_m[i-c][i] == 0): #as long as prev row exists
                    c -= 1 #if prev row element is also 0 then go back another row
                
            while (i + c < order) and (augmented_m[i+c][i] == 0):                
                c += 1 #if next row exists and next row element is also 0
                #then skip current row and go to the next
            swap(augmented_m, i, c)
   
    
    temp = 0
    for i in range(order):
        for j in range(order):
            if j!= i:
                if augmented_m[j][i] == 0:
                    continue
                temp = augmented_m[j][i]/float(augmented_m[i][i])
                for k in range(order * 2):
                    augmented_m[j][k] -= augmented_m[i][k] * temp

    for i in range(order):
        temp = augmented_m[i][i]
        for j in range(order * 2):
            augmented_m[i][j] = augmented_m[i][j]/float(temp)

    inverse_m = []
    for i in range(order):
        copy = []
        for j in range(order, 2*order):
            copy.append(augmented_m[i][j])
        inverse_m.append(copy)

    return inverse_m
