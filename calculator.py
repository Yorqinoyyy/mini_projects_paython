# 🧮 Calculator mini project
# Ushbu dastur foydalanuvchidan 2 ta son va amalni qabul qiladi va natijani hisoblab beradi.

def calculator():
    print("🧮 Simple Calculator")
    print("Available operations: +, -, *, /")

    # Foydalanuvchidan sonlar va amal olish
    x = float(input("Birinchi sonni kiriting: "))
    y = float(input("Ikkinchi sonni kiriting: "))
    amal = input("Amalni tanlang (+, -, *, /): ")

    # Amallarni tekshirish
    if amal == '+':
        print(f"Natija: {x + y}")
    elif amal == '-':
        print(f"Natija: {x - y}")
    elif amal == '*':
        print(f"Natija: {x * y}")
    elif amal == '/':
        if y != 0:
            print(f"Natija: {x / y}")
        else:
            print("Xatolik: Nolga bo‘lish mumkin emas!")
    else:
        print("Xatolik: Noto‘g‘ri amal kiritildi.")

calculator()
📌MISOL:
Oddiy kalkulyatorga xush kelibsiz!
Amallar: +  qo'shish | -  ayirish | *  ko'paytirish | /  bo'lish | %  qoldiq | **  daraja
Chiqish uchun 'exit' deb yozing.

Amalni kiriting (+, -, *, /, %, **): *
Birinchi sonni kiriting: 5
Ikkinchi sonni kiriting: 7
✅ Natija: 5.0 * 7.0 = 35.0

Amalni kiriting (+, -, *, /, %, **): exit
✅ Kalkulyatordan chiqildi. Xayr!
