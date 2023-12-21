import numpy as np
import math

t_interval = np.arange(0, 51, 5)

a_ij_hat = [
    [0.6, 0.3, 0.2, 0.5, 0, 0.25, 0.4],
    [0, 0, 0.4, 0.3, 0, 0, 0.3],
    [0, 0, 0.7, 0.6, 0.4, 0.45, 0.35],
    [0, 0, 0.45, 0.5, 0.3, 0.35, 0]
]

i_ij_p_hat = [
    [0.4, 0.5, 0.4, 0.4, 0, 0.3, 0.5],
    [0, 0, 0.3, 0.3, 0, 0, 0.4],
    [0, 0, 0.45, 0.5, 0.3, 0.4, 0.4],
    [0, 0, 0.5, 0.4, 0.45, 0.3, 0]
]

i_ij_d_hat = [
    [0.3, 0.4, 0.5, 0.4, 0, 0.4, 0.6],
    [0, 0, 0.35, 0.2, 0, 0, 0.5],
    [0, 0, 0.35, 0.4, 0.35, 0.5, 0.5],
    [0, 0, 0.35, 0.5, 0.5, 0.3, 0]
]

i_ij_t_hat = [
    [0.7, 0.6, 0.4, 0.6, 0, 0.4, 0.5],
    [0, 0, 0.5, 0.4, 0, 0, 0.4],
    [0, 0, 0.6, 0.4, 0.35, 0.55, 0.6],
    [0, 0, 0.5, 0.5, 0.6, 0.3, 0]
]

alfa_array = []
beta_array = []
hama_array = []


for i in range(4):
    tmp_row = []
    for j in range(7):
        if 0 < a_ij_hat[i][j] <= 1:
            tmp = 1/100*(i_ij_t_hat[i][j]+i_ij_p_hat[i][j])*a_ij_hat[i][j]
            tmp_row.append(tmp)
        else:
            tmp_row.append(0)

    alfa_array.append(tmp_row)

# Output
print('\033[1;92m\033[4m\033[7m\033[5m' + 'Alfa:' + '\033[0m')
print("     ", end="")

for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

for i in range(4):
    print(f"S{i+1}: ", end="")
    for j in range(7):
        print(f"{alfa_array[i][j]:.4f}".ljust(8), end="")
    print()



