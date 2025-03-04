from colorama import Fore, Style
import numpy as np
import statistics

# judul
print(Fore.BLACK + "=" * 50)
print("Welcome to Math with Python 1: Aljabar Linear and Statistics")
print("=" * 50 + Style.RESET_ALL)

# aljabar
def solve_linear_equation(a, b):
    """Menyelesaikan persamaan linear ax + b = 0"""
    if a == 0:
        return "Tidak ada solusi" if b != 0 else "Tak hingga solusi"
    return -b / a

def matrix_operations():
    """Operasi dasar pada matriks"""
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(Fore.YELLOW + "\nOperasi Matriks:" + Style.RESET_ALL)
    print("Matriks A:\n", A)
    print("Matriks B:\n", B)
    print("Penjumlahan A + B:\n", A + B)
    print("Perkalian A * B:\n", np.dot(A, B))

# statistik
def basic_statistics(data):
    """Menghitung statistik dasar (mean, median, modus, std dev)"""
    print(Fore.CYAN + "\nStatistik Data:" + Style.RESET_ALL)
    print("Data:", data)
    print("Mean (Rata-rata):", statistics.mean(data))
    print("Median:", statistics.median(data))
    try:
        print("Modus:", statistics.mode(data))
    except:
        print("Modus: Tidak ada (semua nilai unik)")
    print("Standar Deviasi:", statistics.stdev(data))

# start program
# Contoh Aljabar Linear
a, b = 2, -4  # Persamaan 2x - 4 = 0
solution = solve_linear_equation(a, b)
print(Fore.YELLOW + "\nSolusi dari 2x - 4 = 0 adalah x =", solution, Style.RESET_ALL)

# Contoh Operasi Matriks
matrix_operations()

# Contoh Statistik
data = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80]
basic_statistics(data)