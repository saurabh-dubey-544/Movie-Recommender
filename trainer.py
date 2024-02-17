import pandas as pd
import streamlit as st
from components.dataCleaning import dataReading,dataCleaning
from components.dataPreprocesing import dataPreprocessing
from components.modelBuilding import modelTrainer
from helper import save_pickle

readData = dataReading("data/tmdb_5000_movies.csv","data/tmdb_5000_credits.csv")
df = readData.read_data()

cleanData = dataCleaning(df)
df = cleanData.clean_data()

dataPreprocess = dataPreprocessing(df)
df = dataPreprocess.preprocess()

trainer = modelTrainer(df)
similarity = trainer.calculate_similarity()

save_pickle(similarity,"model.pkl")
save_pickle(df,"new_df.pkl")
