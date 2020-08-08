import math
def sol():
    n = '101'
    a = int(n)
    operate = [a]
    counter = 0
    prevLen = len(operate)
    flag_log_value = 0

    while operate.count(1) == 0: # loop through this as long as there is no 1 in operate list
        for i in range(prevLen):
            if operate[i] % 2 == 0:
                if math.log(operate[i],2).is_integer():
                    flag_log_value = math.log(operate[i],2)
                    break
                
                operate[i] = operate[i] / 2
                if operate.count(1) == 1:
                    break
            else:
                operate.append(operate[i] + 1)
                operate[i] = operate[i] -1
                if operate.count(1) == 1:
                    break

        if flag_log_value == 0:
            counter += 1
            operate = list(dict.fromkeys(operate))
            operate.sort()
            prevLen = len(operate)
        else:
            counter += int(flag_log_value)
            break

    return counter
