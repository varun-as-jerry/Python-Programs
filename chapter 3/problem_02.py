
# Qusetion :write a program to fill in a letter template 
#            given below with name and date 

# Letter = '''dear <|Name|>
            #   you are sellected !
            # <|Date|> 

letter = '''dear <|Name|>,
greetings from abc coding house.\nI am happy to tell you that,
you are sellected !
Have a great day ahead!
Thanks and regards,
bill
Date: <|Date|> '''

name = input("Enter Your Name\n")
date= input("Enter Your Date\n")

letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)

print(letter)

