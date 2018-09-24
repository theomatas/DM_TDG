import matrix_2

  

A = matrix_2.Graph("tests.txt")
print ("exo 1: text parser " + str(A.get_brut()) )

print ("exo 2: matrice " + str(A.get_matrix()) )

print ("exo 3: cycle = " + str(A.cycle()) )

print(" ")

B = matrix_2.Graph("t.txt")
print ("exo 1: text parser " + str(B.get_brut()) )

print ("exo 2: matrice " + str(B.get_matrix()) )

print ("exo 3: cycle = " + str(B.cycle()) )
