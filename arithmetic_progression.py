# first n terms of AP.

#a => first number
#d => common difference
#n => number of terms

a = int(input("enter the first number"))
d = int(input("enter the common difference"))
n = int(input("enter number of terms"))

for i in range (1,1+n):
    n_term = a + (i-1)*d
    print(n_term)

sum_n = (n_term/2) * (2*a+(n-1)*d)
print(sum_n)