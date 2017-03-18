from pymongo import MongoClient
import random

stus=MongoClient().test.stu
for stu in stus.find():
    print(stu)
