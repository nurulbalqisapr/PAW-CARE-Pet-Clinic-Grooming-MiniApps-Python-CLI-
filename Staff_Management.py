# =================================================
# MAIN MENU (4) VIEW / MANAGE STAFF 
# =================================================

from Database import staff_data, services

# ===== FUNCTION UNTUK MENAMPILKAN STAFF =====
def display_staff_table():
    width = 100
    print("\n" + "=" * width)
    print("PAW-CARE: PET CLINIC & GROOMING".center(width))
    print("STAFF DATA".center(width))
    print("=" * width)

    # header tabel
    print(f"┌{'─'*4}┬{'─'*25}┬{'─'*20}┬{'─'*25}┬{'─'*15}┐")
    print(f"│ {'No':<2} │ {'Name':<23} │ {'Category':<18} │ {'Service':<23} │ {'Status':<13} │")
    print(f"├{'─'*4}┼{'─'*25}┼{'─'*20}┼{'─'*25}┼{'─'*15}┤")

    for idx, s in enumerate(staff_data, start=1):
        if idx == len(staff_data):
            print(f"│ {idx:<2} │ {s['name']:<23} │ {s['category']:<18} │ {s['service']:<23} │ {s['status']:<13} │")
            print(f"└{'─'*4}┴{'─'*25}┴{'─'*20}┴{'─'*25}┴{'─'*15}┘")
        else:
            print(f"│ {idx:<2} │ {s['name']:<23} │ {s['category']:<18} │ {s['service']:<23} │ {s['status']:<13} │")
            print(f"├{'─'*4}┼{'─'*25}┼{'─'*20}┼{'─'*25}┼{'─'*15}┤")


# ===== FUNCTION ADD STAFF =====
def add_staff():
    while True:
        name = input("\nEnter staff name: ").title()
        if name.isalpha():
            break
        print("✖️  Name must contain letters only")

        if name:
            break
        print("✖️  Name cannot be empty!")

    # Pilih category
    print()
    print("\nCategories available:")
    for idx, cat in enumerate(services.keys(), start=1):
        print(f"[{idx}] {cat}")
    while True:
        cat_choice = input(f"Select Category (1-{len(services)}): ")
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(services):
            category = list(services.keys())[int(cat_choice)-1]
            break
        print("✖️  Invalid selection")

    # Pilih service
    print()
    print(f"\nServices available in {category}:")
    for idx, svc in enumerate(services[category], start=1):
        print(f"[{idx}] {svc}")
    while True:
        svc_choice = input(f"Select Service (1-{len(services[category])}): ")
        if svc_choice.isdigit() and 1 <= int(svc_choice) <= len(services[category]):
            service = services[category][int(svc_choice)-1]
            break
        print("✖️  Invalid selection")

    # Default status
    status = "Available"

    # ===== Konfirmasi sebelum tambah =====
    print("\n------ Confirm Add Staff ------")
    print(f"Name     : {name}")
    print(f"Category : {category}")
    print(f"Service  : {service}")
    print(f"Status   : {status}")
    print("----------------------------------")

    while True:
        confirm = input("Add this staff? (Y/N): ").lower()
        if confirm == "y":
            # ===== INSERT BERDASARKAN CATEGORY =====
            # Temukan index pertama staff dengan kategori > staff baru
            insert_idx = None
            category_order = list(services.keys())
            new_cat_idx = category_order.index(category)

            for i, s in enumerate(staff_data):
                if category_order.index(s['category']) > new_cat_idx:
                    insert_idx = i
                    break

            new_staff = {
                "name": name,
                "category": category,
                "service": service,
                "status": status
            }

            if insert_idx is None:
                staff_data.append(new_staff)
            else:
                staff_data.insert(insert_idx, new_staff)

            print(f"✔ Staff {name} added successfully!")
            break
        elif confirm == "n":
            print("✖️  Add staff cancelled.")
            break
        else:
            print("✖️  Invalid input! Please enter Y or N.")

# ===== FUNCTION UPDATE STAFF STATUS =====
def update_staff_status():
    while True:
        num = input("\nEnter staff number to update status (0 to back): ")
        if num == "0":
            return
        if num.isdigit() and 1 <= int(num) <= len(staff_data):
            idx = int(num) - 1
            staff = staff_data[idx]

            # ===== TAMPILKAN SUMMARY STAFF =====
            print("\n------ Confirm Update Status ------")
            print(f"Name     : {staff['name']}")
            print(f"Category : {staff['category']}")
            print(f"Service  : {staff['service']}")
            print(f"Current Status : {staff['status']}")
            print("----------------------------")

            while True:
                new_status = input("Enter new status (Available/Busy): ").title()
                if new_status in ["Available", "Busy"]:
                    if new_status == staff['status']:
                        print("⚠️ Status unchanged. Enter a different status.")
                    else:
                        confirm = input(f"Change status {staff['status']} → {new_status}? (Y/N): ").lower()
                        if confirm == "y":
                            old_status = staff['status']
                            staff['status'] = new_status
                            print(f"✔ Status updated: {old_status} → {new_status}")
                            return
                        elif confirm == "n":
                            print("✖️  Update cancelled.")
                            return
                        else:
                            print("✖️  Invalid input! Please enter Y or N.")
                else:
                    print("✖️  Invalid status! Use Available or Busy")
        else:
            print("✖️  Invalid number")


# ===== FUNCTION REMOVE STAFF =====
def remove_staff():
    while True:
        num = input("\nEnter staff number to remove (0 to back): ")
        if num == "0":
            return
        if num.isdigit() and 1 <= int(num) <= len(staff_data):
            idx = int(num)-1
            staff = staff_data[idx]

            # ===== TAMPILKAN SUMMARY SEBELUM REMOVE =====
            print("\n------ Confirm Removal ------")
            print(f"Name     : {staff['name']}")
            print(f"Category : {staff['category']}")
            print(f"Service  : {staff['service']}")
            print(f"Status   : {staff['status']}")
            print("----------------------------")

            while True:
                confirm = input("Remove this staff? (Y/N): ").lower()
                if confirm == "y":
                    staff_data.pop(idx)
                    print(f"✔ Staff removed successfully!")
                    return
                elif confirm == "n":
                    print("✖️  Removal cancelled.")
                    return
                else:
                    print("✖️  Invalid input! Please enter Y or N.")
        else:
            print("✖️  Invalid number")


# =================================================
# MAIN MENU (4) VIEW / MANAGE STAFF 
# =================================================
def manage_staff_data(user):
    width = 60
    while True:
        display_staff_table()

        # ================= ADMIN =================
        if user['role'] == "Clinic Administrator":
            print("[1] Add Staff")
            print("[2] Update Staff Status")
            print("[3] Remove Staff")
            print("[0] Back to Main Menu")
            choice = input("Select option (0-3): ")

            if choice == "0":
                break
            elif choice == "1":
                add_staff()
            elif choice == "2":
                update_staff_status()
            elif choice == "3":
                remove_staff()
            else:
                print("✖️  Invalid option. Choose 0-3")

                # ================= STAFF =================
        else:
            print("🔹 View Only Mode - Admin Required to Manage Staff 🔹".center(width))
            input("Press Enter to go back...")
            break


