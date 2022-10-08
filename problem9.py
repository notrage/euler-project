def problem9():
    for i in range (1, 998):
        for j in range (i, 998):
            for k in range(i+j, 998):
                if ( (i**2 + j**2 == k**2) or (i**2 + k**2 == j**2) or (j**2 + k**2 == i**2) ) and (i + j + k == 1000):
                    print(i*j*k,i,j,k)