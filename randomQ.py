import pandas as pd
import csv
import random

df = pd.read_csv('keywords.csv')
score = 0
correct = True

chapter = int(input("Chapter number: ").strip())
df = df[df['Chapter'] == chapter]
word_index = [i for i in range(len(df.axes[0]))]

while correct:
    i = random.choice(word_index)
    ans_key = df['Keyword'].loc[df.index[i]]
    ans_def = df['Definition'].loc[df.index[i]]
    word_index.remove(i)
    
    sampled_index = random.sample(word_index, 3)
    list_def = [ans_def] + [df.loc[n, 'Definition'] for n in sampled_index]
    random.shuffle(list_def)

    print(ans_key)
    for n in range(len(list_def)):
        print(f"{chr(n+65)}: {list_def[n]}")

    try:
        inp_ans = ord(input("Answer: ").upper())-65
        if list_def.index(ans_def) == inp_ans:
            print("Correct!")
            score += 1
            print(f"Score: {score}")
        else:
            print("Incorrect")
            correct = False
            print(f"Final score: {score}")
        print()
    except:
        print("Invalid input")