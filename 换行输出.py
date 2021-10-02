print(" "*7,"phy")
verse = ["如图所示","质量均为m的滑块A、B、C置于水平地面上","中间用劲度系数分别为k1、k2的轻弹簧a，b连接","在施加在滑块C上的水平恒力F作用下","一起无相对运动地向右加速运动"]
for index,item in enumerate(verse):
    if index%2 == 0:
        print(item+",",end='')
    else:
        print(item+".")
print("can you understand the useage?")