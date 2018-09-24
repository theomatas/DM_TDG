import matrix

  

A = matrix.Graph("tests.txt")
print ("exo 1: text parser", A.get_brut() )

print ("exo 2: matrice", A.get_matrix() )

print ("exo 3: cycle =", A.cycle() )

print()

B = matrix.Graph("t.txt")
print ("exo 1: text parser", A.get_brut() )

print ("exo 2: matrice", A.get_matrix() )

print ("exo 3: cycle =", A.cycle() )
