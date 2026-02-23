# ===========================================================
# MAIN MENU (2) VIEW / MANAGE PAW-CARE: SERVICES (MAIN MENU)
# ===========================================================
from Database import services_data

# DISPLAY SERVICE TABLE 
def display_services_table():
    width = 70

    # Cetak tabel
    print("\n" + "=" * width)
    print("PAW-CARE: PET CLINIC & GROOMING".center(width))
    print("PAW-CARE SERVICES".center(width))
    print("=" * width)

    # HEADER TABEL
    print(f"┌{'─'*4}┬{'─'*20}┬{'─'*25}┬{'─'*17}┐")
    print(f"│ {'No':<2} │ {'Category':<18} │ {'Service':<23} │ {'Price':<15} │")
    print(f"├{'─'*4}┼{'─'*20}┼{'─'*25}┼{'─'*17}┤")

    # ISI TABEL
    for idx, s in enumerate(services_data, start=1):
        price_display = f"Rp {s['price']:,}"  # format ribuan
        if idx == len(services_data):
            print(f"│ {idx:<2} │ {s['category']:<18} │ {s['service']:<23} │ {price_display:<15} │")
            print(f"└{'─'*4}┴{'─'*20}┴{'─'*25}┴{'─'*17}┘")
        else:
            print(f"│ {idx:<2} │ {s['category']:<18} │ {s['service']:<23} │ {price_display:<15} │")
            print(f"├{'─'*4}┼{'─'*20}┼{'─'*25}┼{'─'*17}┤")


