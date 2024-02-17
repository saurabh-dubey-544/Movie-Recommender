import pandas as pd

class dataReading:
    def __init__(self,movies_path,credits_path):
        self.movies_path = movies_path
        self.credits_path = credits_path
    def read_data(self):
        movies = pd.read_csv(self.movies_path)
        credits = pd.read_csv(self.credits_path)
        
        movies = movies.merge(credits,on="title")
        return movies
    

class dataCleaning:
    def __init__(self,dataframe:pd.DataFrame):
        self.df = dataframe
        
    def clean_data(self):
        self.df = self.df[['movie_id' , 'title' , 'overview' , 'genres', 'keywords' , 'cast' , 'crew' ]]
        self.df.dropna(inplace=True)
        
        return self.df
        
        