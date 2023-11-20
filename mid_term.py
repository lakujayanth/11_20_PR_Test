import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#Import the WHO data set
mt_res_payment = pd.read_csv('Data/Midterm_data/chefmozaccepts.csv')
mt_res_cuisine = pd.read_csv('Data/Midterm_data/chefmozcuisine.csv')
mt_res_workhrs = pd.read_csv('Data/Midterm_data/chefmozhours4.csv')
mt_res_parking = pd.read_csv('Data/Midterm_data/chefmozparking.csv')
mt_rating = pd.read_csv('Data/Midterm_data/rating_final.csv')
mt_user_cuisine = pd.read_csv('Data/Midterm_data/usercuisine.csv')
mt_user_payment = pd.read_csv('Data/Midterm_data/userpayment.csv')
mt_user_profile = pd.read_csv('Data/Midterm_data/userprofile.csv')
mt_res_othinfo = pd.read_csv('Data/Midterm_data/geoplaces2.csv',encoding='ISO-8859-1')

