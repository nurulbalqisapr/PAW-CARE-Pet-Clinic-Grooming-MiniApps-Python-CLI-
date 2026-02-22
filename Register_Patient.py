from Database import patient_records, services, staff_data

# =================================================
# MAIN MENU (1) REGISTER NEW PATIENT WITH SERVICE 
# =================================================
from datetime import datetime

def register_patient():
    width = 60
    print("\n" + "=" * width)
    print("REGISTER OWNER AND PETS".center(width))
    print("=" * width)

    # ===== INPUT OWNER INFO =====
    while True:
        owner_name = input("Owner Name     : ").title()
        if owner_name.replace(" ", "").isalpha():  
            break
        print("✖️  Owner name must contain letters only!")

    while True:
        owner_contact = input("Owner Contact  : ")
        if owner_contact.isdigit() and 9 <= len(owner_contact) <= 13:
            break
        print("✖️  Contact must be numeric and 9-13 digits!")

    # ===== INPUT DATE =====
    while True:
        date_input = input("Enter Date (YYYY-MM-DD) or leave empty for today: ")
        if not date_input:
            date_input = datetime.today().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break
        except:
            print("✖️  Invalid date format! Use YYYY-MM-DD.")

    owner_data = {
        "owner_name": owner_name,
        "owner_contact": owner_contact,
        "pets": []
    }

    add_more_pets = True
    while add_more_pets:
        # ===== INPUT PET INFO =====
        while True:
            pet_name = input("Pet Name       : ").title()
            if pet_name.replace(" ", "").isalpha():  
                break
            print("✖️  Pet name must contain letters only!")

        while True:
            pet_type = input("Pet Type (Dog/Cat/Other): ").title()
            if pet_type.replace(" ", "").isalpha():  
                break
            print("✖️  Pet Type must contain letters only!")

        while True:
            try:
                age_months = int(input("Pet Age (months) : "))
                if age_months >= 0:
                    pet_age = round(age_months / 12, 2)
                    break
                else:
                    print("✖️  Age must be >= 0!")
            except:
                print("✖️  Invalid input! Enter integer number only.")

        # ===== PILIH CATEGORY =====
        selected_categories = []
        while True:
            print("\nService Categories (you can select multiple, comma separated):")
            for idx, cat in enumerate(services.keys(), start=1):
                print(f"[{idx}] {cat}")
            cat_choices = input("Select Category (1-3, comma separated): ")
            choices = [c.strip() for c in cat_choices.split(",")]
            if all(ch in ["1","2","3"] for ch in choices):
                selected_categories = [list(services.keys())[int(ch)-1] for ch in choices]
                break
            print("✖️  Invalid selection. Choose 1-3 (comma separated)")

        # ===== PILIH SERVICE & STAFF UNTUK MASING-MASING CATEGORY =====
        pet_services = {}
        assigned_staff = {}

        for category in selected_categories:
            print(f"\nAvailable Services in {category}:")
            for idx, svc in enumerate(services[category], start=1):
                print(f"[{idx}] {svc}")

            # ===== PILIH SERVICE =====
            while True:
                svc_choice = input(f"Select Service (1-{len(services[category])}): ")
                if svc_choice.isdigit() and 1 <= int(svc_choice) <= len(services[category]):
                    pet_services[category] = services[category][int(svc_choice)-1]
                    break
                print("✖️  Invalid selection")

            # ===== LIST STAFF SESUAI CATEGORY & SERVICE =====
            available_staff_list = [
                s for s in staff_data
                if s['category'] == category
                and s['service'] == pet_services[category]
                and s['status'] == "Available"
            ]

            if available_staff_list:
                print(f"\nAvailable Staff for {category} - {pet_services[category]}:")
                for idx, s in enumerate(available_staff_list, start=1):
                    print(f"[{idx}] {s['name']} ({s['status']})")

                # ===== USER PILIH STAFF =====
                while True:
                    staff_choice = input(f"Select staff (1-{len(available_staff_list)}): ")
                    if staff_choice.isdigit() and 1 <= int(staff_choice) <= len(available_staff_list):
                        selected_staff = available_staff_list[int(staff_choice)-1]['name']
                        assigned_staff[category] = selected_staff
                        # Set staff jadi Busy
                        for s in staff_data:
                            if s['name'] == selected_staff and s['category'] == category and s['service'] == pet_services[category]:
                                s['status'] = "Busy"
                                break
                        break
                    print("✖️  Invalid selection")
            else:
                assigned_staff[category] = "No available staff"
                print(f"✖️  No available staff for {category} - {pet_services[category]}")

        # ===== ARRIVAL TYPE =====
        print("\nArrival Type:")
        print("[1] Reservation")
        print("[2] Walk-In / Direct Arrival")
        while True:
            arrival_choice = input("Select (1-2): ")
            if arrival_choice == "1":
                arrival_type = "Reservation"
                status = "Check-In"
                break
            elif arrival_choice == "2":
                arrival_type = "Direct Arrival"
                status = "Check-In"
                break
            else:
                print("✖️  Invalid selection. Please choose 1 or 2")

        # ===== SIMPAN DATA HEWAN =====
        pet_data = {
            "pet_name": pet_name,
            "pet_type": pet_type,
            "pet_age": pet_age,
            "categories_services": pet_services,
            "assigned_staff": assigned_staff,
            "arrival_type": arrival_type,
            "status": status
        }
        owner_data["pets"].append(pet_data)

        # ===== SIMPAN KE patient_records SESUAI URUTAN CATEGORY =====
        category_order = ["Health Care", "Grooming", "Pet Hotel"]
        for category, svc in pet_services.items():
            new_record = {
                "no": len(patient_records)+1,
                "date": date_input,
                "owner_name": owner_name,
                "pet_name": pet_name,
                "category": category,
                "service": svc,
                "staff": assigned_staff.get(category, ""),
                "status": status
            }

            insert_idx = None
            for i, rec in enumerate(patient_records):
                if category_order.index(rec["category"]) > category_order.index(category):
                    insert_idx = i
                    break

            if insert_idx is None:
                patient_records.append(new_record)
            else:
                patient_records.insert(insert_idx, new_record)

        # ===== UPDATE NO URUTAN =====
        for idx, rec in enumerate(patient_records, start=1):
            rec["no"] = idx

        # ===== TAMBAH HEWAN BARU? =====
        while True:
            more = input("Add another pet for this owner? (Y/N): ").lower()
            if more == "y":
                add_more_pets = True
                break
            elif more == "n":
                add_more_pets = False
                break
            else:
                print("✖️  Invalid input! Please enter Y or N.")

    print("\nOwner and pets successfully registered!\n")

    # ===== TAMPILKAN RINGKASAN =====
    print("\n" + "="*width)
    print("OWNER & PETS SUMMARY".center(width))
    print("="*width)
    print(f"Owner   : {owner_name}")
    print(f"Contact : {owner_contact}")
    print("="*width)

    for idx, pet in enumerate(owner_data["pets"], start=1):
        years = int(pet['pet_age'])
        months = int(round((pet['pet_age'] - years) * 12))

        if years > 0 and months > 0:
            display_age = f"{years} year{'s' if years != 1 else ''} {months} month{'s' if months != 1 else ''}"
        elif years > 0:
            display_age = f"{years} year{'s' if years != 1 else ''}"
        else:
            display_age = f"{months} month{'s' if months != 1 else ''}"

        print(f"\n┌{'─'* (width-2)}┐")
        print(f"│ Pet {idx}: {pet['pet_name']} ({pet['pet_type']}, {display_age})".ljust(width-1) + "│")
        print(f"├{'─'* (width-2)}┤")
        print(f"│ {'Category':<15} | {'Service':<15} | {'Staff':<20}".ljust(width-1) + "│")
        print(f"├{'─'* (width-2)}┤")

        for cat, svc in pet['categories_services'].items():
            staff_name = pet['assigned_staff'].get(cat, "")
            display_staff = staff_name if staff_name else "No available staff"
            print(f"│ {cat:<15} | {svc:<15} | {display_staff:<20}".ljust(width-1) + "│")
            print(f"├{'─'* (width-2)}┤")

        print(f"│ Arrival Type : {pet['arrival_type']}".ljust(width-1) + "│")
        print(f"│ Status       : {pet['status']}".ljust(width-1) + "│")
        print(f"└{'─'* (width-2)}┘")
