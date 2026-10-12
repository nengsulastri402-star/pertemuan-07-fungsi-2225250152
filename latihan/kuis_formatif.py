# ==============================================================================
# KUIS FORMATIF PERTEMUAN 07: FUNGSI, PARAMETER, RETURN VALUE, SCOPE & GITHUB
# ==============================================================================

"""
1. Apa fungsi kata kunci def dalam Python?
Jawaban:
Kata kunci 'def' digunakan untuk mendefinisikan (membuat) sebuah fungsi baru di Python.

2. Apa perbedaan parameter dan argumen?
Jawaban:
- Parameter: Nama variabel yang dituliskan di dalam tanda kurung saat fungsi DIDEFINISIKAN.
- Argumen: Nilai aktual yang dikirimkan ke dalam fungsi saat fungsi DIPANGGIL.

3. Kapan return lebih tepat daripada print?
Jawaban:
'return' lebih tepat digunakan saat hasil pemrosesan fungsi ingin disimpan ke dalam variabel,
dipakai kembali untuk perhitungan matematika lain, atau diteruskan ke proses lanjutan. 
'print' hanya berguna untuk menampilkan keluaran ke layar tanpa mengembalikan nilai.

4. Apa nilai variabel x pada kode x = kuadrat(4) jika kuadrat mengembalikan x*x?
Jawaban:
Nilainya adalah 16 (4 * 4).

5. Mengapa variabel lokal sebaiknya tidak bergantung pada perubahan dari luar fungsi?
Jawaban:
Agar fungsi bersifat mandiri (modular), terhindar dari efek samping yang tak terduga (side-effects),
serta lebih mudah diuji, dilacak keterhubungannya, dan digunakan kembali (reusable).

6. Apa yang terjadi jika fungsi memerlukan dua parameter tetapi hanya diberi satu argumen?
Jawaban:
Python akan menghasilkan eror bertipe TypeError (TypeError: missing 1 required positional argument).

7. Bagaimana cara memakai nilai return dalam perhitungan lain?
Jawaban:
Nilai return dapat dipanggil secara langsung di dalam ekspresi/operasi aritmetika.
Contoh: total = kuadrat(3) + kuadrat(4)

8. Apa perbedaan Step Into dan Step Over saat debugging fungsi di VS Code?
Jawaban:
- Step Into (F11): Masuk dan menelusuri eksekusi baris demi baris DI DALAM badan fungsi.
- Step Over (F10): Menjalankan fungsi tersebut sekaligus tanpa masuk ke dalam badan fungsi,
  lalu melompat langsung ke baris perintah berikutnya.

9. Mengapa modularisasi membantu pengujian program?
Jawaban:
Modularisasi memecah program besar menjadi bagian-bagian kecil (fungsi) yang fokus pada 1 tugas.
Hal ini mempermudah isolasi masalah dan debugging saat terjadi eror.

10. Perintah Git apa yang mengirim commit lokal ke GitHub setelah remote sudah terhubung?
Jawaban:
Perintah 'git push' (atau 'git push -u origin main' untuk push pertama kali).
"""

def kuadrat(x):
    return x * x

def demonstrasi_kuis():
    print("=== DEMONSTRASI JAWABAN KUIS FORMATIF ===")
    
    # Jawaban Soal 4 & 7
    hasil_kuadrat = kuadrat(4)
    print(f"Jawaban Soal 4: Nilai kuadrat(4) = {hasil_kuadrat}")
    
    ekspresi = kuadrat(3) + kuadrat(4)
    print(f"Jawaban Soal 7: kuadrat(3) + kuadrat(4) = {ekspresi}")

if __name__ == "__main__":
    demonstrasi_kuis()
