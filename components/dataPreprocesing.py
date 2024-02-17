import pandas as pd
import ast

class dataPreprocessing:
    def __init__(self,dataframe) -> None:
        self.df = dataframe
        
    def convert(self,obj):
        L = []
        for i in ast.literal_eval(obj):
            L.append(i['name'])
            
        return L
    
    def convert2(self,obj):
        L = []
        counter = 0
        for i in ast.literal_eval(obj):
            if counter != 3:
                L.append(i['name'])
                counter += 1
            else:
                break
        return L  
    
    def fetch_director(self,obj):
        L = []
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
                
        return L 
     
    def preprocess(self):
        self.df['genres'] = self.df['genres'].apply(self.convert)
        self.df['keywords'] = self.df['keywords'].apply(self.convert)
        self.df['cast'] = self.df['cast'].apply(self.convert2)
        self.df['crew'] = self.df['crew'].apply(self.fetch_director)
        self.df['overview'] = self.df['overview'].apply(lambda x : x.split())
        self.df['genres'] = self.df['genres'].apply(lambda x: [i.replace(' ' , '') for i in x])
        self.df['keywords'] = self.df['keywords'].apply(lambda x: [i.replace(' ' , '') for i in x])
        self.df['cast'] = self.df['cast'].apply(lambda x: [i.replace(' ' , '') for i in x])
        self.df['crew'] = self.df['crew'].apply(lambda x: [i.replace(' ' , '') for i in x])
        self.df['tags'] = self.df['genres'] + self.df['keywords'] + self.df['cast'] + self.df['crew']
        new_df = self.df[['movie_id','title','tags']]
        new_df['tags'] = new_df['tags'].apply(lambda x : ' '.join(x))
        new_df['tags'] = new_df['tags'].apply(lambda x : x.lower())
        
        return new_df