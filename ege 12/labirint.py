def chikl(i, k):
    nachalo = i, k
    if k != 6:
        while ')' not in lab[i][k] and '(' not in lab[i][k + 1]:
            lab[i][k + 1], lab[i][k] = '1' + lab[i][k + 1][1:], '0' + lab[i][k][1:]
            k += 1
    if i != 0:
        while '-' not in lab[i-1][k] and '_' not in lab[i][k]:
            lab[i - 1][k], lab[i][k] = '1' + lab[i - 1][k][1:], '0' + lab[i][k][1:]
            i -= 1
    if k != 0:
        while '(' not in lab[i][k] and ')' not in lab[i][k - 1]:
            lab[i][k - 1], lab[i][k] = '1' + lab[i][k - 1][1:], '0' + lab[i][k][1:]
            k -= 1
    if i != 6:
        while '_' not in lab[i][k] and '-' not in lab[i + 1][k]:
            lab[i + 1][k], lab[i][k] = '1' + lab[i + 1][k][1:], '0' + lab[i][k][1:]
            i += 1
    if nachalo == (i, k):
        lab[i][k] = '0' + lab[i][k][1:]
        return 1
    else:
        lab[i][k] = '0' + lab[i][k][1:]
        return 0


lab = [
    ['0(-_','0-','0-)','(0-','0-','0)-'],
    ['0(-','0_','0','0','0)','(0)'],
    ['0(','0-','0_','0','0','0)'],
    ['0(','0','0-','0_','0','0_)'],
    ['0(','0)','(0','0-','0_','0-)'],
    ['0(_)','(0_','0_','0_','0_-','0)_'],
       ]
pyt = 0
for i in range(6):
    for k in range(len(lab[i])):
        lab[i][k] = '1' + lab[i][k][1:]
        pyt += chikl(i, k)

print(pyt)



# lab = [
#     ['0(-','0-','0-','0-','0-','0)-'],
#     ['0(','0','0','0','0','0)'],
#     ['0(','0','0','0','0','0)'],
#     ['0(','0','0','0','0','0)'],
#     ['0(','0','0','0','0','0)'],
#     ['0(_','0_','0_','0_','0_','0)_'],
#        ]
#     if k != 0:
#         while '(' not in lab[i][k] and ')' not in lab[i][k - 1]:
#             lab[i][k - 1], lab[i][k] = '1' + lab[i][k - 1][1:], '0' + lab[i][k][1:]
#             k -= 1
#     if i != 6:
#         while '_' not in lab[i][k] and '-' not in lab[i + 1][k]:
#             lab[i + 1][k], lab[i][k] = '1' + lab[i + 1][k][1:], '0' + lab[i][k][1:]
#             i += 1
#     if k != 6:
#         while ')' not in lab[i][k] and '(' not in lab[i][k + 1]:
#             lab[i][k + 1], lab[i][k] = '1' + lab[i][k + 1][1:], '0' + lab[i][k][1:]
#             k += 1
#     if i != 0:
#         while '-' not in lab[i-1][k] and '_' not in lab[i][k]:
#             lab[i - 1][k], lab[i][k] = '1' + lab[i - 1][k][1:], '0' + lab[i][k][1:]
#             i -= 1