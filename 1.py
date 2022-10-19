def perevod_chisla_v_sitemu_schislenia(sistema_schislenia, chislo):
    proverka_na_otricatelnye_chisla = False
    if chislo < 0:
        proverka_na_otricatelnye_chisla = True
        chislo *= -1
    otvet = ""
    while chislo > 0:
        otvet = str(chislo % sistema_schislenia) + otvet
        chislo //= sistema_schislenia
    if proverka_na_otricatelnye_chisla:
        print("-" + otvet)
    else:
        print(otvet)
chislo_vvedennoe_polzovatelem = int(input("Введите число: "))
sistema_schislenia = int(input("Введите целевую систему счисления: "))
while sistema_schislenia != 2 and sistema_schislenia !=8:
    print("Выберите двоичную или восьмиричную систему счисления")
    sistema_schislenia = int(input("Введите целевую систему счисления: "))
perevod_chisla_v_sitemu_schislenia(sistema_schislenia, chislo_vvedennoe_polzovatelem)
