with open("inout\data2.txt","r") as f1:
    data=f1.read()
    print(data)

with open("inout\data.txt","r+") as f2:
    f2.write("from") 