import classes_user as c
import csv
import json_user
def to_csv():
    user_input=str(input("enter file name: "))
    combo_1 = "C:\\Users\\arsal\\Desktop\\anaconda\\file prsactice\\csv\\"
    combo=  combo_1+ user_input+".csv"
    with open(combo,"w",newline="") as f:
        file_handler=csv.writer (f,delimiter=",")
        file_handler.writerow(["name","age","gender"])
    return combo        

def into_csv(l,combo):
    with open(combo,"a",newline="") as f:
        file_handler=csv.writer (f,delimiter=",")
        file_handler.writerow(l)
    
    # with open(combo,"r",newline="") as f:
    #     content=csv.reader(f)
    #     l=[]
    #     for i in content:
    #         l+=i
    #     print(l)
    #pushcheck

if __name__=="__main__":
    while True:
        user_input=str(input("to create file press C , to append press P to quit press any other key: "))
        if user_input=="C" or user_input=="c":
            u=to_csv()#own func
        elif user_input == "P" or user_input=="p":
            user_input=str(input("enter file name: "))
            combo_1 = "C:\\Users\\arsal\\Desktop\\anaconda\\file prsactice\\csv\\"
            combo=  combo_1+ user_input+".csv"
            while True:
                user_input=str(input("to append press A: "))
                if user_input== "a" or user_input=="A":
                    u1=c.User(str(input("enter name: ")),int(input("enter age: ")),str(input("enter gender: ")))#class module
                    o=u1.data_csv()#class module
                    print(o)
                    into_csv(o,combo)#own func
                    dic= u1.data_dic()
                    print(dic)
                    json_user.json_dump(u1,dic)

                else:
                    break
        # elif user_input=="I" or user_input=="i":
        #     u1=c.User(str(input("enter name: ")),int(input("enter age: ")),str(input("enter gender: "))) #class module
        #     o=u1.data_csv() #from class module
        #     print(o)
        #     into_csv(o,u)#own func
        #     #print(u1.data_csv())
        else:
            break
