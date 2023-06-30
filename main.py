import subprocess

# Qabul qilingan wifi SSID nomini yozing:
ssid = input("WiFi nomini yozing: ")

# So'rovnoma natijalarini bitta o'zgaruvchida saqlaymiz
output = subprocess.check_output(["netsh", "wlan", "show", "profiles", "key=clear"])

# SSID nomini aniqlash
profiles = [i.split(":")[1][1:-1] for i in output.decode("utf-8").split("\n") if "All User Profile" in i]

# Kerakli SSID profili bo'lmaganda
if ssid not in profiles:
    print("Kechirasiz, bunday SSID mavjud emas!")
else:
    # Profil ma'lumotlarini olish
    output = subprocess.check_output(["netsh", "wlan", "show", "profile", ssid, "key=clear"])
    output = output.decode("utf-8").split("\n")
    
    # Parol ni topish
    password = [i.split(":")[1][1:-1] for i in output if "Key Content" in i]
    
    # Parol topilmasa
    if len(password) == 0:
        print("Kechirasiz, belgilangan SSID uchun parol topilmadi!")
    else:
        print(f"SSID: {ssid}, Parol: {password[0]}") 
