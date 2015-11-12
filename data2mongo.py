import pandas as pandas
import pymongo as pymongo

df = pandas.read_table('data/csdata.txt')
lst = [dict([(colname, row[i]) for i, colname in enumerate(df.columns)]) for row in df.values]
for i in range(3):
  print lst[i]

# change to your Docker Host IP address & port
con = pymongo.MongoClient('192.168.99.100', 27017)
test = con.db.test
test.drop()
for i in lst:
  test.save(i)
