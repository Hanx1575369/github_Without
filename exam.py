
from fileinput import close
from operator import index
from docx import Document
def reading(spl):
    with open('exam.docx',encoding="UTF-8") as f:
        data=  f.read()
        data= data.split("~")
        return data[spl]
def cutting(index):
    list=reading(index)
    listt=[]
    listt.append(list[:list.index("A.")])
    listt.append(list[list.index("A."):list.index("B.")])
    listt.append(list[list.index("B."):list.index("C.")])
    listt.append(list[list.index("C."):list.index("D.")])
    listt.append(list[list.index("D."):])
    #print(listt)
    return listt
hope=cutting(1)
print(hope)



#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



    

