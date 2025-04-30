def find():
    with open("C:\Pythonproject1\inout\data2.txt","r") as f1:
        x=f1.read()
        print(x)

    x1=x.replace("kumar","tejas")
    print(x1)

    with open("C:\Pythonproject1\inout\data2.txt","w") as f1:
        f1.write(x1)


    word="tejas"
    with open("C:\Pythonproject1\inout\data2.txt","r") as f1:
        y=f1.read()
        if(word.find("tejas")!=-1):
            print("found")
        else:
            print("not found")
find()


# WAP to find the line no in which given word present

def find_line():
    word="Unfortunately"
    data=True
    line_no=1
    with open("C:\Pythonproject1\inout\data.txt","r") as f2:
        while data:
            data=f2.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1        
print(find_line())
