import nltk#This imports the nltk library.NLTK(Natural Language Toolkit) is a library used when we are dealing with text
#in our program.It helps in tokenization,stemming etc
nltk.download('all')#We are downloading all nltk packages here the downloading process may take 2-3 minutes
import warnings
warnings.filterwarnings('ignore')#we use this to ignore the warnings means in the output warnings should not appear

#Now we will perform Tokenization
from nltk.tokenize import sent_tokenize#we are importing sentence tokenization(sent_tokenize) from tokenize tool of nltk
#Sentence tokenization means if we have more than one sentences and we want to seperate out the sentences then we use
#sentence tokenization
text="I am Bharadwaj Patil. I am third Year student of Artificial Intelligence and Data Science. Today I am performing a DSBDA practical on text analytics"
tokenized_text = sent_tokenize(text)
tokenized_text#so here in the result you will see that all three sentences are splitted this is due to sentence tokenization
#one very important thing to note that is when you are writing the text ensure that you give spacing after full stop of the
#sentence if you dont give spacing then sentence tokenizer will consider that it is one long sentence and you
#will not see the sentences splitted
#For example in:
#I am Aditya Nikam. I am third Year student of Artificial Intelligence and Data Science.
#Here if do not give spacing after full stop(Nikam. I(like this)) and directly continue the next sentence like(Nikam.I (like
#this)) then we will not get the splitted sentences all will come in one line only
#I am Aditya Nikam.I am third Year student of Artificial Intelligence and Data Science.(Here all will come in one line
#only the sentence will not be splitted as we havent gave spacing after full stop)

length=len(tokenized_text)
print("Number of sentences:", length)#Here we are printing the number of sentences in the text we provided

#Now lets perform tokenization for words of sentences
from nltk.tokenize import word_tokenize #we are importing word tokenization(word_tokenize) from tokenize tool of nltk
#Word tokenization means if we have one or more than one sentences and we want to seperate out the words then we of the
#sentence then we use word tokenization
text="I am Bharadwaj Patil. I am third Year student of Artificial Intelligence and Data Science."
tokenized_text = word_tokenize(text)
tokenized_text#Now here in result you will see that all words of the sentences are seperated even the full stop is seperated
#Again here if you dont give spacing after full stop the word tokenizer will consider the full stop and next word as one
#complete word which is incorrect
#For example in:
#I am Aditya Nikam. I am third Year student of Artificial Intelligence and Data Science.
#Here if do not give spacing after full stop(Nikam. I(like this)) and directly continue the next word like(Nikam.I (like
#this)) then we will see that ".I" is considered as one word we dont want this we want full stop seperate and I seperate
#Like this "." "I"

length=len(tokenized_text)
print("Number of words:", length)#Here we are printing the total no of words of our text(Note that full stop is also)
#counted as word

#Now we want to remove the stop words from our text
from nltk.corpus import stopwords##we are importing stopwords from corpus tool of nltk
#stopwords are common English words like "is", "the", "and", etc., that are often removed from text because
#they don’t help in data analytics
stop_words=set(stopwords.words("English"))
stop_words
#Here we print all the stop words that are in English Language

text="What is your name?"
#Now I want to remove punctuation marks from my text we can do it using re(regular expression) library of python
import re#importing re(regular expression)library
text = re.sub('[^a-zA-Z]', ' ', text)#This keeps only letters in my text and replaces everything else
#(like numbers, punctuation) with spaces.
#Note that if I write          text=re.sub('[a-zA-Z]', ' ', text) then all letters from my text will be removed and replaced
#by spaces and only letters and punctuations will remain in my text
text#You will see that punctuation mark("?") are removed here in my sentence

#As you can see in the result of the command stop_words=set(stopwords.words("English")) which is written above all
#the stop words are in lowercase so we will first need to convert all our words of the sentence in lowercase then only
#stopwords will be removed else not
text1="I am currently in third year of Engineering"
text1=text1.lower()#converting whole text in lowercase
tokens=word_tokenize(text1)#seperating each word from the text using word tokenize
tokens

#Now I want to remove my stopwords
filtered_text=[]#creating empty list to store words which are not stop words
for w in tokens:#the for loop goes through each word(w)of tokens variable
    if w not in stop_words:#this checks if the current word of loop is in the list of stop words or not.If word is not
        #a stop word then next line will execute
        #stop_words variable was decalred in above commands
        filtered_text.append(w)#this will append the word which is not stop word in filtered_text list

filtered_text#printing the words which are not stop words

#Now we will do stemming

#Stemming is the process of reducing a word to its root form by removing suffixes from the word.
#For example:
#"Running", "Runner", "Runs" → All are reduced to the base form "Run".
#"Happiness", "Happier", "Happy" → All are reduced to the base form "Happi".

from nltk.stem import PorterStemmer#Porter Stemmer is a tool which helps us to do the stemming process
porter = PorterStemmer()#created object of Porter Stemmer
print(porter.stem("Playing"))
print(porter.stem("Studies"))
print(porter.stem("Running"))
print(porter.stem("played"))
print(porter.stem("Hardworking"))
print(porter.stem("Happiness"))

