# 集合的運算
#s1={1,2,3}
#x=[1,2,3,[4,5,6]]
#print(3 in x[3]) #如果要判斷巢狀列表是否有指定的資料,要注意指定是第幾項
#print(3 in s1) #貼出3這個資料是否在s1這個集合當中 true or false 使用in這個指令來判斷
#print(3 not in s1)#貼出3是否沒有在s1這個集合當中
#s1={1,2,3,4,5}
#s2={4,5,6,7,8}
#s3=s1&s2 # &是交集 交集:取兩個集合中,相同的資料 注意!貼出的資料會是新的集合 {4,5}
#s3=s1|s2 # |是聯集(案shift和enter上方的案件) 聯集:取兩個集合中的所有資料,但重複的不會取(不重複取) 注意!貼出的資料會是新的集合 {1, 2, 3, 4, 5, 6, 7, 8}
#s3=s1-s2 # -是差集 差集:從s1中,減去和s2重複的部分 注意!貼出的資料會是新的集合 {1,2,3}
#s3=s1^s2 # ^是反交集 反交集:取兩個集合中,不相同的資料 注意!貼出的資料會是新的集合 {1, 2, 3, 6, 7, 8}
#print(s3) 
#s=set("Hello") # set(字串) set會將""中的字母拆解成{}集合 重複的不取
#print("a" in s) #將字串拆解成字母後才能判斷字母是否有在字串當中
 
# 字典的運算:key-value的配對
#dic={"apple":"蘋果","blue":"藍色"} # 注意!! 字典的key和value的位置是固定的,第一個擺key,第二個擺value
#dic["apple"]="大蘋果" #將apple這個key的value 從蘋果改成大蘋果
#print(dic["apple"]) #apple這個key取得蘋果這個value
#print("apple" in dic) #判斷apple這個key是否在dic這個字典裡
#print("cat" not in dic) #判斷cat是否在dic裡
#doc={"蘋果":"apple","藍色":"blue"}
#print(doc["apple"]) #錯誤 因為一定要用key找value 不能用value找key
#print(dic)
#del dic["apple"] #刪除字典中的鍵值對 (key-value pair)
#print(dic)

dic={x:x*2 for x in [3,4,5]} #從列表中的資料產生字典  將[3,4,5]這個列表(list)逐一帶入以x:x*2方式變成字典 ,{變數:變數運算for 變數 in 列表} 這個寫法是固定的   
print(dic)