#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 01:16:01 2021

@author: olumide
"""
from DAfunction import *

#locates the student result using the input research id
def get_student_result(researchid):
    '''
    Parameters
    ----------
    researchid : Integer
    DESCRIPTION: Researchid is the student
    unique id to be analysed and visualized
    
    Function locate grades of input research id

    Returns
    -------
    student_result : Dataframe
    DESCRIPTION: student_result is the dataframe
    of the student with the inputted researchid
    
    '''
    #select rows where index(researchid) is equal to inputted researchid
    student_result = grades.loc[grades.index == researchid]
    #compiles all of the researchis grades
    student_result = grades.loc[researchid,:]
    #formats floats to 2 decimal points
    pd.options.display.float_format = "{:,.2f}".format
    return student_result 

# visualize student result
def visualize_result(Dfresult,researchid):
    '''
    Parameters
    ----------
    Dfresult : Dataframe
    DESCRIPTION:This is the dataframe returned from the 
    student_result function and visualized using
    matplotlib.
    
    researchid : Integer
    DESCRIPTION:This is the research id number of the 
    student to be analysed.

    Function visualises the test results
    
    Returns
    -------
    None.
    '''
    x_axis  = Dfresult.index.tolist()
    y_axis  = Dfresult.tolist()
    plt.plot(x_axis,y_axis,'-ok')
    plt.title(f'Grades for student with research number {researchid}')
    plt.ylabel('Percentage grades (%)')
    plt.xlabel('Tests')
    plt.ylim(0, 105)
    plt.show()


if __name__ == '__main__':
    researchid = int(input('Please enter researchid: '))
    result = get_student_result(researchid)
    print(result)
    visualize_result(result,researchid)