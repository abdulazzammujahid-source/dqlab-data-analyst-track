# DQLab - Exploratory Data Analysis with Python for Beginner
#
# Submitted answers, one block per exercise.


# ======================================================================
# Chapter: Pengenalan Library dalam Python
# ======================================================================

# --- Memanggil library di Python ---
import numpy as np
import pandas as pd

# ======================================================================
# Chapter: Exploratory Data Analysis dengan Pandas - Part 1
# ======================================================================

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
print(order_df.shape)

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
print(order_df.head(10))

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())

# ======================================================================
# Chapter: Exploratory Data Analysis dengan Pandas - Part 2
# ======================================================================

# --- Tugas Praktek ---
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# plot histogram kolom: price
order_df[['price']].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Standar variasi kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].std())
# Varians kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].var())

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Hitung quartile 1
Q1 = order_df[['product_weight_gram']].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[['product_weight_gram']].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3 - Q1
print(IQR)

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
order_df.rename(columns={'freight_value': 'shipping_cost'}, inplace=True)
print(order_df)

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

# --- Tugas Praktek ---
import pandas as pd
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)

# ======================================================================
# Chapter: Mini Project
# ======================================================================

# --- Tugas dari Andra ---
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/order.csv")
# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)
# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["order_delivered_customer_date"]].hist(figsize=(4, 5), bins=5)
plt.show()
