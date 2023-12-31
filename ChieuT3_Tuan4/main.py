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

# Tạo các nhãn và ô nhập liệu cho các điểm A, B, C
label_A = tk.Label(root, text="Điểm A (Ax, Ay):")
label_A.grid(row=0, column=0)
entry_Ax = tk.Entry(root)
entry_Ax.grid(row=0, column=1)
entry_Ay = tk.Entry(root)
entry_Ay.grid(row=0, column=2)

label_B = tk.Label(root, text="Điểm B (Bx, By):")
label_B.grid(row=1, column=0)
entry_Bx = tk.Entry(root)
entry_Bx.grid(row=1, column=1)
entry_By = tk.Entry(root)
entry_By.grid(row=1, column=2)

label_C = tk.Label(root, text="Điểm C (Cx, Cy):")
label_C.grid(row=2, column=0)
entry_Cx = tk.Entry(root)
entry_Cx.grid(row=2, column=1)
entry_Cy = tk.Entry(root)
entry_Cy.grid(row=2, column=2)

# Tạo nút Kiểm tra và nút Xóa
check_button = tk.Button(root, text="Kiểm tra", command=check_triangle)
check_button.grid(row=3, columnspan=3)

clear_button = tk.Button(root, text="Xóa", command=clear_entries)
clear_button.grid(row=4, columnspan=3)

# Khởi chạy giao diện
root.mainloop()
