import pandas as pd

with open('C:\\Users\\123\\Documents\\GinCode\\tools\\testTables\\tables.txt','r',encoding='utf-8') as f:

	for line in f:

		#取表名
		if (line.find('CREATE TABLE'))>-1 or (line.find('create table'))>-1:
			with open('C:\\Users\\123\\Documents\\GinCode\\tools\\testTables\\result.txt',"a") as fo2:
				fo2.write("\n"+"table_name:"+line.split('"')[3]+"\n")
		#过滤index语句		
		elif (line.find('CREATE INDEX'))>-1:
			with open('C:\\Users\\123\\Documents\\GinCode\\tools\\testTables\\result.txt',"a") as fo2:
				fo2.write("--------------"+"\n"+"table_index:"+line.split()[2]+ "-"+line.split()[4]+"\n")
		#解释，取原字段和释义
		elif (line.find('COMMENT ON COLUMN'))>-1:
			with open('C:\\Users\\123\\Documents\\GinCode\\tools\\testTables\\result.txt',"a") as fo2:
				fo2.write((line.split('"')[5])+'-'+line.split('\'')[1]+'\n')
		#数据类型 取原字段和数据类型
		elif (line.find('int')>-1) or (line.find('varchar')>-1) or (line.find('text')>-1) or (line.find('timestamp')>-1) or (line.find('bool')>-1) or (line.find('date')>-1) or (line.find('point')>-1) or (line.find('point')>-1) or (line.find('polygon')>-1) or (line.find('box')>-1):
			with open('C:\\Users\\123\\Documents\\GinCode\\tools\\testTables\\result.txt',"a") as fo2:
				fo2.write(line.split('"')[1]+'-'+line.split()[1]+'\n') 
		else:
			pass

		fo2.close
	f.close