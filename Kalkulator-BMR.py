import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Fungsi
def bmr_laki(berat, tinggi, usia, aktivitas):
    return (66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)) * aktivitas

def bmr_perempuan(berat, tinggi, usia, aktivitas):
    return (655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)) * aktivitas

def hitung():
    jenis_kelamin_pilihan = jenis_kelamin.get()
    berat = int(input_berat_badan.get())
    tinggi = int(input_tinggi_badan.get())
    usia = int(input_usia.get())
    aktivitas = float(input_aktivitas.get())

    if jenis_kelamin_pilihan == "laki":
        hasil = bmr_laki(berat, tinggi, usia, aktivitas)
    elif jenis_kelamin_pilihan == "perempuan":
        hasil = bmr_perempuan(berat, tinggi, usia, aktivitas)

    hasil_bmr.config(text=f"Jumlah kebutuhan kalori anda adalah {hasil:.2f} kkal", foreground='#007BFF')  # Mengubah warna hasil menjadi biru

# root
root = tk.Tk()
root.title("Kalkulator BMR")

# Mendapatkan lebar dan tinggi layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Menghitung posisi tengah
x_position = (screen_width - 535) // 2  # Sesuaikan lebar jendela dengan kebutuhan
y_position = (screen_height - 635) // 2  # Sesuaikan tinggi jendela dengan kebutuhan

# Mengatur geometri jendela
root.geometry(f"535x635+{x_position}+{y_position}")

# Inisialisasi tema ttkbootstrap dengan tema gelap
style = Style('darkly')

# Frame utama
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Mengatur konfigurasi grid untuk membuat kolom tetap ke samping
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

# Judul Kalkulator BMR dengan warna gelap
judul_label = ttk.Label(main_frame, text="kalkulator Basal Metabolic Rate (Perhitungan Kebutuhan Kalori Harian)", font=("Verdana", 10, "bold"), foreground='white', background='#343a40')
judul_label.grid(row=0, column=0, columnspan=4, pady=10, sticky=tk.W)

# Frame input
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Mengatur konfigurasi grid untuk membuat kolom tetap ke samping
for i in range(2):
    input_frame.grid_columnconfigure(i, weight=1)

# Label dan Entry untuk input data dengan warna gelap
labels = ["Berat badan (kg)", "Tinggi badan (cm)", "Usia (tahun)", "Rerata aktivitas harian (1.2 - 1.8)", "Jenis Kelamin"]
for i, label_text in enumerate(labels):
    ttk.Label(input_frame, text=label_text, padding=(0, 5), foreground='white', background='#343a40').grid(row=i, column=0, sticky=tk.W)

input_berat_badan = ttk.Entry(input_frame)
input_berat_badan.grid(row=0, column=1, padx=10, pady=5)

input_tinggi_badan = ttk.Entry(input_frame)
input_tinggi_badan.grid(row=1, column=1, padx=10, pady=5)

input_usia = ttk.Entry(input_frame)
input_usia.grid(row=2, column=1, padx=10, pady=5)

input_aktivitas = ttk.Entry(input_frame)
input_aktivitas.grid(row=3, column=1, padx=10, pady=5)

jenis_kelamin = tk.StringVar()
jenis_kelamin.set("laki")

laki_button = ttk.Radiobutton(input_frame, text="Laki - laki", variable=jenis_kelamin, value="laki")
laki_button.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

perempuan_button = ttk.Radiobutton(input_frame, text="Perempuan", variable=jenis_kelamin, value="perempuan")
perempuan_button.grid(row=5, column=1, padx=10,pady=5, sticky=tk.W)

# Frame Hitung
hitung_button = ttk.Button(main_frame, text="Hitung", command=hitung, style='info.TButton')  # Mengubah warna tombol menjadi biru
hitung_button.grid(row=2, column=0, pady=10, sticky=tk.W+tk.E)

# Frame Hasil
hasil_bmr = ttk.Label(main_frame, text="", font=("Verdana", 10, "bold"), foreground='#007BFF', background='white')  # Mengubah warna hasil menjadi biru
hasil_bmr.grid(row=3, column=0, pady=10, sticky=tk.W)

# Note keseharian dari 1.2 - 1.8
note_aktivitas_text = "Rentang 1.2 - 1.8 menunjukkan seberapa aktif seseorang dalam kehidupan sehari-hari, Penjelasannya seperti berikut :"
note_aktivitas_text1 = "1.2 (Sangat Ringan): Aktivitas fisik sangat sedikit atau hampir tidak ada, seperti kebanyakan waktu dihabiskan dalam posisi duduk, misalnya, untuk pekerjaan kantor yang tidak melibatkan aktivitas fisik."
note_aktivitas_text2 = "1.375 (Ringan): Aktivitas fisik ringan seperti berjalan kaki ringan atau pekerjaan kantor yang melibatkan beberapa gerakan."
note_aktivitas_text3 = "1.55 (Sedang): Aktivitas fisik sedang, mungkin melibatkan latihan ringan atau aktivitas yang melibatkan gerakan selama sebagian besar hari."
note_aktivitas_text4 = "1.725 (Berat): Aktivitas fisik berat, seperti berjalan kaki berat, pekerjaan kantor yang melibatkan banyak gerakan dan latihan yang berat."
note_aktivitas_text5 = "1.9 (Sangat Berat): Aktivitas fisik sangat berat, seperti berjalan kaki sangat berat, pekerjaan kantor yang melibatkan banyak gerakan dan latihan sangat berat."
note_aktivitas = ttk.Label(main_frame, text=f"{note_aktivitas_text}\n\n{note_aktivitas_text1}\n\n{note_aktivitas_text2}\n\n{note_aktivitas_text3}\n\n{note_aktivitas_text4}\n\n{note_aktivitas_text5}", font=("Verdana", 8), wraplength=500, justify='left', foreground='white', background='#343a40')
note_aktivitas.grid(row=4, column=0, columnspan=4, pady=10, sticky=tk.W)

root.mainloop()
