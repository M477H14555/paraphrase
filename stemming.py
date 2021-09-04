from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

TTTE = PorterStemmer()
lyrics = '''
I got knots all up in my chest (up in my chest, up in my chest)
Just know, I'm trying my best (I'm trying my best)
'Cause, when you look (when you look)
When you laugh (when you laugh)
When you smile (when you smile)
I'll bring you back (bring you back)
And now I'm sad (now I'm sad)
And I'm a mess (and I'm a mess)
And now we high (now we high)
That's, why I left (why I left)
That's, why I left
Will your tongue still remember the taste of my lips? (my lips, my lips, my lips)
Will your shadow remember the swing of my hips? (my hips, my hips, my hips)
Will your lover caress you the way, that I did? (I did, I did, I did)
Will you notice my charm, if he slips up one bit? (one bit)
'Cause I don't need to know
I just wanna make sure you're okay (okay)
I don't need to know
I just wanna make sure you're all safe, all safe, all safe
Will he play you those songs, just the way, that I did? (I did, I did, I did)
Will he play you so strong, just the way, that I did? (I did)
Yeah, yeah, yeah, yeah
Will he treat you like it, just the way, that I did? (I did, I did, I did)
'Cause I don't blame ya
'Cause I don't need to know
I just want to make sure you're okay (okay)
I don't need to know
I just want to make sure you're all safe
'''
stpwrds = set(stopwords.words("english"))
wrds = word_tokenize(lyrics)

coffee_filter = [word for word in wrds if word.casefold() not in stpwrds]
print(coffee_filter[:20])

TTTE_list = [TTTE.stem(word) for word in coffee_filter]
print(coffee_filter[:20])

# og = ["walk", "walked", "walking"]
# for word in og:
#     print(word, ":", TTTE.stem(word))

# print(f"Before: {len(wrds)}")
# coffee_filter = []
# for word in wrds:
#     if word.casefold() not in stpwrds:
#         coffee_filter.append(word)
# print(f"After: {len(coffee_filter)}")
