import numpy as np
# Metode Trapezoidal Rule dengan pembagian equispaced dan input titik
def trapezoidal_rule(x, y):
# x adalah array titik-titik pembagi, y adalah array nilai fungsi pada titik-titik tersebut
    n = len(x) # jumlah titik (jumlah subinterval + 1)
# Menghitung integral menggunakan rumus Trapezoidal
    integral = (x[-1] - x[0]) * (y[0] + 2 * np.sum(y[1:n-1]) + y[n-1]) / (2 * (n - 1))
    return integral
# Contoh penggunaan
# Input titik-titik pembagi secara manual (x) dan nilai fungsi pada titik-titik tersebut (y)
x = np.array([1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8]) # Titik-titik pembagi
y = np.array([1.449, 2.06, 2.645, 3.216, 3.779, 4.338, 4.898]) # Nilai fungsi
# Menghitung integral
result = trapezoidal_rule(x, y)
# Menampilkan hasil
print(f"Integral menggunakan metode Trapezoidal Rule adalah: {result}")