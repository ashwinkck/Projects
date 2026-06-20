with open("story.txt","r") as f:   #open and reading the text file
    story = f.read()

words = set() #Creating set for getting the unique word alternatively it was list, but we need unique so
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):  #complete for loop will locates all of the different words inside our story
    if char == target_start:
        start_of_word = i


    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1


answers = {}

for word in words:
    answer = input(f"Enter a word for {word} :" )
    answers[word] = answer

print(answers)

for word in words:
    story.replace(word,answers[word])

print(story)