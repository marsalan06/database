def post(record):
    name_entery=str(input("Name: "))
    age_entery=int(input("Enter age: "))
    depart=str(input("Enter department: "))
    additional=int(input("If any other details provide number: "))
    if additional > 0:
        dic={}
        for i in range(additional):
            key=str(input("enter detail type: "))
            dic[key]=str(input("enter value for above detail: "))
    post_data={
        
        "name_entery":name_entery,
        "age_entery":age_entery,
        "department":depart,
        "additional":dic
        }
    print(post_data)
    record.insert_one(post_data)
    print(record.count_documents({}))

from pymongo import MongoClient
client=MongoClient("mongodb+srv://test:test@cluster0-yro7g.mongodb.net/test?retryWrites=true&w=majority")
print(client.list_database_names())
db=client.get_database("udemy_collect")
record=db.test
print(record.count_documents({}))
post(record)