# FUNCTION ADMIN PLACEHOLDER
#===============================================
# SUB MENU VIEW / MANAGE SERVICE
# 1. ADD SERVICE 
#----------------------------------
def add_service():
    print("\n" + "=" * 60)
    print("ADD SERVICE".center(60))
    print("=" * 60)
    print()
    display_services_table()
    # Ambil category unik
    categories = sorted(set(s['category'] for s in services_data))

    for idx, cat in enumerate(categories, start=1):
        print(f"[{idx}] {cat}")

    # === PILIH CATEGORY ===
    while True:
        choice = input("Select category number (0 Cancel): ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice)-1]
            break
        else:
            print("✖️  Invalid selection")

    # === INPUT SERVICE NAME (WAJIB) ===
    while True:
        service_name = input("Enter new service name: ").strip().title()

        if service_name == "":
            print("✖️  Service name cannot be empty")
            continue

        if not service_name.replace(" ", "").isalpha():
            print("✖️  Service must contain letters only")
            continue

        # Cek duplikat
        if any(s['category'] == category and s['service'] == service_name for s in services_data):
            print("✖️  Service already exists in this category")
        else:
            break

    # === INPUT PRICE (WAJIB) ===
    while True:
        price_input = input("Enter price: ").strip()

        if not price_input.isdigit():
            print("✖️  Price must be numeric")
            continue

        price = int(price_input)

        if price <= 0:
            print("✖️  Price must be positive")
            continue

        break

    # === SIMPAN DATA ===
    services_data.append({
        "category": category,
        "service": service_name,
        "price": price
    })
    services_data.sort(key=lambda x: (x['category'], x['service']))
    print(f"\n✔ '{service_name}' successfully added to {category}!")

    # === TAMPILKAN TABEL TERBARU ===
    display_services_table()


# 2. UPDATE SERVICE 
#----------------------------------
def update_service():
    print("\n" + "=" * 60)
    print("UPDATE SERVICE".center(width))
    print("=" * 60)
    print()
    display_services_table()

    # ===== PILIH SERVICE =====
    while True:
        choice = input("Select service number to update (0 to cancel): ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(services_data):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    old_data = services_data[idx].copy()
    category = old_data['category']

    # ===== MENU OPSI UPDATE =====
    while True:
        print("\nWhat do you want to update?")
        print("[1] Service Name")
        print("[2] Price")
        print("[3] Both")
        print("[0] Cancel")

        option = input("Select option: ")

        if option in ["1", "2", "3", "0"]:
            break
        else:
            print("✖️  Invalid selection")

    if option == "0":
        return

    # Default nilai baru = lama dulu
    new_name = old_data['service']
    new_price = old_data['price']

    # ===== UPDATE NAME =====
    if option in ["1", "3"]:
        while True:
            name_input = input(f"New name ({old_data['service']}): ").strip().title()

            if name_input == "":
                print("✖️  Name cannot be empty")
                continue

            # Cek duplicate
            if name_input != old_data['service']:
                if any(
                    s['category'] == category and
                    s['service'] == name_input
                    for s in services_data
                ):
                    print("✖️  Service already exists in this category")
                    continue

            new_name = name_input
            break

    # ===== UPDATE PRICE =====
    if option in ["2", "3"]:
        while True:
            price_input = input(f"New price (Rp {old_data['price']:,}): ").strip()

            if not price_input.isdigit():
                print("✖️  Price must be numeric")
                continue

            if int(price_input) <= 0:
                print("✖️  Price must be positive")
                continue

            new_price = int(price_input)
            break

    # ===== CEK TIDAK ADA PERUBAHAN =====
    if new_name == old_data['service'] and new_price == old_data['price']:
        print("✖️  No changes detected.")
        return

    # ===== KONFIRMASI DINAMIS =====
    print("\n------- Confirm Changes -------\n")
    print(f"Category     : {category}")

    if new_name != old_data['service']:
        print(f"Service      : {old_data['service']}  ->  {new_name}")
    else:
        print(f"Service      : {old_data['service']}")

    if new_price != old_data['price']:
        print(f"Price        : Rp {old_data['price']:,}  ->  Rp {new_price:,}")
    else:
        print(f"Price        : Rp {old_data['price']:,}")

    print("------------------------------------")

    # ===== LOOP KONFIRMASI =====
    while True:
        confirm = input("Confirm update? (y/n): ").lower()

        if confirm == "y":
            services_data[idx]['service'] = new_name
            services_data[idx]['price'] = new_price

            services_data.sort(key=lambda x: (x['category'], x['service']))

            print("✔  Service successfully updated!")
            display_services_table()
            return

        elif confirm == "n":
            print("✖️  Update cancelled.")
            return

        else:
            print("✖️  Please enter 'y' or 'n'")


# 3. REMOVE SERVICE 
#----------------------------------
def remove_service():
    print("\n" + "=" * 60)
    print("REMOVE SERVICE".center(width))
    print("=" * 60)
    print()
    display_services_table()
    while True:
        choice = input("Select service number to remove (0 to cancel): ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(services_data):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    selected = services_data[idx]

    # ===== KONFIRMASI =====
    print("\n------ Confirm Delete ------")
    print(f"Category : {selected['category']}")
    print(f"Service  : {selected['service']}")
    print(f"Price    : Rp {selected['price']:,}")
    print("----------------------------")

    while True:
        confirm = input("Are you sure you want to delete this service? (y/n): ").lower()

        if confirm == "y":
            removed = services_data.pop(idx)
            print(f"\n✔  '{removed['service']}' successfully removed!")
            
            # tampilkan tabel terbaru
            display_services_table()
            return

        elif confirm == "n":
            print("✖️  Deletion cancelled.")
            return

        else:
            print("✖️  Please enter 'y' or 'n'")


# =================================================
# MAIN MENU (2) VIEW / MANAGE PAW-CARE: SERVICES 
# =================================================
def manage_services(user):
    width = 70

    # ADMIN OPTIONS
    display_services_table()
    if user['role'] == "Clinic Administrator":
        while True:
            print("\n" + "="*width)
            print("ADMIN OPTIONS".center(width))
            print("="*width)
            print("[1] Add Service and Price")
            print("[2] Update Service and Price")
            print("[3] Remove Service")
            print("[0] Back to Main Menu")
            choice = input("Select Option: ")

            if choice == "1":
                add_service()
            elif choice == "2":
                update_service()
            elif choice == "3":
                remove_service()
            elif choice == "0":
                break
            else:
                print("✖️  Invalid selection! Choose 0-3")
    else:
        # STAFF / VIEW ONLY
        print("\n" + "="*width)
        print("🔹 View Only - Admin Required to Manage Services 🔹".center(width))
        print("="*width)

        input("Press Enter to go back...")
