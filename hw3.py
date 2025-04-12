text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
space_count  = 0
for i in range(len(text)):
    if text[i] == ' ' or text[i] == '\n':
        space_count += 1
print(space_count)

textWithoutMistakes = text.replace(' iZ ', ' is ').replace(' iz ', ' is ').replace(' Iz ', ' is ')

formatedText = textWithoutMistakes.lower().split('\n ')
for i in range(len(formatedText)):
    formatedText[i] = formatedText[i].capitalize()
print('\n'.join(formatedText))