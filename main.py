# 主程式
# 封包
# 封包是讓一堆模組打包在一個資料夾然後一一叫出
import geometry.point as wry #載入"geometry"這個封包中的"point"模組 讓他AKA wry
result=wry.distance(3,4) #讓result這個變數等於wry模組中的distance這個函式以數字3,4帶入變數
print("距離",result) #並貼出成果
import geometry.line as peko #載入"geometry"這個封包中的"line"模組 讓他AKA peko
result=peko.slope(1,1,3,3) #讓result這個變數等於peko模組中的slpoe這個函式以數字1,1,3,3帶入變數
print("斜率",result) #並貼出成果
#注意 取別名的話一定要使用別名