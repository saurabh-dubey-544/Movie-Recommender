import pickle

def save_pickle(model,filename):
    with open(filename,"wb") as f:
        pickle.dump(model,f)
        
def load_pickle(pickle_file:pickle):
    with open(pickle_file,"rb") as f: 
        return pickle.load(f)
    
def movie_list(df)->list:
    return sorted(list(df["title"].values))