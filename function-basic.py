# 定義函式
#注意!! 函式裡面的code沒有呼叫就不會執行 def只是定義而已
# def multiply(n1,n2): #定義multiply(n1,n2)是個函式
#     print(n1*n2) #注意!這是在函式中寫出結果 好壞取決於之後寫複雜程式 #執行函式時會貼出n1*n2
#     return n1*n2 #並且回傳數值10 注意!回傳值可以寫任何東西
#     # 注意!!! 沒有寫return的話 程式會自己在最後return 並且回傳值會是none
#     #如果有叫出函式還要再函式外部繼續操作資料的需求,使用回傳值計算結果比較好
# # 呼叫函式
# value=multiply(3,4) 
# print(value) #注意! 這是函式回傳後再印出結果 好壞取決於之後寫複雜程式
# 注意!!! 以上呼叫結果會是12 10,因為第一個12是呼叫進函式後,函式中的print(n1*n2)而貼出12
# 注意!!! 第二個10是multiply(3,4)的回傳值是10 (因為函是最後return的回傳值是10,讓multiply(3,4)=10)
# 沒有寫return的話就會是none
# multiply(5,5) #流程 呼叫函式,將資料傳進函式,印出n1*n2,跳出來
# multiply(50,22)


# 函式可用來做程式的包裝:同樣的邏輯可以重複利用
# def calculate(n):
#     sum=0
#     for n in range(1,n+1):
#         sum+=n
#     print(sum)

# calculate(100)
# calculate(10)

# def calculate(min,max):
#     sum=0
#     for x in range(min,max+1):
#         sum=sum+x
#     print(sum)

# min=int(input("請輸入數字1:"))
# max=int(input("請輸入數字2:"))

# calculate(min,max)

#自己實做看看
def cat(min,max): #定義cat為以下函式
    d=0
    for c in range(min,max+1): #不能打range(11) 因為0的0次方會是1 會多加一次1
        d=d+c**c
    return d  #回傳值是d
min=int(input("請輸入最小值: "))
max=int(input("請輸入最大值: "))
w=cat(min,max)
print(w) 
e=0
while e<=w:
    e+=1
    if e*e==w:
        print("有整數平方根",e)
        break
else:
    print("此數沒有整數平方根")
