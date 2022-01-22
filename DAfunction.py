#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:21:19 2021

@author: olumide
"""

#import libraries
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import sqlite3

#Global variables

DB_NAME = 'ResultDatabase.db'
all_test = []
Df_tables = ['Test_1','Test_2','Test_3','Test_4','Test_mock','Sum_test']
grades = []

#connect and acess the  database and store tables in variables
def create_dfs(df_table):
    '''
    

    Parameters
    ----------
    df_table : LIST
    DESCRIPTION: This is the list of all the database tables

    Returns
    -------
    df : DATAFRAME
    DESCRIPTION: This is dataframe containing data from database  

    '''
    Title = df_table
    connection = sqlite3.connect(DB_NAME)
    df = pd.read_sql(f'SELECT * FROM {Title}',connection)
    connection.close()
    return df 

#set index and select assessment columns by dropping uneeded columns
def wrangle_dfs(df):
    '''
    

    Parameters
    ----------
    df : DATAFRAME
    DESCRIPTION: Dataframe returned from create_dfs function

    Returns
    -------
    df : DATAFRAME
    DESCRIPTION: The dataframe returned has a set index of 
    researchid and select test columns needed.
    '''
    df = df.set_index('researchid').iloc[:,4:]
    return df

#applying the functions to create necessary data frames
for i in Df_tables:
    df = create_dfs(i)
    df = wrangle_dfs(df)
    all_test.append(df)
#combine all assessment columns
all_test = pd.concat(all_test,axis = 1,keys=Df_tables)
#sorted index in descending order and fill missing values
all_test = all_test.sort_index(ascending=False).fillna(0)


#select grades column using all test from database
def select_grades_df(df):
    '''
    

    Parameters
    ----------
    df : DATAFRAMWE
    DESCRIPTION: This takes in dataframe

    Returns
    -------
    df : DATAFRAME
    DESCRIPTION: This return grades column for argument
    dataframe

    '''
    #set index and select grades column
    df = df.set_index('researchid').iloc[:,3]
    return df

#applying the function to create the  dataframe with grades columns only
for i in Df_tables:
    df = create_dfs(i)
    df = select_grades_df(df)
    grades.append(df)
#merging all the dataframes in the grade list
grades = pd.concat(grades,axis = 1,keys=Df_tables)\
    .sort_index(ascending=False).fillna(0)
    
#student rate loading and cleaning

#read csv and store in variable
studentrate = pd.read_csv('StudentRate.csv').set_index('research id')
#drop columns not needed
cols = [0,1,3,4,5,6]
studentrate.drop(studentrate.columns[cols],axis=1,inplace =  True)
#sort index and rename column header
studentrate.sort_index(ascending = False,inplace = True)
studentrate.rename({'What level programming knowledge do you have?'\
                           :'Skill level'},axis =1,inplace=True)
