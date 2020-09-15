import wikipedia

flag=True

def searcher(question):
    global flag
    answer = wikipedia.summary(question).split(".")
    for line in answer:
        print(line)
    X=int(input("Do you want to quit(0):"))
    if X==0:
        flag=False

while flag==True:
    if __name__ == "__main__":
        question = input("Search Wikipedia:")
        searcher(question)
