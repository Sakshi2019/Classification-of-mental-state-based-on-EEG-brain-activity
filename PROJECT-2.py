import numpy as np

from sklearn.naive_bayes import GaussianNB

x = []
file = 'EEG_data.csv'
with open(file) as f:
	x = f.readlines()

train = []
test = []
traininput = []
trainoutput = []
testinput = []
testoutput = []

for i, a in enumerate(x):
	if i < len(x) - 102:
		train.append(list(int(b) for b in a.split(',')))
	else:
		test.append(list(int(b) for b in a.split(',')))

for i, a in enumerate(train):
	toappend = []
	for c, b in enumerate(a):
		
			if c >= 2 and c < 13:
				toappend.append(b)
			elif c==13:
				trainoutput.append(b)
	if(len(toappend) > 0):
		traininput.append(toappend)

for i, a in enumerate(test):
	toappend = []
	for c, b in enumerate(a):
		
			if c >=2 and c < 13:
				toappend.append(b)
			elif c == 13:
				testoutput.append(b)
	if(len(toappend) > 0):
		testinput.append(toappend)

X = np.array(traininput)
y = np.array(trainoutput)


#Gaussian Naiive Bayes
gnb = GaussianNB()
gnb.fit(X, y)

correct = [0]
incorrect = [0]
gnbs = []

for i, a in enumerate(testinput):
	
	if gnb.predict([a])[0] == testoutput[i]:
		correct[0] += 1
		gnbs.append(0)
	else:
		incorrect[0] += 1
		gnbs.append(1)
	
print(correct)
print(incorrect)


#Only about 80% Accurate
