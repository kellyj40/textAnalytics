# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator
import copy
from random import shuffle


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])
			if random.random() < split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow(float(instance1[x]) - float(instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0


def k_fold(filename, k):
	k_sets = []
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		size_of_groups = int(len(dataset)/k)
		shuffle(dataset)
		count = 0
		countLoop = 0
		while countLoop <= k:
			sub_set = dataset[count:size_of_groups+count]
			count+=size_of_groups
			if len(sub_set) > 0:
				k_sets+=[sub_set]
			countLoop+=1
	return k_sets


results = []
def main():
	# prepare data
	k_fold_num = 5
	kfold_set = k_fold('iris.csv', k_fold_num)

	k = 1
	# for x in range(len(kfold_set)):
	print(kfold_set)
	total_accuracy = 0
	for test_set in kfold_set:
		predictions = []
		training_set_copy = copy.deepcopy(kfold_set)
		training_set_copy.remove(test_set)
		training_set=[]
		for training in training_set_copy:
			training_set += training


		for x in range(len(test_set)):
			neighbors = getNeighbors(training_set, test_set[x], k)
			result = getResponse(neighbors)
			predictions.append(result)


		accuracy = getAccuracy(test_set, predictions)
		total_accuracy+=accuracy
		print('Accuracy: ' + repr(accuracy) + '%')
	print("Average accuracy: "+ str(total_accuracy/k_fold_num)+ '%')


main()
# results=[[0.1, 87.5], [0.2, 96.52], [0.3, 96.81], [0.4, 97.03],
# 		[0.5, 93.75], [0.6, 97.14], [0.7, 97.5],
# 		[0.8, 90.32], [0.9, 85.71]]
# import matplotlib.pyplot as plt
# for result in results:
# 	plt.plot(result[0], result[1], 'ro')
# plt.axis([0.0, 1.0, 80, 100])
# plt.xlabel('Split Value')
# plt.ylabel('Accuracy')
# plt.show()