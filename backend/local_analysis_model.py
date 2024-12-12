import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix



#Read the data
df=pd.read_csv('dataset/news.csv')

#Get shape and head
df.shape
df.head()

# Get the labels
labels=df.label
labels.head()

# Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

# Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

d_test=tfidf_vectorizer.transform(["Krunal Pandya was too good in Pushpa 2."])

# Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

# Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)

def askLocal(data):
    print(data)
    analysis_result = []
    for i in data:
        print(i)
        transformed_txt = tfidf_vectorizer.transform([i["text"]])
        prediction = pac.predict(transformed_txt)
        result = {
            "id": i["id"],
            "text": i["text"],
            "result":{
                "sentiment_analysis": "",
                "is_fake": True if prediction[0] == "FAKE" else False,
                "sources":[]
            }
        }
        analysis_result.append(result)
    
    return analysis_result


# let tweet = {
#     id: for identifying in the page, 
#     txt: text of the tweet,
#     result: {
#         sentiment_analysis: "",
#         is_fake: bool, 
#         sources: [
#             "source1",
#             "source2",
#             "source3"
#         ]
#     }
# }




# score=accuracy_score(y_test,y_pred)
# print(f'Accuracy: {round(score*100,2)}%')

# # Build confusion matrix
# confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])