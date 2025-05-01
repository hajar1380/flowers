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
