def len(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5 #平面座標系線段的公式
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1) #斜率 tan()