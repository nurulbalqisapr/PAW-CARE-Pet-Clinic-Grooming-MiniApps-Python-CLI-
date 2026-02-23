#==============================================
# CAPSTONE PROJECT | MODULE 1
# Author: NURUL BALQIS APRIANY
# Purwadhika / JCDSOHAM - 006
# Mini Application Pet Clinic & Grooming 
#==============================================


# import function from Menu_Auth.py
from Menu_Auth import show_menu_auth, create_acc, signin

# import function from RegisterPatient.py
from Register_Patient import register_patient

# import function from Service_Management.py
from Service_Management import manage_services  

# import function from Patient_Management.py
from Patient_Management import manage_patients

# import function from Payment.py
from Payment import checkout_payment

# import function from Staff_Management.py
from Staff_Management import manage_staff_data

# ==========================================
# MAIN MENU ADMIN
# ==========================================
def main_menu_admin(user):
    while True:
        width = 60
        print("\n" + "=" * width)
        print("PAW-CARE: PET CLINIC & GROOMING".center(width))
        print("Welcome to PAW-CARE App".center(width)) 
        print("=" * width)
        print("[1] Register New Patient")
        print("[2] View / Manage PAW-CARE: Services")
        print("[3] View / Manage Patient Records")
        print("[4] View / Manage Staff Data")
        print("[5] Check-Out & Payment")
        print("[0] Logout")
        print("=" * width)

        choice = input("Select Menu (0-5): ")

        if choice == "0":
            print("\nLogging out...")
            break
        elif choice == "1": register_patient()
        elif choice == "2": manage_services(user)
        elif choice == "3": manage_patients(user)
        elif choice == "4": manage_staff_data(user)
        elif choice == "5": checkout_payment()
        else:
            print("✖️  Invalid selection! Please choose 0-5.")

# ==========================================
# MAIN MENU STAFF
# ==========================================
def main_menu_staff(user):
    while True:
        width = 60
        print("\n" + "=" * width)
        print("PAW-CARE: PET CLINIC & GROOMING".center(width))
        print(f"Logged in as: {user['name']} ({user['role']})".center(width))
        print("=" * width)
        print("[1] View PAW-CARE: Services")
        print("[2] View Patient Records")
        print("[3] View Staff Data")
        print("[4] Check-Out & Payment")
        print("[0] Logout")
        print("=" * width)

        choice = input("Select Menu (0-4): ")

        if choice == "0":
            print("\nLogging out...")
            break
        elif choice == "1": manage_services(user)
        elif choice == "2": manage_patients(user)
        elif choice == "3": manage_staff_data(user)
        elif choice == "4": checkout_payment()
        else:
            print("✖️  Invalid selection! Please choose 0-4.")

# ==========================================
# SYSTEM MENU
# ==========================================
def menu():
    while True:
        show_menu_auth()
        pilih = input("Select Menu (1-3): ")

        if pilih == "1":
            create_acc()
        elif pilih == "2":
            user_login = signin()
            if user_login:
                if user_login["role"] == "Clinic Administrator":
                    main_menu_admin(user_login)
                else:
                    main_menu_staff(user_login)
        elif pilih == "3":
            print("System Closed")
            break
        else:
            print("✖️  Invalid selection. Please choose 1-3")

# ==========================================
# RUN
# ==========================================
menu()
