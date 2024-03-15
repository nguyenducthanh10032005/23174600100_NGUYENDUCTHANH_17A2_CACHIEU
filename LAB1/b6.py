import math

def Cộng_vecto(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def Trừ_vecto(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def Độ_dài_vecto(e):
    return math.sqrt(e[0]**2 + e[1]**2 + e[2]**2)

def Nhân_2vector(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def Góc_cosin(a, b):
    Độ_dài_a = Độ_dài_vecto(a)
    Độ_dài_b = Độ_dài_vecto(b)
    Q = Nhân_2vector(a, b)
    cosine = Q / (Độ_dài_a * Độ_dài_b)
    return round(cosine, 2)

# Nhập tọa độ của vecto a
a = []
for i in range(3):
    m = float(input(f"Nhập tọa độ thứ {i+1} của vecto a: "))
    a.append(m)

# Nhập tọa độ của vecto b
b = []
for i in range(3):
    n = float(input(f"Nhập tọa độ thứ {i+1} của vecto b: "))
    b.append(n)

# Phép cộng vecto a + b
c = Cộng_vecto(a, b)
print("Kết quả phép cộng a + b:", c)

# Phép trừ vecto a - b
d = Trừ_vecto(a, b)
print("Kết quả phép trừ a - b:", d)

# Độ dài của vecto a và b
Độ_dài_a = Độ_dài_vecto(a)
Độ_dài_b = Độ_dài_vecto(b)
print("Độ dài của vecto a:", Độ_dài_a)
print("Độ dài của vecto b:", Độ_dài_b)

# Cosin góc hợp giữa hai vecto a và b
cosine = Góc_cosin(a, b)
print("Cosin góc hợp giữa hai vecto a và b:", cosine)