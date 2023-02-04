import pandas as pd
import numpy as np

file1 = open('Janet.conllu', 'r')
Lines = file1.readlines()

texts = []
intents = []

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if(line.startswith('# text')):
        p_line = line.strip()
        print("Line{}: {}".format(count, p_line[8:]))
        texts.append(p_line[8:])

    if(line.startswith('# intent')):
        x_line = line.strip()
        print("Line{}: {}".format(count, x_line[10:]))
        intents.append(x_line[10:])

data = {'Text':texts, 'Intent':intents}
df = pd.DataFrame(data)

print(df.head(5))

df.to_csv(r'data.tsv',index=False, sep='\t')