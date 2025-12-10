numInput=int(input())
text = ""
for h in range(numInput):
    text=""
    for x in range((numInput*2)):
        if x<(numInput-(h+1)):
            text += " "
        elif x<(numInput+(h+1)):
            text += "*"
        else :
            text += " "
    print(text)