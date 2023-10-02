from sympy import Point, Triangle
import tkinter as tk
from tkinter import messagebox


def is_triangle(a, b, c):
  # Tạo các điểm từ các đoạn
  point_a = Point(a[0], a[1])
  point_b = Point(b[0], b[1])
  point_c = Point(c[0], c[1])

  # Tạo tam giác từ các điểm
  triangle = Triangle(point_a, point_b, point_c)

  # Kiểm tra xem tam giác có hợp lệ không
  if triangle.is_real:
    return True
  else:
    return False


def clear_entries():
  entry_Ax.delete(0, tk.END)
  entry_Ay.delete(0, tk.END)
  entry_Bx.delete(0, tk.END)
  entry_By.delete(0, tk.END)
  entry_Cx.delete(0, tk.END)
  entry_Cy.delete(0, tk.END)


def check_triangle():
  try:
    A = (float(entry_Ax.get()), float(entry_Ay.get()))
    B = (float(entry_Bx.get()), float(entry_By.get()))
    C = (float(entry_Cx.get()), float(entry_Cy.get()))

    if is_triangle(A, B, C):
      messagebox.showinfo("Kết quả", "Ba đoạn tạo thành một tam giác.")
    else:
      messagebox.showerror("Kết quả", "Ba đoạn không tạo thành một tam giác.")
  except ValueError:
    messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Kiểm tra tam giác")
root.geometry("350x200")

# Tạo các nhãn và ô nhập liệu cho các điểm A, B, C
label_A = tk.Label(root, text="Điểm A:")
label_A.place(x=10,y=20)
label_Ax = tk.Label(root, text="Ax: ")
label_Ax.place(x=70,y=20)
entry_Ax = tk.Entry(root)
entry_Ax.place(x=100,y=22,width=80)
label_Ay = tk.Label(root, text="Ay: ")
label_Ay.place(x=200,y=20)
entry_Ay = tk.Entry(root)
entry_Ay.place(x=230,y=22,width=80)


label_B = tk.Label(root, text="Điểm B:")
label_B.place(x=10,y=50)
label_Bx = tk.Label(root, text="Bx: ")
label_Bx.place(x=70,y=50)
entry_Bx = tk.Entry(root)
entry_Bx.place(x=100,y=52,width=80)
label_By = tk.Label(root, text="By: ")
label_By.place(x=200,y=50)
entry_By = tk.Entry(root)
entry_By.place(x=230,y=52,width=80)

label_C = tk.Label(root, text="Điểm C:")
label_C.place(x=10,y=80)
label_Cx = tk.Label(root, text="Bx: ")
label_Cx.place(x=70,y=80)
entry_Cx = tk.Entry(root)
entry_Cx.place(x=100,y=82,width=80)
label_Cy = tk.Label(root, text="By: ")
label_Cy.place(x=200,y=80)
entry_Cy = tk.Entry(root)
entry_Cy.place(x=230,y=82,width=80)


# Tạo nút Kiểm tra và nút Xóa
check_button = tk.Button(root, text="Kiểm tra", command=check_triangle)
check_button.place(x=60,y=120,width=70)

clear_button = tk.Button(root, text="Xóa", command=clear_entries)
clear_button.place(x=200,y=120,width=70)

# Khởi chạy giao diện
root.mainloop()
