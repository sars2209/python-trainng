# 參數的預設資料

# def power(base,exp=0): #如果沒有給數字會跑不出來,所以給exp一個預設值0 假設沒有給exp的數值就自動給0
#     print(base**exp)
# power(exp=2,base=3)
# power(4)

# 使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

# 無限/不定 參數資料
#當資料數量不一定時可在變數前加星號,資料會以tuple列表儲存(有順序但不可動的列表)
#計算平均數
###以下非常重要!!
def avg(*ns): #定義avg為不定資料數量的列表
    sum=0 #總和計算
    for n in ns: #用for迴圈將n逐一帶入列表ns中
        sum+=n #並將其加總在回到迴圈
    print(sum/len(ns)) #貼出迴圈計算完後的總合並且除以資料的長度 ###別忘記! len是計算tuple或是list列表長度的工具
        #############len是取得列表中有幾個項目  #取得列表的長度 用法是len(列表)
avg(1,2,3,4,5,6,7,8,9,10)
avg(3,5,7,50,110)
avg(-100,50,60.5,550.545)
