#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:39:25 2022

@author: olumide
"""

from DAfunction import *

def Hardworking(grades,studentrate):
    '''
    Parameters
    ----------
    grades : Dataframe
    DESCRIPTION: This the dataframe that contains all grades for each 
    researchid for all test
    studentrate : Dataframe
    DESCRIPTION : This dataframe contains programming skill level
    for all researchid
    
    Function selects research id with skill level of beginner or below
    beginner and summative test score of above 60. 

    Returns
    -------
    Dfcombined: Dataframe
    DESCRIPTION: Dataframe that holds all the rsearchid with summative grade
    score above 60 and programming skill level of beginner or below beginner.
    
    '''
    #join the student rate dataframe to the grade dataframe
    Dfcombined = grades.merge(studentrate,left_index=True,right_index=True)
    #check if the summative grade is above 60 
    #and studentrate is beginner or below beginner
    Dfcombined = Dfcombined.loc[(Dfcombined.iloc[:,5].values > 60) & \
                                ((Dfcombined.iloc[:,6] == 'Beginner') | \
                                (Dfcombined.iloc[:,6] == 'Below beginner'))]
    #drop unnecessary test score columns
    test_list_drop = [0,1,2,3,4]
    Dfcombined.drop(Dfcombined.columns[test_list_drop],axis =  1,inplace = True)
    #sort sum test grades in descending order
    Dfcombined.sort_values('Sum_test', ascending=False,inplace = True)
    #reset index to create a researchid column
    Dfcombined.reset_index(inplace=True)
    Dfcombined.rename({'index':'researchid'},axis=1,inplace=True)
    #format float to 2 decimal places
    pd.options.display.float_format = "{:,.2f}".format
    return(Dfcombined)

if __name__ == '__main__':
    hardworking_students = Hardworking(grades, studentrate)
    print(hardworking_students)