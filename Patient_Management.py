# ==========================================
# MAIN MENU (3) VIEW / MANAGE PATIENT RECORD
# ==========================================
from Database import patient_records, services_data, staff_data

# DISPLAY SERVICE TABLE PATIENT RECORDS
# ==========================================
def display_patient_records_table():
    width = 135
    print("\n" + "=" * width)
    print("PAW-CARE: PET CLINIC & GROOMING".center(width))
    print("PATIENT RECORDS".center(width))
    print("=" * width)

    if not patient_records:  # cek kalau list kosong
        alert_msg = "✖️  No patient records found  ✖️"
        print("\n" + alert_msg.center(width) + "\n")

    else:  
        print(f"┌{'─'*4}┬{'─'*12}┬{'─'*18}┬{'─'*14}┬{'─'*18}┬{'─'*20}┬{'─'*22}┬{'─'*15}┐")
        print(f"│ {'No':<2} │ {'Date':<10} │ {'Owner Name':<16} │ {'Pet Name':<12} │ {'Category':<16} │ {'Service':<18} │ {'Staff':<20} │ {'Status':<13} │")
        print(f"├{'─'*4}┼{'─'*12}┼{'─'*18}┼{'─'*14}┼{'─'*18}┼{'─'*20}┼{'─'*22}┼{'─'*15}┤")

        for idx, p in enumerate(patient_records, start=1):
            if idx == len(patient_records):
                print(f"│ {idx:<2} │ {p['date']:<10} │ {p['owner_name']:<16} │ {p['pet_name']:<12} │ {p['category']:<16} │ {p['service']:<18} │ {p['staff']:<20} │ {p['status']:<13} │")
                print(f"└{'─'*4}┴{'─'*12}┴{'─'*18}┴{'─'*14}┴{'─'*18}┴{'─'*20}┴{'─'*22}┴{'─'*15}┘")
            else:
                print(f"│ {idx:<2} │ {p['date']:<10} │ {p['owner_name']:<16} │ {p['pet_name']:<12} │ {p['category']:<16} │ {p['service']:<18} │ {p['staff']:<20} │ {p['status']:<13} │")
                print(f"├{'─'*4}┼{'─'*12}┼{'─'*18}┼{'─'*14}┼{'─'*18}┼{'─'*20}┼{'─'*22}┼{'─'*15}┤")


