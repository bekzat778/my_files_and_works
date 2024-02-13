def histogram(f)->list:
    for i in f:
        for j in range(i):
            print('*',end ="")
        print('\n')


k = [5,8,6]
histogram(k)