import json 
import classes_user as c
def json_dump(kin,dic):
    combo="C:\\Users\\arsal\\Desktop\\anaconda\\file prsactice\\csv\\jsons\\"+kin.name+".json"
    with open (combo,"w") as f:
        json.dump(dic,f)
def json_load ():
    try:
        file_name=str(input("enter name: "))
        combo="C:\\Users\\arsal\\Desktop\\anaconda\\file prsactice\\csv\\jsons\\"+file_name+".json"
        with open(combo) as f:
            lp= json.load(f)
            print(lp)
    except FileNotFoundError:
        print("Sorry "+file_name+" non present")

if __name__=="__main__":
    while True:
        user_input=str(input("to create user in json press P, to view file press V: "))
        if user_input =="p" or user_input=="P":
            o=c.User(str(input("enter name: ")),int(input("enter age: ")),
            str(input("enter gender: ")))#class module
            print(o.name)
            dic=(c.User.data_dic(o))#func of class module
            print (dic) 
            # combo="C:\\Users\\arsal\\Desktop\\anaconda\\file prsactice\\csv\\jsons\\"+o.name+".json"
            # with open (combo,"w") as f:
            #     json.dump(dic,f)
            json_dump(o,dic)#own func
        elif user_input =="V" or user_input=="v":
            json_load()#own func