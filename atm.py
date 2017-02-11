# This is written for PYTHON 3
# Don't forget to install requests package
import os
import requests
import json
import random


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

def manInsert(data):
	result = []
	average = 0
	for index in range(0, len(data)):
		num = random.randint(1000,100000)
		name = data[index]["name"]
		data[index]["visitors"] = num 
		average += num
		result.append((name,num))
	average = average\\len(data)
	return (average,result)

def randomInsertBranch(apiKey):
	customerID = 0
	url = "http://api.reimaginebanking.com/branches?key=b41d66a7ca98a1d3df650659190e2e62".format(customerID,apiKey)
	data = requests.get(url)
	#data = data.text.replace("true","True")
	#data = data.replace("false","False")
	data = eval(data.text)
	average, tupleList = (manInsert(data))
		

def main():
	customerId = "589e66741756fc834d9047b4"
	apiKey = "b41d66a7ca98a1d3df650659190e2e62"
	
	#amountMain(apiKey)
	randomInsertBranch(apiKey)
	
main()

