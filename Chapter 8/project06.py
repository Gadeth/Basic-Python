def sortStringByChar(myData):
    myData.sort(reverse=True)
    return(myData)
print(sortStringByChar)

def getListBuah():
    count = int(input('ingin memasukkan berapa buah? '))
    loop = 0
    data = []
    while loop < count:
        nama = input("Masukkan buah ke-{0} : ".format(loop+1))
        data.append(nama)
        loop += 1
    return data

dataList = getListBuah()

if(dataList):
    print("\nHasil buah dari list",dataList,'dengan urutan dari jumlah karakter penyusun tiap string huruf besar ke kecil :')
    result = sortStringByChar(dataList)
    print(result)

