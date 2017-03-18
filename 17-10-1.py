from pymongo import MongoClient

stus=MongoClient().test.stu
print(list(stus.find()))