# 3. UPDATE PATIENT SERVICE
#----------------------------------
def update_patient_service():
    print("\n" + "=" * 60)
    print("UPDATE CATEGORY AND SERVICE".center(60))
    print("=" * 60)
    print()
    display_patient_records_table()
    # ===== PILIH DATA =====
    while True:
        choice = input("Select patient number to update (0 to cancel): ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(patient_records):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    old_data = patient_records[idx]

    print("\n------- Selected Patient -------")
    print(f"Owner    : {old_data['owner_name']}")
    print(f"Pet      : {old_data['pet_name']}")
    print(f"Category : {old_data['category']}")
    print(f"Service  : {old_data['service']}")
    print("--------------------------------")

    new_category = old_data["category"]
    new_service = old_data["service"]

    # ===== PILIH CATEGORY =====
    categories = sorted(set(p["category"] for p in services_data))
    print("\nSelect New Category (or enter 0 to keep current):")
    for i, cat in enumerate(categories, 1):
        print(f"[{i}] {cat}")
    # print("[0] Keep current category")

    while True:
        cat_choice = input("Select a new category number: ")

        if cat_choice == "0":
            break

        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            new_category = categories[int(cat_choice) - 1]
            break
        else:
            print("✖️  Invalid selection")

    # ===== PILIH SERVICE =====
    available_services = sorted(
        set(p["service"] for p in services_data if p["category"] == new_category)
    )
    print(f"\nSelect New Service for category '{new_category}':")
    for i, srv in enumerate(available_services, 1):
        print(f"[{i}] {srv}")

    while True:
        srv_choice = input("Select a new service number: ")

        if srv_choice == "0":
            if new_category != old_data["category"]:
                # Category diganti, service wajib diganti
                print("✖️  You must choose a new service for the new category!")
                continue
            break

        if srv_choice.isdigit() and 1 <= int(srv_choice) <= len(available_services):
            new_service = available_services[int(srv_choice) - 1]
            
            # Cek duplicate: sama persis dengan data lama
            if new_category == old_data["category"] and new_service == old_data["service"]:
                print("✖️  No changes detected. Please choose a different service or cancel.")
                continue  # loop lagi
            break

        else:
            print("✖️  Invalid selection")

    # ===== KONFIRMASI =====
    print("\n------- Confirm Changes -------")
    if new_category != old_data['category']:
        print(f"Category : {old_data['category']} -> {new_category}")
    else:
        print(f"Category : {old_data['category']}")

    if new_service != old_data['service']:
        print(f"Service  : {old_data['service']} -> {new_service}")
    else:
        print(f"Service  : {old_data['service']}")
    print("--------------------------------")

    while True:
        confirm = input("Confirm update? (y/n): ").lower()

        if confirm == "y":
            patient_records[idx]["category"] = new_category
            patient_records[idx]["service"] = new_service
            print("✔  Service successfully updated!\n")
            display_patient_records_table()
            return
        elif confirm == "n":
            print("✖️  Update cancelled.")
            return
        else:
            print("✖️  Please enter 'y' or 'n'")

            
# 3. UPDATE PATIENT STAFF
#----------------------------------
def update_patient_staff():
    print("\n" + "=" * 60)
    print("UPDATE ASSIGNED STAFF".center(60))
    print("=" * 60)
    print()
    # ===== PILIH DATA PASIEN =====
    while True:
        choice = input("Select patient number: ")
        print("[0] Cancel")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(patient_records):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    patient = patient_records[idx]
    category = patient['category']
    service = patient['service']
    owner = patient['owner_name']

    print(f"\nSelected Patient: {patient['pet_name']} ({category} - {service})")
    print(f"Owner: {owner}")

    # ===== FILTER STAFF SESUAI CATEGORY & SERVICE =====
    available_staff = [
        s for s in staff_data
        if s['category'] == category
        and s['service'] == service
        and s['status'] == "Available"
    ]

    if not available_staff:
        print("\n⚠️  All staff for this service are currently busy.")
        print("Please wait until a staff becomes available and try again later.\n")
        return
    
    # ===== TAMPILKAN LIST STAFF DENGAN STATUS =====
    print("\nSelect Staff:")
    for i, s in enumerate(available_staff, 1):
        print(f"[{i}] {s['name']} (Status: {s['status']})")

    while True:
        staff_choice = input("Choose staff number: ")
        if staff_choice.isdigit() and 1 <= int(staff_choice) <= len(available_staff):
            selected_staff = available_staff[int(staff_choice) - 1]
            if selected_staff['status'] != "Available":
                print(f"⚠️  {selected_staff['name']} is currently {selected_staff['status']}. Please choose another staff.")
                continue
            patient_records[idx]['staff'] = selected_staff['name']
            #  UPDATE STATUS STAFF MENJADI BUSY (jika sudah dipilih) 
            for s in staff_data:
                if s['name'] == selected_staff['name'] and s['category'] == category and s['service'] == service:
                    s['status'] = "Busy"
                    break

            print(f"✔  Staff updated successfully to {selected_staff['name']}!\n")
            display_patient_records_table()
            break
        else:
            print("✖️  Invalid selection")


# 3. UPDATE PATIENT STATUS
#----------------------------------
def update_patient_status():
    print("\n" + "=" * 60)
    print("UPDATE PATIENT STATUS".center(60))
    print("=" * 60)
    print()
    display_patient_records_table()
    while True:
        print("[0] Cancel")
        choice = input("Select patient number to update: ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(patient_records):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    patient = patient_records[idx]

    print(f"\nOwner : {patient['owner_name']}")
    print(f"Pet   : {patient['pet_name']}")
    print(f"Current Status : {patient['status']}")

    while True:
        new_status = input("Enter new status: ").strip().title()

        if any(char.isdigit() for char in new_status):
            print("✖️  Status cannot contain numbers!")
            continue

        if new_status == "":
            print("✖️  Status cannot be empty!")
            continue

        break

    while True:
        confirm = input(f"Change status to '{new_status}'? (y/n): ").lower()

        if confirm == "y":
            patient_records[idx]['status'] = new_status
            print("\n✔  Status successfully updated!\n")

            #  KEMBALIKAN STAFF KE AVAILABLE JIKA PASIEN SELESAI
            if new_status.lower() == "completed":
                staff_name = patient_records[idx]['staff']
                patient_category = patient_records[idx]['category']
                patient_service = patient_records[idx]['service']

                for s in staff_data:
                    if s['name'] == staff_name and s['category'] == patient_category and s['service'] == patient_service:
                        s['status'] = "Available"
                        break
            display_patient_records_table()
            break

        elif confirm == "n":
            print("✖️  Update cancelled.")
            break

        else:
            print("✖️  Invalid input! Please enter 'y' or 'n'.")


# 3. REMOVE PATIENT 
#----------------------------------
def remove_patient():
    print("\n" + "=" * 60)
    print("REMOVE PATIENT RECORD".center(60))
    print("=" * 60)
    print()
    display_patient_records_table()
    while True:
        print("[0] Cancel")
        choice = input("Select patient number to remove: ")

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(patient_records):
            idx = int(choice) - 1
            break
        else:
            print("✖️  Invalid selection")

    patient = patient_records[idx]

    print("\n------ Confirm Removal ------")
    print(f"Owner : {patient['owner_name']}")
    print(f"Pet   : {patient['pet_name']}")
    print(f"Service : {patient['service']}")
    print("----------------------------------")

    while True:
        confirm = input("Are you sure you want to remove this record? (y/n): ").lower()

        if confirm == "y":
            removed = patient_records.pop(idx)
            print(f"\n👋 Record for {removed['pet_name']} has been removed.\n")

            #  KEMBALIKAN STAFF KE AVAILABLE JIKA RECORD DIHAPUS
            staff_name = removed['staff']
            patient_category = removed['category']
            patient_service = removed['service']

            for s in staff_data:
                if s['name'] == staff_name and s['category'] == patient_category and s['service'] == patient_service:
                    s['status'] = "Available"
                    break

            display_patient_records_table()
            break

        elif confirm == "n":
            print("✖️  Removal cancelled.")
            break

        else:
            print("✖️  Invalid input! Please enter 'y' or 'n'.")


# ==========================================
# MAIN MENU (3) VIEW / MANAGE PATIENT RECORD
# ==========================================
def manage_patients(user):
    width = 60

    while True:
        display_patient_records_table()

        print("\n" + "="*width)
        print("PATIENT MANAGEMENT".center(width))
        print("="*width)

        # ================= ADMIN =================
        if user['role'] == "Clinic Administrator":
            print("[1] Update Patient Service")
            print("[2] Update Assigned Staff")
            print("[3] Update Status")
            print("[4] Remove Patient")
            print("[0] Back to main menu")

            choice = input("Select Option: ")

            if choice == "1":
                update_patient_service()
            elif choice == "2":
                update_patient_staff()
            elif choice == "3":
                update_patient_status()
            elif choice == "4":
                remove_patient()
            elif choice == "0":
                break
            else:
                print("\n✖️  Invalid selection!")

        # ================= STAFF =================
        else:
            print("🔹 View Only Mode - Admin Required to Manage Patients 🔹".center(width))
            input("Press Enter to go back...")
            break
