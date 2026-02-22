# =================================================
# MAIN MENU (5) PAYMENT
# =================================================

from Database import patient_records, services_data
from datetime import datetime
import random

def checkout_payment():
    # ===== FILTER RECORDS YANG STATUS COMPLETED =====
    completed_records = [p for p in patient_records if p['status'] == "Completed"]

    # ===== DAPATKAN LIST OWNER UNIQUE =====
    owners = sorted(list(set(p['owner_name'] for p in completed_records)))
    
    width = 135

    # ===== TAMPILKAN TABEL RECORD COMPLETED =====
    print("\n" + "="*width)
    print("PAW-CARE: PET CLINIC & GROOMING".center(width))
    print("Completed Patient Records".center(width))
    print("="*width)
    
    if not completed_records:
        alert_msg = "✖️  No completed patient records available for checkout!  ✖️"
        print("\n" + alert_msg.center(width) + "\n")
    else:
        # header tabel
        print(f"┌{'─'*4}┬{'─'*12}┬{'─'*18}┬{'─'*18}┬{'─'*18}┬{'─'*20}┬{'─'*20}┬{'─'*14}┐")
        print(f"│ {'No':<2} │ {'Date':<10} │ {'Owner Name':<16} │ {'Pet Name':<16} │ {'Category':<16} │ {'Service':<18} │ {'Staff':<18} │ {'Status':<12} │")
        print(f"├{'─'*4}┼{'─'*12}┼{'─'*18}┼{'─'*18}┼{'─'*18}┼{'─'*20}┼{'─'*20}┼{'─'*14}┤")

        # Isi tabel
        for idx, p in enumerate(completed_records, start=1):
            print(f"│ {idx:<2} │ {p['date']:<10} │ {p['owner_name']:<16} │ {p['pet_name']:<16} │ {p['category']:<16} │ {p['service']:<18} │ {p['staff']:<18} │ {p['status']:<12} │")
            
            # Garis bawah tiap baris, kecuali baris terakhir
            if idx != len(completed_records):
                print(f"├{'─'*4}┼{'─'*12}┼{'─'*18}┼{'─'*18}┼{'─'*18}┼{'─'*20}┼{'─'*20}┼{'─'*14}┤")
            else:
                print(f"└{'─'*4}┴{'─'*12}┴{'─'*18}┴{'─'*18}┴{'─'*18}┴{'─'*20}┴{'─'*20}┴{'─'*14}┘")

    

    # ===== PILIH OWNER BERDASARKAN NOMOR =====
    print("\nSelect patient for checkout:")
    for idx, o in enumerate(owners, start=1):
        print(f"[{idx}] {o}")

    while True:
        choice = input(f"Select owner (1-{len(owners)}) or 0 to cancel: ")
        if choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(owners):
            owner_name = owners[int(choice)-1]
            break
        print("❌ Invalid selection")

    # ===== FILTER RECORDS MILIK OWNER =====
    owner_records = [p for p in completed_records if p['owner_name'] == owner_name]

    # ===== CETAK STRUK =====
    transaction_id = f"TX{random.randint(1000,9999)}"
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    width = 120
    print("\n" + "="*width)
    print("PAW-CARE PET CLINIC & GROOMING".center(width))
    print("="*width)
    print(f"Date          : {today}")
    print(f"Transaction ID: {transaction_id}")
    print(f"Owner Name    : {owner_name}")
    print("-"*width)

    # header tabel struk
    print(f"┌{'─'*4}┬{'─'*18}┬{'─'*18}┬{'─'*25}┬{'─'*20}┬{'─'*18}┐")
    print(f"│ {'No':<2} │ {'Pet Name':<16} │ {'Category':<16} │ {'Service':<23} │ {'Staff':<18} │ {'Price':<16} │")
    print(f"├{'─'*4}┼{'─'*18}┼{'─'*18}┼{'─'*25}┼{'─'*20}┼{'─'*18}┤")

    # hitung total
    total_price = 0
    for idx, p in enumerate(owner_records, start=1):
        price = next((s['price'] for s in services_data if s['category']==p['category'] and p['service']==s['service']), 0)
        total_price += price
        print(f"│ {idx:<2} │ {p['pet_name']:<16} │ {p['category']:<16} │ {p['service']:<23} │ {p['staff']:<18} │ Rp{price:<14,} │")
        # update status ke Completed (meski sudah Completed)
        p['status'] = "Completed"

    print(f"├{'─'*4}┴{'─'*18}┴{'─'*18}┴{'─'*25}┴{'─'*20}┴{'─'*18}┤")
    print(f"│ {'TOTAL'.center(87)} │ Rp{total_price:<14,} │")
    print(f"└{'─'*89}┴{'─'*18}┘")
    print("="*width)
    print("Thank you for visiting PAW-CARE!".center(width))
    print("="*width)