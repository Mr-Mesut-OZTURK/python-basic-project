"""
student module
"""


def student(valid):
    print(f"Sayın {valid['name']} hoşgeldiniz...")

    while True:
        print("""
                1 - Kullanıcı kayıt
                2 - ayarlar
                3 - çıkış
        """)


        komut = input("Ne yapmak istersiniz : ")

        if komut == "1":
            print("Kullanıcı kayıt")
        elif komut == "2":
            print("Ayarlar")
        elif komut == "3":
            break
        else:
            print("Hatalı seçim!...")
            print("*" * 50)