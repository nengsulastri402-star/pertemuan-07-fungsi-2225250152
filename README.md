# Pertemuan 07: Fungsi Python

- **Nama:** SULASTRI
- **NIM:** 2225250152
- **Kelas:** B

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular serta mengunggahnya ke GitHub.

## Cara Menjalankan Program
Jalankan program utama melalui terminal VS Code dengan perintah:

```bash
python3 praktik/utilitas_matematika.py
```

## Struktur Fungsi

1. `luas_persegi_panjang(p, l)`: Menerima parameter panjang (`p`) dan lebar (`l`), mengembalikan nilai luas ($p \times l$).
2. `luas_segitiga(a, t)`: Menerima parameter alas (`a`) dan tinggi (`t`), mengembalikan nilai luas segitiga ($0.5 \times a \times t$).
3. `jumlah_n(n)`: Menerima parameter `n`, menghitung akumulasi $1 + 2 + \dots + n$ menggunakan perulangan `for`, dan mengembalikan totalnya.
4. `faktorial(n)`: Menerima parameter `n`, menghitung perkalian faktorial ($n!$) menggunakan perulangan, dan mengembalikan hasilnya.
5. `tampilkan_menu()`: Menampilkan pilihan menu operasi matematika ke layar terminal.

## Hasil Pengujian

| Operasi | Input | Hasil Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Luas persegi panjang | p=8, l=5 | 40 | 40.0 | Lolos |
| Luas segitiga | a=10, t=6 | 30.0 | 30.0 | Lolos |
| Jumlah 1..n | n=10 | 55 | 55 | Lolos |
| Faktorial | n=5 | 120 | 120 | Lolos |
| Faktorial | n=0 | 1 | 1 | Lolos |

## Refleksi

Pemisahan kode menjadi fungsi-fungsi modular membuat program menjadi lebih rapi, mudah dibaca, serta memudahkan pengujian setiap rumus matematika secara independen tanpa harus menyalin baris kode berkali-kali. Penggunaan parameter dan return value memungkinkan setiap fungsi fokus pada satu tugas khusus.
