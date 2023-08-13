# pip install better_profanity

from better_profanity import profanity 

text ='Please tom, stop calling my dog a bitch please'

censored = profanity.censor(text)

print(censored)


#Please tom, stop calling my dog a **** please
