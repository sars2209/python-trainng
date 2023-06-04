# 註解 我的第一個程式碼
# 撰寫程式:副檔名用 py
# 執行程式:python 檔案名稱
print("Hello Python")

# 個資判斷
# 姓名
x=input("請輸入姓名")
# 電話
y=input("請輸入電話號碼")
n=len(y)
e=1
while e==1:
    if n==10 and y.startswith("09") and y.isdigit():
        break
    else:
        print("輸入錯誤,請再輸入一次")
        del y
        y=input("請再次輸入電話號碼")
        n=len(y)
# 生日
print("Hello Python")
print("Hello Python")