import iris

rs = iris.sql.exec('select * from Data.Titanic')

for row in rs:
    print (row)