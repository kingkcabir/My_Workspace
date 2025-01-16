text = input("input your words: ")
text = text.lower()
vowels = []
consonant = []
for ch in text:
    if ch in 'aeiou':
        vowels.append(ch)
    if ch in 'bcdfghjklmnpqrstvwxyz':
        consonant.append(ch)
    
print('vowels or consonants?')
answer = input('your response: ')
if answer == 'vowels':
    print('vowels in word are: ', ' '.join(vowels), end=' ')
        
elif answer == 'consonant':
    print('consonant in word are: ', ' '.join(consonant), end=' ')