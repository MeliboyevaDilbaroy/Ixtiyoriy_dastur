# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VvqTOKo5be9fNcisPi9JRb0qFmPGUvNb
"""

talabalar = [
    ("Ahmad", "Ibragimov"),
    ("Salim", "Jumayev"),
    ("Diyor", "To'xtayev"),
    ("Zarina", "Rahmatova"),
    ("Ali", "Asqarov")
]

# Ismlar va familyalarni alifbo tartibida sort qilish
talabalar_sorted = sorted(talabalar, key=lambda x: (x[0].lower(), x[1].lower()))

# Natijani chiqarish
print("Talabalar alifbo tartibida:")
for ism, familiya in talabalar_sorted:
    print(f"{ism} {familiya}")