#Lemmatization is the process of changing a word to its base or dictionary form (called a lemma) by following proper
#grammar rules
#Stemming also converts the word in base form but the word converted by stemming may not be gramatically correct as it does
#not follow grammar rules thats the difference between stemming and lemmatization
#For example in stemming the word "studies" will be converted to "studi" which is gramtically incorrect
#But if we use lemmatization the word "studies" will be converted to "study" thats gramatically correct
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("studies"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("playing"))
#Here we see that the output of playing will be playing only because lemmatize function takes the word by default as noun.
#If you do not tell the lemmatizer whether a word is a verb, noun, or adjective,
#it will automatically assume the word is a noun.
#So as we know that playing is a verb so we should write
print(lemmatizer.lemmatize("playing", pos="v"))#Now the output will be play
#Similarly we know that "better" is an adjective so we should write
print(lemmatizer.lemmatize("better",pos="a"))#Now the output will be good
#pos means part of speech which helps to determine whether the word is noun(n),adjective(a),or verb(v)

#POS Tagging means  means labeling each word with correct of part of speech like whether the word is noun,verb,adjective
#adverb etc
text2 = "The white sweater fits him perfectly"
tokens1 = word_tokenize(text2)
print(nltk.pos_tag(tokens1))
#The output tells that the is Determiner(DT),white is adjective(JJ),sweater is noun(NN),fits is verb(VBZ),him is preposition
#(PRP),perfectly is adverb(RB)

corpus = [
    'data science is one of the most important fields of science',
    'this is one of the best data science courses',
    'data scientists analyze data'
]#This creates a list of sentences and stores it in the variable corpus.
words_list = []#It Creates an empty list to store unique words only (no duplicates allowed in sets)
for doc in corpus:#The for loop goes through each sentence (doc) one by one from the corpus
    words = doc.split(' ')#Splits the sentence into words using space ' ' as the separator.
#For example 'data science' becomes ['data', 'science'].
    for word in words:#Goes through each words of the words list one by one
        if word not in words_list:#Checks if the current word is there or not in word_list if not then line executes
            words_list.append(word)#adds the current word in word_list if its not already added
print('Number of words in the corpus:', len(words_list))#Prints how many unique words are in the entire corpus.
print('The words in the corpus: \n', words_list)

import pandas as pd
import numpy as np
n_docs = len(corpus)#calculating the number of sentences(document) in corpus
n_words = len(words_list)#calculating the number of unique words in the corpus
df_tf = pd.DataFrame(np.zeros((n_docs, n_words)), columns=words_list)
#We create a dataframe(table) here using pd.Data Frame of size n_docs x n_words means suppose we have 3 sentences in corpus
#means n_docs=3 and no.of unique words in corpus is 14 like in our case so n_words=14
#so table will have 3 rows and 14 columns
#intially values in every column will be zero using np.zeros
#columns=words_list will make the unique words as column names means as we have 14 unique words in our example so 14 columns

for i in range(n_docs):#the for loop goes through each sentence in the corpus one by one
    words = corpus[i].split()#it seperates the words of the current sentence
    #For example: "data science is fun" becomes ["data", "science", "is", "fun"].
    for w in words:#Now we go through each word of that current sentence one by one
        df_tf.loc[i, w] += 1 /len(words)#df_tf.loc[i, w] puts the value of TF in the current row of for loop(i) and the
        #word(w)
        #Means if for loop is running for first sentence then i value will be zero and if current word is "data" in
        #inner for loop then df_tf.loc[i, w] will place the calculated tf value in zero row of data column using loc
        #function and same for the others
        #Here we have applied the formula of TF
        #Intially the value of numerator is kept as 1 means that word is one time if the current word appears more
        #than one time in that particular sentence then the value incremen
df_tf

import numpy as np
idf_values = {}#this creates an empty dictionary to store idf values of each word

for word in words_list:#The for loop goes through each word of the set of unique words
    doc_count = 0#it will count how many sentences have the current word intially it is intialized to zero
    for doc in corpus:#This goes through each sentence of the corpus
        if word in doc.split():#doc.split() splits the sentence into words
            #if word in doc.split() checks if the current word is there or not in the sentence
            doc_count += 1#if the word is there in sentence then increase the count by 1
    idf = np.log10(n_docs / doc_count)#Applying the formula of idf
    idf_values[word] = idf# We store the calculated idf in the dictionary using the word as the key.means the word is the
    #key of the key value
for word in sorted(idf_values.keys()):#print the idf values of each word alphabetically
    #We used sorted function()to print the words alphabetically
    print(f"{word:>10}: {idf_values[word]}")

df_tf_idf = df_tf.copy()#we are creating a copy of df_tf dataframe to ensure that any changes made to df_tf_idf don't affect
#the original df_tf dataframe.

# Multiply each TF value by its corresponding IDF
for word in words_list:#this starts for loop and for loop goes through each word of unique word list(word_list)which
    #is a list declared in above commands one by one
    for i in df_tf.index:#it loop through each row of our df_tf dataframe which was used to show tf values
        tf = df_tf.loc[i, word]#This line retrives value of tf for the current row and current word from df_tf dataframe
        #Like for example if currently the loop is visiting first row(row 0) of df_tf dataframe so i=0 and and if
        #current word in for loop is "data" means w="data" then this command will retrive the zero row value of data column
        #from df_tf dataframe
        idf = idf_values[word]#it retrives the idf value of current word
        tf_idf = tf * idf#multiplying tf and idf to get tf-idf value
        df_tf_idf.loc[i, word] = tf_idf#It puts the value of TF-IDF in the current row of for loop(i) and the
        #word(w)
        #Means if for loop is running for first row of df_tf dataframe then i value will be zero and if current word is
        #"data" in inner for loop then df_tf_idf.loc[i, w] will place the calculated tf-idf value in zero row of data column
        #using loc function and same for the others

# Display the TF-IDF table
df_tf_idf#printing df-tf_idf dataframe to show the values calculated