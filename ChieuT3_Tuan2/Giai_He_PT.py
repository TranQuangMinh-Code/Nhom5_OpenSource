# Bài này giải hệ phương trình x + 2y = 5 và 3x + 4y = 6
# Yêu cầu hoàn chỉnh lại đoạn code
# Để có 1 app giải hệ phương trình có n phương trình n ẩn
import tkinter

import numpy as np
from tkinter import *

print("Giải Hệ Phương Trình:")
print("Phương Trình 1:")
x1 = int(input("    +) Nhập x1 = "))
y1 = int(input("    +) Nhập y1 = "))
t1 = int(input(f"+) PT1: {x1}x + {y1}y = "))
print("Phương Trình 2:")
x2 = int(input("    +) Nhập x2 = "))
y2 = int(input("    +) Nhập y2 = "))
t2 = int(input(f"+) PT2: {x2}x + {y2}y = "))
print("Hệ Phương Trình: ")
print(f"    {x1}x + {y1}y = {t1}")
print(f"    {x2}x + {y2}y = {t2}")

print("1) Tạo ma trận A:")
A = np.array([(x1,y1),(x2,y2)])
print(A)

print("2) Tạo ma trận B:")
B = np.array([t1,t2])
print(B)

print("3) Nghịch đảo ma trận A:")
A1 = np.linalg.inv(A)   #Tạo ma trận nghịch đảo
print(A1)

X = np.dot(A1,B)
print('Nghiệm của hệ: ', X)