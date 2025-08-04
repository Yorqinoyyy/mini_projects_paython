tasks = []
while True:
    print("\n--- To-Do List ---")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Chiqish")

   tanlov = input("Tanlovingizni kiriting (1/2/3): ")

    if tanlov == "1":
        vazifa = input("Vazifani kiriting: ")
        tasks.append(vazifa)
        print(f"✅ '{vazifa}' ro'yxatga qo'shildi.")
    elif tanlov == "2":
        if tasks:
            print("\n📋 Vazifalar:")
            for i, vazifa in enumerate(tasks, 1):
                print(f"{i}. {vazifa}")
        else:
            print("❌ Hozircha vazifalar yo'q.")
    elif tanlov == "3":
        print("Chiqilmoqda...")
        break
    else:
        print("❌ Noto'g'ri tanlov!")
