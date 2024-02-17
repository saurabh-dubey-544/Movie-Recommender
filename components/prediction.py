class modelPrediction:
    def __init__(self,dataframe,similarity):
        self.similarity = similarity
        self.dataframe = dataframe
        
    def recommend(self,movie):
        movie_index = self.dataframe[self.dataframe['title'] == movie].index[0]
        distances = self.similarity[movie_index]
        
        movies_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x:x[1])[1:6]
        predicted_movies = []
        for i in movies_list:
            predicted_movies.append(self.dataframe.iloc[i[0]].title)
            
        return predicted_movies