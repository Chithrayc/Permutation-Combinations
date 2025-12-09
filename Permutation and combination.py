print("\n \n Permutation & Combination \n \n ")


#Example 1:Permutation (order matters)

from itertools import permutations  # contain the formula
count=0
data=["apple","banana","orange"]
perm=permutations(data,2)
for i in list(perm):
    print(i)
    count+=1

print("permutation count ", count)

'''    nPr=n!/(n-r)!
           3!/(3-2)!
            6/1=6       '''

#Example 2:Combination (order does not matter)

from itertools import combinations
count=0
fruits=["apple","banana","orange"]
fruits2=["apple","orange","banana"]
perm=combinations(fruits2,2)
for i in list(perm):
    print(i)
    count+=1

print(" combination count: ",count)

'''  nCr=n!/(n-r)!r!
        =3!/(3-2)!2!
        =6/1*2
        =6/2
        =3 '''

#Example 3:Combination with Replacement (Repetition allowed)

from itertools import combinations_with_replacement as cr
count=0
fruits=["apple","banana","orange"]
fruits2=["apple","orange","banana"]
perm=cr(fruits,2)
for i in list(perm):
    print(i)
    count+=1

print(" combination with Element count:",count)
