# 🎯 Guess the Number mini project
# Dastur 1 dan 50 gacha tasodifiy son tanlaydi va foydalanuvchi uni topishi kerak.

import random

def guess_number():
    print("🎯 Guess the Number o'yini")
    number = random.randint(1, 50)  # Tasodifiy son tanlash
    attempts = 0

    while True:
        guess = int(input("1 dan 50 gacha son kiriting: "))
        attempts += 1

        if guess < number:
            print("⬆️ Kattaroq son o‘ylang.")
        elif guess > number:
            print("⬇️ Kichikroq son o‘ylang.")
        else:
            print(f"🎉 Tabriklaymiz! {attempts} ta urinishda topdingiz.")
            break

guess_number()
