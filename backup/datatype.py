#資料:程式中的基本單位
#數字
123
1.23
#字串
"測試中文"
"hello world"
#布林值
True
False
#有順序,可動的列表 List
[1,2,3]
["hello","world"]
#有順序,不可動的列表 Tuple
(1,2,3)
("Hello World")
# 集合 Set
# 集合沒有順序
{1,2,3}
{"Hello","World"}
#字典 Dictionary
#在大引號中用:來代表apple對應到蘋果 data對應到資料
{"apple":"蘋果","data":"資料"}

#變數:用來儲存資料的自訂名稱
#變數名稱=資料
data=3
x=4
#print(資料)
print(3)
print(x)
print(data)
print(["hello","world"])
#變數有彈性 可以任意更改
x=True           #取代舊資料 從3變成True 這是布林值代表正確或是錯誤
print(x)
x="hello python" #雙引號是字串 裡面可以放任何種類的字,或是數字
print(x)
x={2,5,7}        #大括號是集合 set 集合裡面沒有順序
print(x)
x=[2,4,6]        #中括號是有順序,可動的列表 list
print(x)
x=(5,6,7)        #小括號是有順序但不可動的列表 tuple
print(x)