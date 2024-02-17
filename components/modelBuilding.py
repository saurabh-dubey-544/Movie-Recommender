import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class modelTrainer:
    def __init__(self,dataframe:pd.DataFrame):
        self.df = dataframe
        
    def stem(self,text):
        ps = PorterStemmer()
        y = []
        
        for i in text.split():
            y.append(ps.stem(i))
            
        return " ".join(y)

    def calculate_similarity(self):
        cv = CountVectorizer(max_features=5000 , stop_words='english')
        vectors = cv.fit_transform(self.df['tags']).toarray()
        self.df['tags'] = self.df['tags'].apply(self.stem)
        similarity = cosine_similarity(vectors)
        return similarity