#數字運算
# x=3+6
# x=x+1 #等號後方要先看 所以會是7+1=8 就是變數加一
# x+=1 # x+=1是x=x+1的簡寫 結果會是一模一樣
# x-=1 # x-=1是x=x-1的簡寫 她是變數減一
# x*=1 # 以此類推 變數x乘一的簡寫 所有的運算都可以套用一樣意思  
# print(x)
# y=3-6
# print(y)
# z=3*6    #一個*代表乘法
# print(z)
# w=3/7    #一個除號會是小數除法 如果除出來的結果會是除不盡他會寫上來
# print(w)
# e=3//7   #兩個除號會是整數除法 如果除出來的結果有小數 它會自動省略只保留整數部分
# print(e)
# q=3**6   #兩個*代表次方 q是3的6次方的意思
# print(q)
# r=2**0.5 #開根號的話就是某數的0.5次方 也就是兩個*後打0.5
# print(r)
# d=7%3    #%代表取餘數 7除3會餘1 所以d等於1
# print(d)
#字串運算
# 字串使用單引號或是雙引號都可以 
# 字串會裡面的每個字元編號(索引)  從 0 開始算起
s="hello wo\"rld" #如果在字串中要使用到引號的話要在前面加上 \ 來讓程式知道這個引號是字
print(s)
t="hello" "world" #字串的串接使用 + 或是空白鍵 字串就會接在一起
print(t)
y="hello\nworld"  #\n代表換行
print(y)
u="""hello

world"""          #python換行也可以一次打三個引號
print(u)
i="hello"*3+"world" #pythond字串如果想要重複可以加上乘法
print(i)
# 字串會裡面的每個字元編號(索引) 注意!! 字元從 0 開始算起
print(i[0]) #要貼出字串中的其中一個字元要使用中括號中間加上第幾個字元 記得字元從0開始的
print(i[8]) #貼出字串i的第八個字元
print(i[1:4]) #貼出字串i從第1到第4個的字元 注意! 包含開頭不包含結尾
print(i[1: ]) #貼出字串i從第1到後面所有的字元
print(i[ :9]) #貼出字串i第9個字元前面所有的字元 不包含第9個