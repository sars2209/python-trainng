# 載入內建的sys模組並取得資訊
# import sys as system # 載入sys模組 AKA system 電腦會辨認出你取的AKA
# print(system.platform) #貼出系統
# print(system.maxsize) #

# 建立geometry模組，並載入使用 #python的模組要是python的檔案
# import module.geometry as geometry  #載入geometry模組
# # geometry.distance() #呼叫geometry模組中定義的distance並回傳回傳值
# result=geometry.distance(1,1,5,5) #result等於我給的數字 #跟上面那行可以寫在一起 會是result=geometry.distance(1,1,5,5)
# print(result) #貼出result

# result=geometry.slope(1,2,5,6)  #呼叫geometry模組中定義的slope並回傳回傳值
# print(result)

# 調整搜尋模組的路徑
import sys
print(sys.path) #印出模組的搜尋路徑 #注意!!!這是當我們要使用模組時python會按照順序去這些地方把模組抓進來 #路徑使用list列表方式呈現
#注意!!!!!!!!!!如果使用的模組與目前的程式不同資料夾的話會找不到!!
#注意!!!!!!!!!!我們可以使用以下方法指定python要去找這些資料夾來得到模組
sys.path.append("module") #讓python要尋找模組時多尋找當前路徑底下的module資料夾 #相對路徑
# 以上是在模組的搜尋路徑中{新增路徑}
print("------------------------------")
import geometry
print(geometry.distance(1,1,5,5))


# 這個對未來寫程式非常重要

# 新增絕對路徑