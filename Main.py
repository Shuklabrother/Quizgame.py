import  pyfiglet

print(pyfiglet.figlet_format("Quiz \nGame"))

score = 0

print("1.What is the capital city of Australia?\na). Sydney\nb). Melbourne\nc). Canberra\nd). Perth")

ans = str(input ("Choose option: "))

if ans=="c":

  print("You won 1000 points ")

  score+=1000

else:

  print("You loss 1000 points ")

  score-=1000

print("Your score is", score)
