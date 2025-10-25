display_cost = int(input('Цена монитора: '))
keyboard_cost = int(input('Цена клавиатуры: '))
mouse_cost =int(input('Цена мыши: '))
pc_cost =int(input('Цена блока: '))

print(f'Цена 3 пк: {(display_cost+keyboard_cost+mouse_cost+pc_cost)*3}')