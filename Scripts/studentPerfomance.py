#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 01:24:26 2021

@author: olumide
"""
from DAfunction import *

def absolute_performance(test_title):
    '''
    Parameters
    ----------
    test_title : String
    DESCRIPTION: This is the title of the specific 
    test to be analysed.
    

    Returns
    -------
    test_score : Dataframe
    This returns a dataframe for selected test with
    absolute perfomance result of all students.
    
    '''
    #locate selected test and format scores to 2 decimal places
    test_score = all_test.loc[:,test_title]
    pd.options.display.float_format = "{:,.2f}".format
    return test_score

def relative_performance(test_title):
    '''
    Parameters
    ----------
    test_title : String
    DESCRIPTION: This is the title of the test to be analysed

    Returns
    -------
    test_score : Dataframe
    This returns a dataframe for selected 
    test with relative perfomance result of all students
    
    '''
    test_score = all_test.loc[:,test_title].copy()
    columns = list(test_score.columns)
    for i in columns:
        test_score[i + '_relative'] = test_score.loc[:,i] \
            - test_score.loc[:,i].mean()
        test_score.drop([i,],inplace = True,axis=1)
    pd.options.display.float_format = "{:,.2f}".format
    return test_score
    
#visualize relative and absolute performance    
def visualize_performance(abs_score,rela_score,test_title,researchid):
    '''
    Parameters
    ----------
    abs_score : Dataframe
    DESCRIPTION: Dataframe containing the absolute performance of 
    the deisred student id needed to be visualized
    rela_score : Dataframe 
    DESCRIPTION:  Dataframe containing the relative performance of 
    the deisred student id needed to be visualized
    test_title : String
    DESCRIPTION: Title of test to be visualized
    researchid : Integer
    DESCRIPTION: research id number of student to be visualized
    
    Function visualises the absolute and relative performance
    of a student for a selected test
    
    Returns
    -------
    None.

    '''
    
    width = 0.35
    x_axis_title = abs_score.columns.to_list()
    x_axis = np.arange(len(x_axis_title))
    y_axis = abs_score.values[0]
    y2_axis = rela_score.values[0]
    fig, ax = plt.subplots()
    ax.bar(x_axis,y_axis, width, label='absolute performance')
    ax.bar(x_axis + width, y2_axis, width, label='relative performance')
    ax.set_xticks(x_axis + width / 2)
    ax.set_xticklabels(x_axis_title)
    ax.legend(loc='best')
    plt.title(f'Perfomance of student with research no. {researchid} for {test_title}')
    plt.ylabel('Percentage grade (%)')
    plt.xlabel('Test questions')
    plt.show()

if __name__ == '__main__':
    test_title = input('Please enter test title: ')
    test_score_abs = absolute_performance(test_title)
    test_score_rela = relative_performance(test_title)
    student_id  = int(input('Enter student ID: '))
    abs_score = test_score_abs.loc[test_score_abs.index == student_id]
    rela_score = test_score_rela.loc[test_score_rela.index == student_id]
    visualize_performance(abs_score,rela_score,test_title,student_id)