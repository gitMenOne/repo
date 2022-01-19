msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0

#msg_new = ''.join(msg)
#msg_list = list(msg_new)
#print(msg_list)
for el in msg:
    if el.startswith('+'):
        print(index)
        msg.append('+')
        #     digit = int(el)
   #     print(digit)
    index = index + 1
print(msg)

