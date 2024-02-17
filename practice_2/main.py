

# print(a)
# print(b)

temp = [1, 2, - 1, -2, -3, 3, 4, 5, -1, 2, 3, 4]
plus_temp = 0
m_a_x = 0
n = len(temp)
for i in range(n):
    if temp[i] > 0:
        plus_temp += 1

    if temp[i] < 0 or i == n:
        if m_a_x < plus_temp:
            m_a_x = plus_temp
        plus_temp = 0


print(m_a_x)