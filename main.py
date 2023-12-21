import math

matrix_values = [
    [1.00, 1.00 / 5.00, 1.00 / 14.00, 1.00 / 27.00],
    [5.00, 1.00, 5.00 / 14.00, 5.00 / 27.00],
    [14.00, 14.00/5.00, 1.00, 14.00 / 27.00],
    [27.00, 27.00/5.00, 27.00/14.00, 1.0]
]

G1 = 1
G2 = 5
G3 = 14
G4 = 27

Vi_array = []
Pi_array = []
sum_Vi = 0

print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Matrix: ' + '\033[0m')

print("      ", end="")
for j in range(len(matrix_values[0])):
    print(f'G{j + 1}'.ljust(10), end="")
print("Vi".ljust(10) + "Pi".ljust(10))

for i, row in enumerate(matrix_values):
    Vi = math.pow(row[0] * row[1] * row[2] * row[3], 1 / 4)
    Vi_array.append(Vi)
    sum_Vi += Vi

for i, Vi in enumerate(Vi_array):
    Pi = Vi / sum_Vi
    Pi_array.append(Pi)
    print(f'G{i + 1}  ', end="")
    for value in matrix_values[i]:
        print(f"{value:.2f}".ljust(10), end="")
    print(f"{Vi:.2f}".ljust(10) + f"{Pi:.2f}".ljust(10))

En1 = [sum(matrix_values[i][j] * Pi_array[j] for j in range(len(matrix_values[0]))) for i in range(len(matrix_values))]
En2 = [En1[i] / Pi_array[i] for i in range(len(matrix_values))]

print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Matrix of En1 and En2:' + '\033[0m')

print("      ", end="")
for j in range(len(matrix_values[0])):
    print(f'G{j + 1}'.ljust(10), end="")
print("\nEn1    ", end="")
for i in range(len(matrix_values)):
    print(f"{En1[i]:.2f}".ljust(10), end="")
print("\nEn2    ", end="")
for i in range(len(matrix_values)):
    print(f"{En2[i]:.1f}".ljust(10), end="")
print()

lambda_max = sum(En2) / 4
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'lambda max:' + '\033[0m', f"{lambda_max:.1f}")

agreeableness_index = (lambda_max - len(matrix_values)) / (len(matrix_values) - 1)
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Agreeableness index (UI):' + '\033[0m', f"{agreeableness_index:.1f}")

random_index = 0.9
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Random index (WI):' + '\033[0m', random_index)

agreement_relation = agreeableness_index / random_index
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Agreement relation (WU):' + '\033[0m', f"{agreement_relation:.1f}")

if agreement_relation < 0.1:
    print('The degree of agreement should be considered satisfactory')
elif 0.1 < agreement_relation < 0.3:
    print('The degree of agreement should be considered acceptable')
else:
    print('The expert is advised to reconsider his judgments.')
