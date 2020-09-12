import collections
import re



def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ', paragraph)\
        .lower().split()
            if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]



paragraph = "Bob hit a ball, the hit BALL flew after it was hit"
banned = ["hit"]

print(mostCommonWord(paragraph,banned))
