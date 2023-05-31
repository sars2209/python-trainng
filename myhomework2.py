#1*2*3*4....*10
# y=1 #y不能從0開始 因為會從0開始 0乘任何數都是0
# x=1
# while x<=10: 
#     y=x*y
#     x+=1
# print(y)

# n=1
# m=1
# for n in range(1,11): #不能寫range(11)因為會從0開始 0乘任何數都是0
#     m=n*m
# print(m)

# #1^1+2^2+3^3....10^10
# a=0
# b=1 #b不能從0開始 因為0的0次方會是1 會多加一次1
# while b<=10:
#     a=a+b**b
#     b+=1
# print(a)

# d=0
# for c in range(1,11): #不能打range(11) 因為0的0次方會是1 會多加一次1
#     d=d+c**c
# print(d)

# 奇偶數辨別
# x=int(input("輸入一個數字"))
# if x%2==0:
#     print("偶數")
# else:
#     print("奇數")

# 填字遊戲
# x=input("輸入主詞")
# y=input("輸入地點")
# z=input("輸入形容詞")
# n=input("輸入動詞")
# print(x,"在",y,z,"的",n,"嘿嘿")

# 計算字數
# x=input("輸入隨意一段話來抒發心情吧!")
# y=len(x)
# print("你使用了",y,"句話來抒發心情")

#尋找因數
#while迴圈版本 解決
# x=int(input("輸入一個數字"))
# n=0
# while n<=x:
#     n+=1
#     if x%n==0:
#         print("因數有",n)

#for迴圈版本 解決
# y=int(input("請輸入一個數字"))
# for i in range(1,y+1):
#     if y%i==0:
#         print("因數有",i)

# 尋找兩個數之間的最小公倍數
# for迴圈版本 解決
x=int(input("請輸入數字一: "))
y=int(input("請輸入數字二: "))
z=x*y
for i in range(1,z+1):
    if i%x==0 and i%y==0:   
        print("最小公倍數:",i)
        break

# while迴圈版本 解決
x=int(input("請輸入數字一: "))
y=int(input("請輸入數字二: "))
n=0
z=x*y
while n<=z:
    n+=1
    if n%x==0 and n%y==0:
        print("最小公倍數: ",n)
        break

# 尋找兩個數之間的最大公因數
# for迴圈版本
x=int(input("輸入數字一: "))
y=int(input("輸入數字二: "))
z=x+y
for i in range(z,0,-1): #要從數字大檢查到數字小才找的到最大公因數
    if x%i==0 and y%i==0:
        print("最大公因數:",i)
        break

# while迴圈版本
x=int(input("輸入數字一: "))
y=int(input("輸入數字二: "))
z=x+y
n=1
while n<=z:
    z-=1 #要從數字大檢查到數字小才找的到最大公因數
    if x%z==0 and y%z==0:
        print("最大公因數:",z)
        break




