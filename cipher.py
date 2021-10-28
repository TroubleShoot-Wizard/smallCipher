msgString = str(input("Enter message to be encrypted. : "))
msgList = []
msgList[:0]=msgString;

for i in range(len(msgList)):
	if(msgList[i] == 'a'):
		msgList[i] = 'u';
	elif(msgList[i] == 'e'):
		msgList[i] = 'o';
	elif(msgList[i] == 'o'):
		msgList[i] = 'e';
	elif(msgList[i] == 'u'):
		msgList[i] = 'a';

outputString = ""
for i in msgList:
	outputString += i;

print(outputString);
