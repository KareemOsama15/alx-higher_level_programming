#!/usr/bin/python3

def text_indentation(text):
    
    # if not isinstance(text, str):
    #     raise TypeError("text must be a string")
    
    # # for delim in '.?:':
    # #     newText = text.split(delim)
    # #     for i in newText:
    # #         i = i.strip(" ")
    # #         text = i + delim + "\n\n"
    # # print(text)

    for delim in ".:?":
        newtext = text.split(delim)
        text = ""
        for line in newtext:
            line = line.strip()
            text += line + '\n'
        print(text)
        print('=' * 20)
        print(newtext)

    # # print(newtext)

######################################


    # if type(text) is not str:
    #     raise TypeError("text must be a string")

    # s = text[:]

    # for d in ".?:":
    #     list_text = s.split(d)
    #     s = ""
    #     for i in list_text:
    #         i = i.strip(" ")
    #         s = i + d if s is "" else s + "\n\n" + i + d

    # print(s[:-3], end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
