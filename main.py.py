# Mengimpor library tkinter untuk membuat GUI
import tkinter as tk

# Mengimpor messagebox untuk menampilkan pesan error
from tkinter import messagebox


# Function untuk menghitung diskon
def calculate_discount():
    try:
        # Mengambil nilai original price dari input user
        price = float(price_entry.get())

        # Mengambil nilai discount dari input user
        discount = float(discount_entry.get())

        # Menghitung harga setelah diskon
        final_price = price - (price * discount / 100)

        # Menampilkan hasil final price ke label result
        result_label.config(
            text=f"Final Price: Rp {final_price:.2f}"
        )

    # Jika user memasukkan selain angka
    except ValueError:

        # Menampilkan popup error
        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers!"
        )


# Membuat main window aplikasi
root = tk.Tk()

# Memberikan judul window
root.title("Discount Calculator")

# Mengatur ukuran window
root.geometry("500x260")

# Mengatur warna background menjadi abu-abu
root.configure(bg="#e9e9e9")


# ================= ORIGINAL PRICE =================

# Membuat label Original Price
price_label = tk.Label(
    root,
    text="Original Price:",
    font=("Arial", 14),
    bg="#e9e9e9"
)

# Menampilkan label ke window
price_label.pack(pady=(15,2))


# Membuat kotak input Original Price
price_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=18
)

# Menampilkan input box ke window
price_entry.pack(pady=(0,8))


# ================= DISCOUNT =================

# Membuat label Discount
discount_label = tk.Label(
    root,
    text="Discount (%):",
    font=("Arial", 14),
    bg="#e9e9e9"
)

# Menampilkan label discount
discount_label.pack(pady=(0,2))


# Membuat kotak input Discount
discount_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=18
)

# Menampilkan input discount
discount_entry.pack(pady=(0,12))


# ================= BUTTON =================

# Membuat tombol Calculate
calculate_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 14),
    padx=10,
    pady=4,

    # Saat tombol diklik akan menjalankan function calculate_discount
    command=calculate_discount
)

# Menampilkan tombol ke window
calculate_button.pack(pady=10)


# ================= RESULT =================

# Membuat label untuk menampilkan hasil
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    bg="#e9e9e9"
)

# Menampilkan hasil ke window
result_label.pack(pady=10)


# Menjalankan aplikasi GUI
root.mainloop()