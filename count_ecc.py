from bsgs import bsgs

from variable import a,b,p

def count_ecc(a, b, p):
    ecc_Point = []
    count = 0
    for i in range(p):
        mod_x = (i ** 3 + a * i + b) % p

        for j in range(int(p)):
            if (j**2)%p == mod_x:
                count += 1
                # if j == 0:
                #     ecc_Point.append([i, j])
                #     break
                # else:
                #     ecc_Point.append([i, j])
                #     ecc_Point.append([i, p - j])
                # break
    return count+1

# ecc_T = []
# ecc_test = []
# for a in range(-p, p):
#     for b in range(-p, p):
#         if 4*a**3 + 27*b**2 != 0:
#             test = count_ecc(a,b,p) #tổng số điểm của ecc
#             ecc_test.append(test) #thêm số điểm và các thông số a,b vào mảng
#             ecc_T.append([test,a,b])

