people = ["Nathan", "Spencer", "Brother Scott"]
numbers = [11, 2, 55]
things = ["dogs", 28, True]

print("These are things I like:", things)
print("This is a thing I don't like:", things[0])
print("This is the last thing:", things[-1])


things.append("One more thing...")
print("This is things now", things)

sentence = "Ain't nobody got time for that"
words = sentence.split()
print("The words are", words)


things.append(people)
print("This is things now:", things)
print("This is the first person in the last thing:", things[-1][0])