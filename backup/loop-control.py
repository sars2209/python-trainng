# break的簡易範例
# n=0
# while n<5:
#     if n==3: #當n=3時 執行break跳出迴圈到第八行的print(n)
#         break #breakg是強制跳出迴圈
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的n: ",n) #印出迴圈結束後的n

# continue的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: #x除以2餘數為零時(x為偶數時)
#         continue #contiune會忽略迴圈中的程式繼續跑下一個迴圈
#                 #所以上面兩行是當x為偶數時自動忽略print(x)和n+=1(忽略contiune後這輪for迴圈的其他命令)繼續下一輪for迴圈
#     print(x)
#     n+=1
# print("最後的n: ",n)

# else的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else: #else在迴圈中是在迴圈結束前執行以下命令
#     print(sum) #印出1+2+3+......+10

# 綜合範例:找出整數平方根 使用for迴圈
# 輸入9 得到3
# 輸入11 得到(沒有整數平方根)
n=int(input("輸入一個正整數: ")) #請使用者輸入並轉換成數字 因為原本是字串
for i in range(n+1): #變數i會從0一直測試到n(使用者輸入的數字) 使用n+1是因為這樣range才會帶入到n
    if i*i==n: #當i*i=n時,就找到了n的整數平方根
        print("整數平方根",i) #貼出正確答案的i
        break #注意!! 使用break結束迴圈是因為,break強制結束迴圈時不會執行else區塊的命令(因為else依然是在for迴圈中)
else: #如果n(使用者輸入的數字)沒有整數平方根的話執行else
    print("沒有整數平方根") #貼出沒有整數平方根

# 自己操作:找出整數平方根 使用while迴圈
x=input("請輸入一個正整數: ") #請使用者輸入數字(字串)
x=int(x) #將字串轉換成數字
y=0 #假定y是0 y是要尋找x的整數平方根的變數
while y<=x: #當y小於等於x是true時執行以下命令
#注意!while迴圈不可使用range(x+1)因為range是列表list
    y+=1 #執行y=y+1 讓數字越來越大來尋找x的整數平方根
    if y*y==x: #當y乘y等於x時 就找到x的整數平方根了!
        print("整數平方根: ",y) #貼出y(x的整數平方根)
        break #並且強制結束迴圈!(break強制結束迴圈不會執行else)
else: #當y小於等於x是false時(y大於x時) 執行以下命令(沒有整數平方根)
    print("沒有整數平方根") #貼出沒有整數平方根


