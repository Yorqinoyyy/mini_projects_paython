def calculator():
    print("📌 Oddiy kalkulyatorga xush kelibsiz!")
    print("Amallar: +  qo'shish | -  ayirish | *  ko'paytirish | /  bo'lish | %  qoldiq | **  daraja")
    print("Chiqish uchun 'exit' deb yozing.")

    while True:
        amal = input("\nAmalni kiriting (+, -, *, /, %, **): ").strip()

        if amal.lower() == "exit":
            print("✅ Kalkulyatordan chiqildi. Xayr!")
            break

        if amal not in ['+', '-', '*', '/', '%', '**']:
            print("❌ Noto'g'ri amal! Qayta urinib ko'ring.")
            continue

        try:
            x = float(input("Birinchi sonni kiriting: "))
            y = float(input("Ikkinchi sonni kiriting: "))

            if amal == '+':
                natija = x + y
            elif amal == '-':
                natija = x - y
            elif amal == '*':
                natija = x * y
            elif amal == '/':
                if y != 0:
                    natija = x / y
                else:
                    print("❌ Nolga bo'lish mumkin emas!")
                    continue
            elif amal == '%':
                natija = x % y
            elif amal == '**':
                natija = x ** y

            print(f"✅ Natija: {x} {amal} {y} = {natija}")

        except ValueError:
            print("❌ Faqat son kiriting!")

# Dastur ishga tushadi
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
