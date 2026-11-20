# DQLab - Fundamental SQL Using INNER JOIN and UNION
#
# Submitted answers, one block per exercise.


# ======================================================================
# Chapter: Penggabungan Tabel dari Relasi Kolom
# ======================================================================

# --- Tugas Praktek ---
SELECT * FROM ms_item_kategori;
SELECT * FROM ms_item_warna;

# --- Menggabungkan Tabel dengan Key Columns ---
SELECT * FROM ms_item_kategori, ms_item_warna
WHERE nama_barang = nama_item;

# --- Bagaimana jika urutan Tabel diubah? ---
SELECT * FROM ms_item_warna, ms_item_kategori
WHERE nama_barang = nama_item;

# --- Menggunakan Prefix Nama Tabel ---
SELECT ms_item_kategori.*, ms_item_warna.*
FROM ms_item_warna, ms_item_kategori
WHERE nama_barang = nama_item;

# --- Penggabungan Tanpa Kondisi ---
SELECT * FROM ms_item_kategori, ms_item_warna;

# ======================================================================
# Chapter: INNER JOIN
# ======================================================================

# --- Tugas Praktek: Menggunakan INNER JOIN (1/3) ---
SELECT * FROM ms_item_kategori INNER JOIN ms_item_warna ON ms_item_kategori.nama_item = ms_item_warna.nama_barang;

# --- tabel tr_penjualan dan tabel ms_produk ---
SELECT * FROM tr_penjualan;
SELECT * FROM ms_produk;

# --- Tugas Praktek: Menggunakan INNER JOIN (2/3) ---
SELECT * FROM tr_penjualan INNER JOIN ms_produk ON tr_penjualan.kode_produk = ms_produk.kode_produk;

# --- Tugas Praktek: Menggunakan INNER JOIN (3/3) ---
SELECT 
  tr_penjualan.kode_transaksi,
  tr_penjualan.kode_pelanggan,
  tr_penjualan.kode_produk,
  ms_produk.nama_produk,
  ms_produk.harga,
  tr_penjualan.qty,
  ms_produk.harga * tr_penjualan.qty AS total
FROM tr_penjualan
INNER JOIN ms_produk
ON tr_penjualan.kode_produk = ms_produk.kode_produk;

# ======================================================================
# Chapter: UNION
# ======================================================================

# --- Tabel yang Akan Digabungkan ---
SELECT * FROM tabel_A;
SELECT * FROM tabel_B;

# --- Menggunakan UNION ---
SELECT * FROM tabel_A
UNION
SELECT * FROM tabel_B;

# --- Menggunakan UNION dengan Klausa WHERE ---
SELECT * FROM tabel_a
WHERE kode_pelanggan = 'dqlabcust03'
UNION
SELECT * FROM tabel_b
WHERE kode_pelanggan = 'dqlabcust03';

# --- Menggunakan UNION dan Menyelaraskan Kolom-Kolomnya. ---
SELECT CustomerName, ContactName, City, PostalCode 
FROM Customers 
UNION 
SELECT SupplierName, ContactName, City, PostalCode 
FROM Suppliers;

# ======================================================================
# Chapter: Mini Project
# ======================================================================

# --- Project INNER JOIN ---
SELECT DISTINCT ms_pelanggan.kode_pelanggan, ms_pelanggan.nama_customer, ms_pelanggan.alamat FROM ms_pelanggan INNER JOIN tr_penjualan ON ms_pelanggan.kode_pelanggan = tr_penjualan.kode_pelanggan WHERE tr_penjualan.nama_produk IN ('Kotak Pensil DQLab', 'Flashdisk DQLab 32 GB', 'Sticky Notes DQLab 500 sheets');

# --- Project UNION ---
SELECT kode_produk, nama_produk, harga FROM ms_produk_1 WHERE harga < 100000
UNION
SELECT kode_produk, nama_produk, harga FROM ms_produk_2 WHERE harga < 50000;
