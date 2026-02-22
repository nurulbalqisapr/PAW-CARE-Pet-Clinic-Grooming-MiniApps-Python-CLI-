from Database import admin

# ==========================================
# MENU AUTH
# ==========================================
def show_menu_auth():
    width = 60
    print("\n" + "=" * width)
    print("PAW-CARE CLINIC & GROOMING SYSTEM".center(width))
    print("Staff Access".center(width))
    print("=" * width)
    print("1. Create Account")
    print("2. Staff Sign-In")
    print("3. Exit System")
    print("=" * width)

# ==========================================
# INPUT USERID
# ==========================================
def input_userid():
    while True:
        userid = input("User ID    : ")
        if len(userid) < 6 or len(userid) > 20:
            print("User ID must be 6-20 characters")
            continue

        if not userid.isalnum():
            print("User ID must contain only letters and numbers")
            continue

        if not userid.islower():
            print("User ID must be all lowercase letters")
            continue

        if any(u["userid"] == userid for u in admin):
            print("User ID already exists")
            continue
        return userid

# ==========================================
# INPUT PASSWORD
# ==========================================
def input_password():
    while True:
        password = input("Password   : ")
        if len(password) < 8:
            print("Password minimum 8 characters")
            continue
        upper = any(c.isupper() for c in password)
        lower = any(c.islower() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in "@#$%.,/" for c in password)
        if upper and lower and digit and special:
            return password
        else:
            print("Password must contain upper, lower, number, and special character ('@#$%.,/')")

# ==========================================
# CREATE ACCOUNT (ALL ROLES)
# ==========================================
def create_acc():
    width = 60
    print("\n" + "=" * width)
    print("CREATE NEW ACCOUNT".center(width))
    print("=" * width)

    userid = input_userid()
    password = input_password()

    while True:
        name = input("Full Name  : ")
        if name.replace(" ", "").isalpha():  
            break
        print("✖️ Name must contain letters only")

    # Pilih role
    roles = ["Clinic Administrator", "Staff"]
    print("\nSelect Role:")
    for idx, r in enumerate(roles, start=1):
        print(f"[{idx}] {r}")
    while True:
        role_choice = input("Select Role (1-2): ")
        if role_choice in ["1", "2"]:
            role = roles[int(role_choice)-1]
            break
        print("✖️  Invalid selection. Choose 1 or 2")

    print("-" * width)
    print(f"Role Assigned : {role}")
    print("-" * width)

    while True:
        save = input("Save Data? (Y/N): ").lower()
        if save == "y":
            admin.append({
                "userid": userid,
                "password": password,
                "name": name,
                "role": role
            })
            print("\n✔️    Account successfully created")
            break
        elif save == "n":
            print("\n✖️    Account not saved")
            break
        else:
            print("✖️  Invalid input! Please enter Y or N.")

    print("=" * width)

# ==========================================
# SIGN IN
# ==========================================
def signin():
    attempts = 0
    width = 60
    while attempts < 5:
        print("\n" + "=" * width)
        print("STAFF SIGN-IN".center(width))
        print("=" * width)

        userid_input = input("User ID    : ")
        password_input = input("Password   : ")

        user_data = next((u for u in admin if u["userid"] == userid_input), None)

        if not user_data:
            attempts += 1
            print(f"✖️   User ID not registered ({attempts}/5 attempts)")
            continue
        if user_data["password"] != password_input:
            attempts += 1
            print(f"✖️   Incorrect password ({attempts}/5 attempts)")
            continue
        
        print("\n✓ You're now signed in")
        print(f"Hi {user_data['name']} — {user_data['role']}")
        return user_data  # kembalikan seluruh dict

    print("\n✖️   System Locked. Maximum login attempts reached.")
    return None
