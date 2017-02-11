# This is written for PYTHON 3
# Don't forget to install requests package
import os
import requests
import json
import random
import statistics


def getListOfAmount(data):
	result = []
	for index in range(0, len(data)):
		result.append(data[index]["amount_left"])
	return result

def amountMain(apiKey):
	customerID = 0
	url = "http://api.reimaginebanking.com/atms?lat=38.9283&lng=-77.1753&rad=15&key=b41d66a7ca98a1d3df650659190e2e62".format(customerID,apiKey)
	data = requests.get(url)
	data = data.text.replace("true","True")
	data = data.replace("false","False")
	data = eval(data)
	data = data["data"]
	print(getListOfAmount(data))

def addressParse(data):
	result = ""
	for key in data:
		result += data[key] + " "
	return result

def manInsert(data):
	result = []
	average = 0
	for index in range(0, len(data)):
		num = random.randint(50000,100000)
		name = data[index]["name"]
		data[index]["visitors"] = num 
		average += num
		address = addressParse(data[index]["address"])
		lng = data[index]["geocode"]["lng"]
		lat = data[index]["geocode"]["lat"]
		result.append((name,address,num,lat,lng))
	average = average // len(data)
	#random.shuffle(result)
	result = sorted(result, key = lambda x: x[2])
	return (average,result)

def getStandardDev(data):
	result = []
	for index in range(0,len(data)):
		result.append(data[index][2])
	std = statistics.pstdev(result)
	return std

def makeList(data, index):
	result = []
	for thing in range(0, len(data)):
		print(data[thing])
		result.append(data[thing][index])
	#assert(False)
	return result
		 
	
	

def randomInsertBranch(apiKey):
	customerID = 0
	url = "http://api.reimaginebanking.com/branches?key=b41d66a7ca98a1d3df650659190e2e62".format(customerID,apiKey)
	data = requests.get(url)
	#data = data.text.replace("true","True")
	#data = data.replace("false","False")
	data = eval(data.text)
	average,tupleList = manInsert(data)
	name = makeList(tupleList,0)
	pop = makeList(tupleList,2)
	lng = makeList(tupleList,4)
	lat = makeList(tupleList, 3)
	return (name,pop,lng,lat)
	print("average: ",average)
	print("\n")
	print(getStandardDev(tupleList))

def main():
	customerId = "589e66741756fc834d9047b4"
	apiKey = "b41d66a7ca98a1d3df650659190e2e62"
	
	#amountMain(apiKey)
	return randomInsertBranch(apiKey)
	
#main()

