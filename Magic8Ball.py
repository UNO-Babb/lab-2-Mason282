#Magic8Ball.py
#Name: Mason Rodgers
#Date: 1/29/25
#Assignment: 8 ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
question=input("What do you desire" '?')

answers=["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
"Do not count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
"Outlook not so good.","Outlook good.", "Reply hazy, try again.","Signs point to yes.", "Very doubtful.", "Without a doubt.",
"Yes.", "Yes ,definitely.", "You may rely on it."]
  #Answer question randomly with one of the options from your earlier list.
length=len(answers)
r=random.random() * length

r=int(r) 
print(r)
response=answers[r]
print(response)


if __name__ == '__main__':
  main()

