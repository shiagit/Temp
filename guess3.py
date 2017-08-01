
import random
ans = input('輸入數字：')
wrong = []
while True:
    rnum = str(random.randrange(1000))
    if rnum in wrong:
        continue
    if rnum == ans:
        print('輸入數為'+ rnum)
        break
    else:
        print(rnum)
        wrong.append(rnum)
    continue
