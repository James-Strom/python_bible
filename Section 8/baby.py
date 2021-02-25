from random import choice

questions = ["Why is the sea green?", "Why is grass green?: ", "Why is 1 bigger than 0: ",
			"Why is the sky blue?:"]


question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
	answer = input("why?: ").strip().lower()

print("Oh...Okay")
