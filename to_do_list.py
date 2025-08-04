# To-Do List mini project
# Ushbu dastur foydalanuvchiga vazifalar qo‘shish, ko‘rish va o‘chirish imkonini beradi.

def to_do_list():
    tasks = []  # Vazifalarni saqlash uchun bo'sh ro'yxat

    while True:
        print("\n--- To-Do List ---")
        print("1. Vazifa qo'shish")
        print("2. Vazifalarni ko'rish")
        print("3. Vazifani o'chirish")
        print("4. Chiqish")

        choice = input("Tanlovingiz (1-4): ")

        if choice == '1':
            task = input("Yangi vazifani kiriting: ")
            tasks.append(task)
            print(f"✅ Vazifa qo'shildi: {task}")
        elif choice == '2':
            if tasks:
                print("\n📋 Vazifalar:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("❌ Vazifalar yo‘q.")
        elif choice == '3':
            if tasks:
                index = int(input("O'chirish uchun vazifa raqamini kiriting: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"🗑️ O‘chirildi: {removed}")
                else:
                    print("❌ Noto‘g‘ri raqam!")
            else:
                print("❌ Vazifalar yo‘q.")
        elif choice == '4':
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov!")

to_do_list()
