import random
if __name__ == '__main__':
    checkcode = ""
    for i in range(4):
        index = random.randrange(0,4)
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97,122))
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90))
        else:
            checkcode += str(random.randint(1,9))
    print("验证码：",checkcode)
            