for i in range(4):
    tmp_row = []
    for j in range(7):
        if 0 < a_ij_hat[i][j] <= 1:
            tmp = ((2.718**i_ij_t_hat[i][j])*1/1000/(1+a_ij_hat[i][j])**2)
            tmp_row.append(tmp)
        else:
            tmp_row.append(0)

    beta_array.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Beta:' + '\033[0m')


print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i in range(4):
    print(f"S{i+1}: ", end="")
    for j in range(7):
        print(f"{beta_array[i][j]:.5f}".ljust(8), end="")
    print()

for i in range(4):
    tmp_row = []
    for j in range(7):
        if 0 < a_ij_hat[i][j] <= 1:
            tmp = 2.718**(0.001*(i_ij_p_hat[i][j]+i_ij_t_hat[i][j]))*a_ij_hat[i][j]
            tmp_row.append(tmp)
        else:
            tmp_row.append(0)

    hama_array.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Hama:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i in range(4):
    print(f"S{i+1}: ", end="")
    for j in range(7):
        print(f"{hama_array[i][j]:.2f}".ljust(8), end="")
    print()


ip_for_S1 = []


for t in t_interval:
    tmp_row = []
#alfa_array[0][j] = a ij
#a_ij_hat[0][j] = i_p_hat
    for j in range(7):
        if 0 < a_ij_hat[0][j] * math.log10(max(1, (1 + alfa_array[0][j] * i_ij_d_hat[0][j]) * (t * t - 1))) <= 1:
            tmp = i_ij_p_hat[0][j] * math.log10(max(1, (1 + alfa_array[0][j] * i_ij_d_hat[0][j]) * (t*t - 1)))
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    ip_for_S1.append(tmp_row)


print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Ip for S1:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{ip_for_S1[i][j]:.5f}".ljust(8), end="")
    print()


id_for_S1 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < hama_array[0][j]*(i_ij_d_hat[0][j]+0.4*t) <= 1:
            tmp = hama_array[0][j]*(i_ij_d_hat[0][j]+0.4*t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    id_for_S1.append(tmp_row)
# Output

print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Id for S1:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{id_for_S1[i][j]:.2f}".ljust(8), end="")
    print()



it_for_S1 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < i_ij_t_hat[0][j]*(1 - beta_array[0][j] * t) <= 1:
            tmp = i_ij_t_hat[0][j]*(1 - beta_array[0][j] * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    it_for_S1.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'It for S1:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{it_for_S1[i][j]:.2f}".ljust(8), end="")
    print()


ip_for_S2 = []


for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < a_ij_hat[1][j] * math.log10(max(1, (1 + alfa_array[1][j] * i_ij_d_hat[1][j]) * (t * t - 1))) <= 1:
            tmp = i_ij_p_hat[1][j] * math.log10(max(1, (1 + alfa_array[1][j] * i_ij_d_hat[1][j]) * (t * t - 1)))
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    ip_for_S2.append(tmp_row)


print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Ip for S2:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{ip_for_S2[i][j]:.2f}".ljust(8), end="")
    print()


id_for_S2 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < hama_array[1][j] * (i_ij_d_hat[1][j] + 0.4 * t) <= 1:
            tmp = hama_array[1][j] * (i_ij_d_hat[1][j] + 0.4 * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    id_for_S2.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Id for S2:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{id_for_S2[i][j]:.2f}".ljust(8), end="")
    print()


it_for_S2 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < i_ij_t_hat[1][j] * (1 - beta_array[1][j] * t) <= 1:
            tmp = i_ij_t_hat[1][j] * (1 - beta_array[1][j] * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    it_for_S2.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'It for S2:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{it_for_S2[i][j]:.2f}".ljust(8), end="")
    print()


ip_for_S3 = []


for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < a_ij_hat[2][j] * math.log10(max(1, (1 + alfa_array[2][j] * i_ij_d_hat[2][j]) * (t * t - 1))) <= 1:
            tmp = i_ij_p_hat[2][j] * math.log10(max(1, (1 + alfa_array[2][j] * i_ij_d_hat[2][j]) * (t * t - 1)))
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    ip_for_S3.append(tmp_row)


print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Ip for S3:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{ip_for_S3[i][j]:.2f}".ljust(8), end="")
    print()



id_for_S3 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < hama_array[2][j] * (i_ij_d_hat[2][j] + 0.4 * t) <= 1:
            tmp = hama_array[2][j] * (i_ij_d_hat[2][j] + 0.4 * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    id_for_S3.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Id for S3:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{id_for_S3[i][j]:.2f}".ljust(8), end="")
    print()


it_for_S3 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < i_ij_t_hat[2][j] * (1 - beta_array[2][j] * t) <= 1:
            tmp = i_ij_t_hat[2][j] * (1 - beta_array[2][j] * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    it_for_S3.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'It for S3:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{it_for_S3[i][j]:.2f}".ljust(8), end="")
    print()



ip_for_S4 = []


for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < a_ij_hat[3][j] * math.log10(max(1, (1 + alfa_array[3][j] * i_ij_d_hat[3][j]) * (t * t - 1))) <= 1:
            tmp = i_ij_p_hat[3][j] * math.log10(max(1, (1 + alfa_array[3][j] * i_ij_d_hat[3][j]) * (t * t - 1)))
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    ip_for_S4.append(tmp_row)


print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Ip for S4:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{ip_for_S4[i][j]:.2f}".ljust(8), end="")
    print()


id_for_S4 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < hama_array[3][j] * (i_ij_d_hat[3][j] + 0.4 * t) <= 1:
            tmp = hama_array[3][j] * (i_ij_d_hat[3][j] + 0.4 * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    id_for_S4.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Id for S4:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{id_for_S4[i][j]:.2f}".ljust(8), end="")
    print()


it_for_S4 = []

for t in t_interval:
    tmp_row = []

    for j in range(7):
        if 0 < i_ij_t_hat[3][j] * (1 - beta_array[3][j] * t) <= 1:
            tmp = i_ij_t_hat[3][j] * (1 - beta_array[3][j] * t)
            tmp_row.append(tmp)
        else:
            tmp_row.append(1)

    it_for_S4.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'It for S4:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{it_for_S4[i][j]:.2f}".ljust(8), end="")
    print()


probability_1 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        tmp = 1 - math.log(1 + alfa_array[0][j] * ip_for_S1[i][j] * id_for_S1[i][j] * it_for_S1[i][j])
        tmp_row.append(tmp)

    probability_1.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Probability_1 n lg(x):' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{probability_1[i][j]:.2f}".ljust(8), end="")
    print()


probability_2 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        tmp = 1 - math.log(1 + alfa_array[1][j] * ip_for_S1[i][j] * id_for_S1[i][j] * it_for_S1[i][j])
        tmp_row.append(tmp)

    probability_2.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Probability_2 n lg(x):' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{probability_2[i][j]:.2f}".ljust(8), end="")
    print()

probability_3 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        tmp = 1 - math.log(1 + alfa_array[2][j] * ip_for_S1[i][j] * id_for_S1[i][j] * it_for_S1[i][j])
        tmp_row.append(tmp)

    probability_3.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Probability_3 n lg(x):' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{probability_3[i][j]:.2f}".ljust(8), end="")
    print()



probability_4 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        tmp = 1 - math.log(1 + alfa_array[3][j] * ip_for_S1[i][j] * id_for_S1[i][j] * it_for_S1[i][j])
        tmp_row.append(tmp)

    probability_4.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Probability_4 n lg(x):' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{probability_4[i][j]:.2f}".ljust(8), end="")
    print()


inequality_1 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        if 0 <= probability_1[i][j] <= 0.9:
            tmp = probability_1[i][j]
        else:
            tmp = 0
        tmp_row.append(tmp)

    inequality_1.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Inequality_1:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{inequality_1[i][j]:.2f}".ljust(8), end="")
    print()


inequality_2 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        if 0 <= probability_2[i][j] <= 0.9:
            tmp = probability_2[i][j]
        else:
            tmp = 0
        tmp_row.append(tmp)

    inequality_2.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Inequality_2:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{inequality_2[i][j]:.2f}".ljust(8), end="")
    print()


inequality_3 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        if 0 <= probability_3[i][j] <= 0.9:
            tmp = probability_3[i][j]
        else:
            tmp = 0
        tmp_row.append(tmp)

    inequality_3.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Inequality_3:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{inequality_3[i][j]:.2f}".ljust(8), end="")
    print()


inequality_4 = []

for i, t_value in enumerate(t_interval):
    tmp_row = []

    for j in range(7):
        if 0<= probability_4[i][j] <= 0.9:
            tmp = probability_4[i][j]
        else:
            tmp = 0
        tmp_row.append(tmp)

    inequality_4.append(tmp_row)

# Output
print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Inequality_4:' + '\033[0m')
# Print header
print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i, t_value in enumerate(t_interval):
    print(f"t:({t_value})  ", end="")
    for j in range(7):
        print(f"{inequality_4[i][j]:.2f}".ljust(8), end="")
    print()




print('\n\033[1;92m\033[4m\033[7m\033[5m' + 'Intervals:' + '\033[0m')

print("      ", end="")
for j in range(7):
    print(f"F{j+1}".ljust(8), end="")
print()

# Print rows
for i in range(4):
    print(f"S{i+1}  ", end="")
    row_has_nonzero = any(inequality_1[i][j] != 0 or inequality_2[i][j] != 0 or inequality_3[i][j] != 0 or inequality_4[i][j] != 0 for j in range(7))

    if row_has_nonzero:
        for j in range(7):
            interval_min = 0.0
            interval_max = 0.9

            if inequality_1[i][j] != 0:
                interval_min = max(interval_min, t_interval[i])
                interval_max = max(interval_max, t_interval[i] + 0.5)

            if inequality_2[i][j] != 0:
                interval_min = max(interval_min, t_interval[i])
                interval_max = max(interval_max, t_interval[i] + 0.5)

            if inequality_3[i][j] != 0:
                interval_min = max(interval_min, t_interval[i])
                interval_max = max(interval_max, t_interval[i] + 0.5)

            if inequality_4[i][j] != 0:
                interval_min = max(interval_min, t_interval[i])
                interval_max = max(interval_max, t_interval[i] + 0.5)

            interval_str = f"[{interval_min:.1f};{interval_max:.1f}]"
            print(interval_str.replace('.', ',').ljust(8), end="")
    else:
        print("[;]".ljust(8) * 7, end="")

    print()

print('\n В результаті обчислень ми отримали наступний висновок: для чотирьох ситуацій (S1-S4) нема допустимого часу на прийняття, '
      'форматування та реалізації рішення')
