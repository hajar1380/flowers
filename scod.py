# scob.py - گل‌فروشی 

flowers = {
    "رز": 150000,
    "لاله": 55000,
    "نرگس": 20000,
    "مریم": 40000
}

basket = {}

def show_products():
    print("\n--- لیست گل‌ها ---")
    for name, price in flowers.items():
        print(f"{name} - {price} تومان")

def add_to_basket():
    name = input("نام گل مورد نظر را وارد کنید: ")
    if name in flowers:
        count = int(input("چند عدد؟ "))
        if name in basket:
            basket[name] += count
        else:
            basket[name] = count
        print(f"{count} عدد {name} به سبد اضافه شد.")
    else:
        print("این گل موجود نیست.")

def show_basket():
    print("\n--- سبد خرید ---")
    total = 0
    for name, count in basket.items():
        price = flowers[name] * count
        total += price
        print(f"{name} × {count} = {price} تومان")
    print(f"جمع کل: {total} تومان")

def main():
    while True:
        print("\n1. نمایش گل‌ها")
        print("2. افزودن به سبد")
        print("3. نمایش سبد خرید")
        print("4. خروج")
        choice = input("انتخاب شما: ")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_basket()
        elif choice == "3":
            show_basket()
        elif choice == "4":
            print("خروج از برنامه.")
            break
        else:
            print("انتخاب نامعتبر.")

if name == "__main__":
    main()