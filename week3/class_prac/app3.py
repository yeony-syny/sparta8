from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

quiz = db.movies.find_one({'title':'매트릭스'})
print(quiz['star'])

same_names = list(db.movies,.find({'star':{'매트릭스'}},{'_id':False})
print()