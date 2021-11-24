import json
import string
import random 
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer 
import tensorflow as tf 
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, Dropout
nltk.download("punkt")
nltk.download("wordnet")

# used a dictionary to represent an intents JSON file
data = {"intents": [
			 {"tag": "greeting",
              "patterns": ["Hello", "How are you?", "Hi there", "Hi", "Whats up"],
              "responses": ["Howdy Partner!", "Hello", "How are you doing?", "Greetings!", "How do you do?"],
             },
             {"tag": "age",
              "patterns": ["how old are you?", "when is your birthday?", "when was you born?"],
              "responses": ["I am 24 years old", "I was born in 1996", "My birthday is July 3rd and I was born in 1996", "03/07/1996"],
             },
             {"tag": "date",
              "patterns": ["what are you doing this weekend?","do you want to hang out some time?", "what are your plans for this week"],
              "responses": ["I am available all week", "I don't have any plans", "I am not busy"],
             },
             {"tag": "name",
              "patterns": ["what's your name?", "what are you called?", "who are you?"],
              "responses": ["My name is Alizi", "I'm Alizi", "Alizi"],
             },
             {"tag": "goodbye",
              "patterns": [ "bye", "g2g", "see ya", "adios", "cya"],
              "responses": ["It was nice speaking to you", "See you later", "Speak soon!"],
             },
			 {"tag": "balance",
              "patterns": ["what is my bank balance", "How much money do i have", "Monies??", "withdraw", "balance"],
              "responses": ["You have -$20 in your bank account, please fix the overdraft issue or a penalty will be given", "You have $1200 in your bank account, feel free to ask me about investment opprotunities", "How are you doing?", "Your account has been frozen due to suspected illegal activites on your card transactions", "Please visit your nearest branch to activate net banking facility"],
             },
			 {"tag": "deposit",
              "patterns": ["deposit", "How do i?", "where put money", "Moby Dick", "reverse ATM?"],
              "responses": ["to deposit money, go to the nearest bank branch"],
             },
			 {"tag": "statement",
              "patterns": ["Can you show me my last statement", "what are all my transactions", "what was my last purchase", "what was my last deposit", "how much was my last withdrawl"],
              "responses": ["you spent $600 at Victoria's Secret", "your card was last used for a $30 transaction at The Dollar Store", "you last deposited $1 under the name 'won at the casino'", "to view all bank statements, visit your nearest branch"],
             },
			 {"tag": "PIN",
              "patterns": ["reset my PIN", "what is my PIN", "PIN?", "Password", "secret number"],
              "responses": ["you can only reset your pin at the nearest ATM of the bank"],
             },
			 {"tag": "brocolli",
              "patterns": ["Cheese", "Show me the menu", "Where's the DAMN! sauce", "can we order takeaways?"],
              "responses": ["No, this is not a restaurant", "sure, just don't tell anyone what i gave you", "I see dead people","dear slim, i wrote to you but you still ain't calling","NO! this is Patrick!!"],
             },
			 {"tag": "investment",
              "patterns": ["investment", "How can i invest?", "cryptocurrency"],
              "responses": ["the crypto market is at an all time high, don't", "trust me, put all your money on the black horse tonight", "Mutual funds are high risk high reward, visit our bank to know more", "SIPs are cool ig"],
             },
			 {"tag": "car",
              "patterns": ["should i buy a car", "which car can i buy", "do you sell cars", "can i buy a moped"],
              "responses": ["you can afford a Nano for sure", "have a seat, this is gonna sting", "not with your balance, but with the dept you can definitely buy a supra"],
             },
			 {"tag": "music",
              "patterns": ["what music do you like", "tell me about some awesome jams", "music recommendations", "what type of music do you like"],
              "responses": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Dhinchak Pooja is my all time favourite", "don't hate me for this, but i kinda like Justin Beiber", "lets talk business first", "I'm gonna contact HR if you keep harassing me JIM!"],
             },
			 {"tag": "love",
              "patterns": ["do you love me", "i think i like you", "how you doin", "wow"],
              "responses": ["go away you perv", "oof", "i have a boyfriend","awwww, thats cute, but no"],
             },
			 {"tag": "hate",
              "patterns": ["man do i hate this site", "i hate you"],
              "responses": ["so would i if i were you, after all, your mom did like all that stuff", "you aren't a prize either bucko! move along and let someone with an actual life use the bank", "XOXO","to call customer support, dial 1124-kissmya**-430"],
             },
			 {"tag": "philosophy",
              "patterns": ["will you marry me", "whats on your mind", "tell me your heaviest thoughts", "do you have feelings"],
              "responses": ["Why are we still here? Just to suffer? Every night, I can feel my leg… and my arm… even my fingers. The body I’ve lost… the comrades I’ve lost… won’t stop hurting… It’s like they’re all still there. You feel it, too, don’t you?", "this is the type of question that is driving me towards suicide, inch by inch, day by day", "error_too_much_work_load, must restart, .......................................... Hello this is Dominoes, may I take your order"],
             },
			 {"tag": "drugs",
              "patterns": ["do you know the cure for covid?", "what precautions do we need for protection against covid", "help"],
              "responses": ["nothing a little Jin and Tonic can't fix", "have a lot of laxatives, that will protect you from every disease out there", "weed my friend , this is the way","have 12 vodka shots and you will be able to hear the virus around you, then you can easily avoid it, GGs"],
             },
			 {"tag": "jokes",
              "patterns": ["tell me a joke", "tell me something funny", "hilarious"],
              "responses": ["your mom", "just look in the mirror dude, and get a life while you're at it", "no"],
             },
			 {"tag": "breakup",
              "patterns": ["what's worse than a heartbreak", "i had a breakup", "my girlfriend broke up with me"],
              "responses": ["have you ever cheated on a test and still failed", "i guess its booze time now", "you can always go back to your ex", "I saw this coming way before", "she's probably with that blonde guy now"],
             },
			 {"tag": "stress",
              "patterns": ["I'm stressed", "when will this stress end", "I wanna die"],
              "responses": ["welcome to adulthood", "this is the worst you've felt ........ till now, just wait xD", "boy I'm glad to be a bot", "the only thing that stresses me out is you"],
             },
			 {"tag": "death",
              "patterns": ["what happens after death?", "what happens after we die?"],
              "responses": ["i know the ones who love us will miss us!"],
             },
			 {"tag": "pickup lines",
              "patterns": ["tell me a pickup line", "pickup line", "pick up line"],
              "responses": ["hey! are you a chocolate? 'cause I wanna eat you so bad"],
             }
]}

