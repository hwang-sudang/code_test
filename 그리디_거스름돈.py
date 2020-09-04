# 그리디 알고리즘 1번 거스름돈
# 1000엔 지불
# 잔돈으로 줄 수 있는 것 : 500, 50, 10, 5, 1

price = int(input()) # 물건의 가격
money = 1000

coins = [500,100,50,10,5,1] # 동전 종류
take = money-price
temp = [] # 동전 갯수

for i in coins:
    temp.append(take//i)
    take -= i*(take//i)


print(sum(temp))        
    