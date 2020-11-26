text1 = """Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]"""
text2="""Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."""

#tokenization
text1 = text1.split()
text2 = text2.split()

#removing stop words
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

stopwords = stopwords.words("english")

for i in range(len(stopwords)):
    if stopwords[i] in text1:
        text1.remove(stopwords[i])

    if stopwords[i] in text2:
        text2.remove(stopwords[i])


#Jaccards Index
#JI = len(intersection)/len(union)

set1= set(text1)
set2= set(text2)
JI=len(set1.intersection(set2))/len(set1.union(set2))
print(JI*100)
