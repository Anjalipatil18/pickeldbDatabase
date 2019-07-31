import meradb
db1 = meradb.load('pehla.db')
db2 = meradb.load('doosra.db')
db1.setData('key', 'value1')
db2.setData('key', 'value2')
db2.getData('key')
db1.getData('key')