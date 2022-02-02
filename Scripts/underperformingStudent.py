#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:52:38 2022

@author: olumide
"""

from DAfunction import *


def find_underperforming(grades):
    '''
    Parameters
    ----------
    grades : Dataframe
    DESCRIPTION: This dataframe contains grades for all formative and 
    summative test for each researchid.
    
    Function drops disengaged students and returns underperforming
    students
    
    Returns
    -------
    sumtest_check : Dataframe
    DESCRIPTION: This dataframe contains all underperforming students.
    
    '''
    #create new colum containing lowest formative test score
    grades['lowest_formative_test_score'] = grades.iloc[:,0:4].min(axis=1)
    #check and exclude disengaged student
    disengaged = grades[grades[grades[['Test_1','Test_2','Test_3','Test_4']]==0]\
                        .count(axis=1) > 3 ]
    disengaged_list = disengaged.index.tolist()
    grades.drop(disengaged_list,axis=0,inplace=True)
    #check that average of all formative grades is less than 50
    ftest_check = grades.loc[grades.iloc[:,0:4].mean(axis = 1) < 50]
    #check that summative grade is less than 50
    sumtest_check = ftest_check.loc[ftest_check.loc[:,'Sum_test'] < 50]
    sumtest_check.sort_values('Sum_test', ascending=True,inplace = True)
    #reset index to create a researchid column
    sumtest_check.reset_index(inplace=True)
    #format float to 2 decimal places
    pd.options.display.float_format = "{:,.2f}".format
    return sumtest_check

    
if __name__ == '__main__':
    display = find_underperforming(grades).copy()
    print(display)