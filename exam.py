
from fileinput import close
from docx import Document
with open('exam.docx',encoding="UTF-8") as f:
    data=  f.read()
    lenght=(len(data))
    for i in range(1,100):
        try:
            a=data.index("Câu "+ str(i))
            print(a)
            d=[]
            d.append(str(a))
            print(d[i-1])
            #print(data[a:b])
            #print("ccccccccccccccccccccccccccccccccccccccc")
            #d.append(data[0:6])
            #print(a,b)
            #print(d[i-1])
        except:
            break



    