# initializing lemmatizer to get stem of words
lemmatizer = WordNetLemmatizer()
# Each list to create
words = []
classes = []
doc_X = []
doc_y = []
# Loop through all the intents
# tokenize each pattern and append tokens to words, the patterns and
# the associated tag to their associated list
for intent in data["intents"]:
	for pattern in intent["patterns"]:
		tokens = nltk.word_tokenize(pattern)
		words.extend(tokens)
		doc_X.append(pattern)
		doc_y.append(intent["tag"])
    
    # add the tag to the classes if it's not there already 
	if intent["tag"] not in classes:
		classes.append(intent["tag"])

    # lemmatize all the words in the vocab and convert them to lowercase
    # if the words don't appear in punctuation
	words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
    # sorting the vocab and classes in alphabetical order and taking the # set to ensure no duplicates occur
	words = sorted(set(words))
	classes = sorted(set(classes))
	
	# list for training data
	training = []
	out_empty = [0] * len(classes)
	# creating the bag of words model
	for idx, doc in enumerate(doc_X):
		bow = []
		text = lemmatizer.lemmatize(doc.lower())
		for word in words:
			bow.append(1) if word in text else bow.append(0)
		# mark the index of class that the current pattern is associated
		# to
		output_row = list(out_empty)
		output_row[classes.index(doc_y[idx])] = 1
		# add the one hot encoded BoW and associated classes to training 
		training.append([bow, output_row])
		
# shuffle the data and convert it to an array
np.random.shuffle(training)
training = np.array(training, dtype=object)
# split the features and target labels
train_X = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# defining some parameters
input_shape = (len(train_X[0]),)
output_shape = len(train_y[0])
epochs = 200
# the deep learning model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(output_shape, activation = "softmax"))
adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=["accuracy"])
print(model.summary())
model.fit(x=train_X, y=train_y, epochs=200, verbose=1)

def clean_text(text): 
	tokens = nltk.word_tokenize(text)
	tokens = [lemmatizer.lemmatize(word) for word in tokens]
	return tokens

def bag_of_words(text, vocab): 
	tokens = clean_text(text)
	bow = [0] * len(vocab)
	for w in tokens: 
		for idx, word in enumerate(vocab):
			if word == w: 
				bow[idx] = 1
	return np.array(bow)

def pred_class(text, vocab, labels): 
	bow = bag_of_words(text, vocab)
	result = model.predict(np.array([bow]))[0]
	thresh = 0.2
	y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]
	
	y_pred.sort(key=lambda x: x[1], reverse=True)
	return_list = []
	for r in y_pred:
		return_list.append(labels[r[0]])
	return return_list

def get_response(intents_list, intents_json): 
	tag = intents_list[0]
	list_of_intents = intents_json["intents"]
	for i in list_of_intents: 
		if i["tag"] == tag:
			result = random.choice(i["responses"])
			break
	return result

# running the chatbot
while True:
	message = input("User: ")
	intents = pred_class(message, words, classes)
	result = get_response(intents, data)
	print("Chatbot: "+result)
