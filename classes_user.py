#module for cv_2s.py
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def data (self):
        print("welcome user: ")
        print("user name is: "+self.name)
        print("user age is: "+str(self.age))
        print("user gender is: "+self.gender)
    
    def data_dic (self):
        dic={"user_name":self.name, "user_age":self.age, "user_gender":self.gender}
        return dic
        
    def data_csv (self):
        l=[self.name,self.age,self.gender]
        return l

    
if __name__=="__main__":
    while True:
        user_input=str(input("to enter press I to quit press any other key: "))
        if user_input=="I" or user_input=="i":
            u1=User(str(input("enter name: ")),int(input("enter age: ")),str(input("enter gender: ")))
            u1.data()
            print(u1.data_csv())
        else:
            break