def sol():
    a = [1, 2, 3, 4, 8, 12]
    
    count = 0
    N = len(a)
    for j in range(1, N - 1):
        count_j = 0
        count_k = 0

        for i in range(j):
            if a[j] % a[i] == 0:                
                count_j += 1

        
        for k in range(j+1, N):
            if a[k] % a[j] == 0:
                count_k+=1
                
        count += count_j * count_k  

    return count
