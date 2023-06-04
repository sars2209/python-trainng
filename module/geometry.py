# 在geometry模組中定義幾何運算功能
def distance(x1,y1,x2,y2): #定義取平面座標系統中兩點的距離
    return ((x2-x1)**2+(y2-y1)**2)**0.5 #國中公式 三角函數 直角三角形取第三邊公式
def slope(x1,y1,x2,y2): #定義取得平面座標系統中兩點的斜率 就是tan()
    return (y2-y1)/(x2-x1) 