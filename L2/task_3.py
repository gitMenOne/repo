# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'] Необходимо его обработать —
# обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента
# списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# Решить задачу не создавая новый список (как говорят, in place)

msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
for el in msg:
    if el.startswith('+'):
        clear_el = el.replace("+", "")
        if clear_el.isdigit():
            if len(clear_el) < 2:
                clear_el = str(f"\"+0{clear_el}\"")
                msg[index] = clear_el
            else:
                clear_el = str(f"\"+{clear_el}\"")
                msg[index] = clear_el
    elif el.startswith('-'):
        clear_el = el.replace("-", "")
        if clear_el.isdigit():
            if len(clear_el) < 2:
                clear_el = str(f"\"-0{clear_el}\"")
                msg[index] = clear_el
            else:
                clear_el = str(f"\"-{clear_el}\"")
                msg[index] = clear_el
    if el.isdigit():
        if len(el) < 2:
            edit_el = str(f"\"0{el}\"")
            msg[index] = edit_el
        else:
            edit_el = str(f"\"{el}\"")
            msg[index] = edit_el
    index = index + 1
msg_new = ' '.join(msg)
print(msg_new)