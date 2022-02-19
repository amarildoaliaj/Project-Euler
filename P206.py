def Check(n):
    if n.__str__()[0] == '1':
        if n.__str__()[2] == '2':
            if n.__str__()[4] == '3':
                if n.__str__()[6] == '4':
                    if n.__str__()[8] == '5':
                        if n.__str__()[10] == '6':
                            if n.__str__()[12] == '7':
                                if n.__str__()[14] == '8':
                                    if n.__str__()[16] == '9':
                                        if n.__str__()[18] == '0':
                                            return True
    return False


a = (10**9).__int__()
b = (1.4*10**9).__int__()
for i in range(b, a, -10):
    if Check(i*i):
        print(i)
        break
