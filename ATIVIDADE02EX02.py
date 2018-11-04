lda=int(input("digite o valor para o lado a: "))
ldb=int(input("digite o valor para o lado b: "))
ldc=int(input("digite o valor para o lado c: "))
#considerando lado c a base do triangulo
area=ldc/2
if lda > ldb + ldc:
    print("lado a e {}, lado b e {} e lado c e {}".format(lda, ldb, ldc))

else:
    print(" a area do triangulo é {}".format(area))
    
