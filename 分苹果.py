def division():
    print("\n========apple dividing!========\n")
    apple = int(input("num of apples:"))
    children = int(input("num of children:"))
    if apple < children:
        raise ValueError("wrong num to div")
    result = apple // children
    remain = apple - result*children
    if remain > 0:
        print(apple,"apples to",children,"children,each has",result,"left",remain)
    else:
        print(apple,"apples to",children,"children,each has",result)
if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n xxx 0 is not an avaible num")
    except ValueError as e:
        print("\n wrong!",e)   
      
