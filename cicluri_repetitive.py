# i=0
# while i<=3:
#     print(f'valoarea curenta a contorului este {i}')
#     i=i+1
#     print(f'valoarea dupa incrementare a contorului este {i}')
# else:
#     print('testul a luat sfarsit')


# for i in range(40):
#     print(i) #printeaza 40 de numere, nu pana la numarul 40
#
# for i in range(1, 102):
#     print(f'acesta este dalmatioanul cu numarul {i}')
#
# for i in range(0, 101, 2):
#     print(i)

# for i in reversed(range(100, 0, -2)):
#     print(i)

culori=['alb', 'galben', 'rosu', 'violet', 'alb']
for culoare in culori:
    print(f'culoarea curenta este {culoare}')

print(f'lista initiala este {culori}')
for i in range(len(culori)):
    if culori[i]=='alb':
        culori[i]='mov'
        print(f'lista curenta este {culori}')
print(f'lista finala este {culori}')



for culoare in culori:
    if culoare=='mov':
        index=culori.index('mov')
        culori[index]='magenta'
        print(f'culoarea curenta este {culori}')
        # print( f'culoarea curenta este {culori[index]}')
print(f'lista finala modificata este {culori}')
print(culori[index])


# print('---------break----------')
# for i in range(len(culori)):
#     if culori[i]=='magenta':
#         culori[i]='purpuriu'
#         print(f'lista curenta este {culori}')
#         break
# print(f'lista finala este {culori}')

print('---------continue----------')
print(culori)
for i in range(len(culori)):
    if culori[i]=='magenta':
        culori[i]='purpuriu'
        print(f'lista curenta este {culori}')
        continue
print(f'lista finala este {culori}')

note=[10, 4, 6, 7, 4, 8, 3]
note_premiante=[]
for nota in note:
    if nota <=4:
        continue
    note_premiante.append(nota)
print(f'lista note premiante este {note_premiante}')