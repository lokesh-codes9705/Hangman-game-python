import random
print("lets start game")
opp=["apple","mango","carrot","cat","vizag"]
cho=random.choice(opp)
hang=['''
  o
/|\
 /\
''','''
  o
/|\
/
 
''','''
  o
/|\

''','''
  o
/|

''',''' 
  o
  |  
''',''' 
  o
''' ]
print(cho)
quo=[]
lives=6
for i in cho:
    quo+='_'
print(quo)
over=False
while not over:
    guess=input("guess a letter")
    for i in range(len(cho)):
        let=cho[i]                    
        if let ==guess:
            quo[i]=guess
            print (f"one is correct{quo}")              
    if guess not in cho:
         lives-=1
         print(f"you lost 1 life you have just {lives} lives")
         print(hang[lives])                  
         if lives ==0:
             print("you loose")
             break 
    if '_' not in quo:
         print("wow you guessed all great you won")
         break 
print("game over")             