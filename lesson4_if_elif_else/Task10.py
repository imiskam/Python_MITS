armor_color = input("Enter the armor color: ").capitalize()  # red, yellow, black
shield_color = input("Enter the shield color: ").capitalize()  # red, yellow, black
color_list = ("Red", "Yellow", "Black")

# задать предикат, в котором цвет доспехов и щита будут сравниваться с введенными пользователем
is_equipment = armor_color != "Red" and armor_color in color_list \
               and shield_color == "Black" and shield_color in color_list  # доп. проверки на наличие нужного цвета в списке
# проверка предиката
if is_equipment:
    print(is_equipment)
else:
    if armor_color not in color_list or shield_color not in color_list:
        print(f"The {armor_color} or {shield_color} color doesn't exist")
    print(False)
