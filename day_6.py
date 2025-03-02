def printTable(tableName,length):
    result = []
    for i in range(1,length+1):
        result.append(f"{tableName} X {i} ={tableName*i}")

    return '\n'.join(result)
# print(printTable("table,4))
print(printTable(2,10))

def isOdd():
 n= int(input('waht is number?'))
 if n % 2==1 :
  return True
 else:
    return False

print(isOdd())

