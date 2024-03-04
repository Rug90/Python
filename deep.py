Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip(" ")

if Answer == "42" or Answer == "forty two" or Answer == "forty-two":
    print("Yes")
else:
    print("No")