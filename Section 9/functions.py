#functions
#Incorrect way
def add(x,y):
	x + y

#correct way
def add(x,y):
	return x + y

print(add(5,10))

#Storing variables as function answers
answer = add(100,20)
print(answer)

#print not the same as return
#print does not process return, only displays the answer

# Reverse
def rev(text):
	return text[::-1]

print(rev("pen"))
