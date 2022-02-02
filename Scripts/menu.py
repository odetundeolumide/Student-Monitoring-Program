#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:23:00 2022

@author: olumide
"""

from DAfunction import *
import studentPerfomance as sp
import testResults as test
from underperformingStudent import *
from hardworkingStudents import Hardworking
from tkinter import *

def hard_work():
    '''
    displays hardworking student in GUI

    Returns
    -------
    None.

    '''
    
    #displaying previous and next buttons
    table_previous_button.grid(row=2, column=1)
    table_next_button.grid(row=2, column=2)
    #display column headers
    hard_researchid_column.grid(row=3,column=0)
    hard_summative_column.grid(row=3,column=1)
    hard_level_column.grid(row=3,column=2)
    #calling global variables
    global offset, curr_dataframe
    #calling the hardworking function
    output = Hardworking(grades, studentrate)
    #setting current datafrme
    curr_dataframe = output
    #display hardworking students
    table_display(offset=offset, curr_df=output)

def exit_():
    window.destroy()
    
def quit_():
    '''
    Clears the screen after clicking the clear
    button in GUI

    Returns
    -------
    None.

    '''
    #hide all widgets 
    researchid_label.grid_forget()
    researchid_entry.grid_forget()
    researchid_search_button.grid_forget()
    researchid_label2.grid_forget()
    researchid_entry2.grid_forget()
    researchid_search_button2.grid_forget()
    test_label.grid_forget()
    test_entry.grid_forget()
    table_previous_button.grid_forget()
    table_next_button.grid_forget()
    hard_researchid_column.grid_forget()
    hard_summative_column.grid_forget()
    hard_level_column.grid_forget()
    under_researchid_column.grid_forget()
    under_test1_column.grid_forget()
    under_test2_column.grid_forget()
    under_test3_column.grid_forget()
    under_test4_column.grid_forget()
    under_testmock_column.grid_forget()
    under_sumtest_column.grid_forget()
    input_explanation.grid_forget()
    under_lowestscore_column.grid_forget()
    
    # clear table entries if they exist
    global table_entries
    if len(table_entries) > 0:
        # list is not empty. clear it
        for t_entry in table_entries:
            #destroy widget
            t_entry.destroy()
        del table_entries
        table_entries = []
    
def under_perform():
    '''
    displays underperforming students

    Returns
    -------
    None.

    '''
    #display column headers
    under_researchid_column.grid(row=3,column=0)
    under_test1_column.grid(row=3,column=1)
    under_test2_column.grid(row=3,column=2)
    under_test3_column.grid(row=3,column=3)
    under_test4_column.grid(row=3,column=4)
    under_testmock_column.grid(row=3,column=5)
    under_sumtest_column.grid(row=3,column=6)
    under_lowestscore_column.grid(row=3,column=7)

    #calling global variables
    global offset,curr_dataframe
    #calling the underperforming function
    output = find_underperforming(grades)
    #display underperforming students
    table_display(offset=offset, curr_df=output)
    
def abs_and_rela_display():
    '''
    displays the labels,entry and button needed
    to execute abs_and_rela(absolute and relative and 
    relative function)

    Returns
    -------
    None.

    '''
    #show labels entry and button needed for absolute and 
    #relative performance
    input_explanation.grid(row =2,column=1,columnspan=6)
    researchid_label2.grid(row=4, column=1)
    researchid_entry2.grid(row=4, column=2)
    researchid_search_button2.grid(row=4, column=3)
    test_label.grid(row=3,column=1)
    test_entry.grid(row=3,column=2)
    
def abs_and_rela():
    '''
    displays the absolute and relative performance
    for input test and researchid

    Returns
    -------
    None.

    '''
    #get test title
    test_title = (test_entry.get())
    #derive absolute and test score using function from student peformance
    test_score_abs = sp.absolute_performance(test_title)
    test_score_rela = sp.relative_performance(test_title)
    #get student it
    student_id  = int(researchid_entry2.get())
    #locate absolute and relative test score for inputted research id
    abs_score = test_score_abs.loc[test_score_abs.index == student_id]
    rela_score = test_score_rela.loc[test_score_rela.index == student_id]
    #visualize absolute and relative performance
    sp.visualize_performance(abs_score,rela_score,test_title,student_id)
    
def grade_viz_display():
    '''
    display necessary buttons ,labels and entry needed
    to execute grade_viz(the function that displays test
    results)
    
    Returns
    -------
    None.

    '''
    #display necessary label,button and entry 
    researchid_label.grid(row=3, column=1)
    researchid_entry.grid(row=3, column=2)
    researchid_search_button.grid(row=3, column=3)
    
def grade_viz():
    '''
    displays the test results of the input
    research id

    Returns
    -------
    None.

    '''
    #convert entry box item to integer
    research_id = int(researchid_entry.get())
    #obtain result of input researchid
    result = test.get_student_result(research_id)
    #visualize the result
    test.visualize_result(result,research_id)
 
def prevous_button_clicked():
    '''
    moves page to the previous page

    Returns
    -------
    None.

    '''
    global offset, curr_dataframe
    # update offset
    offset -= 1
    
    # call table_display
    table_display(offset, curr_dataframe)

def next_button_clicked():
    '''
    moves page to the next page

    Returns
    -------
    None.

    '''
    global offset, curr_dataframe
    # update offset
    offset += 1
    # call table_display
    table_display(offset, curr_dataframe)

def table_display(offset, curr_df, tk_row_start_pos=4):
    '''
    

    Parameters
    ----------
    offset : TYPE
        DESCRIPTION.
    curr_df : TYPE
        DESCRIPTION.
    tk_row_start_pos : INTEGER, optional
    DESCRIPTION. The default is 4.

    Returns
    -------
    None.

    '''
    # check if offset is now zero. If so, disable back button
    if offset == 0:
        table_previous_button['state'] =  'disabled'
    else:
        table_previous_button['state'] =  'normal'
    # fetch batch of data to display from current data using offset/page
    start_idx = offset * num_rows_per_page
    end_idx = start_idx + num_rows_per_page
    data = curr_df.iloc[start_idx : end_idx]
    
    # display data
    for i in range(len(data)):

        row_data = data.iloc[i]
        for j in range(len(row_data)):
            if type(row_data[j]) is str:
                e = Entry(window, width=11)
            else:
                e = Entry(window, width=5)
            e.grid(row=tk_row_start_pos+i, column=j)
            # if type(row_data[j]) is np.float64 or type(row_data[j]) is np.float32:
            if type(row_data[j]) is np.float64:
                e.insert(END, np.round(row_data[j], 2))
            else:
                e.insert(END, row_data[j])
            table_entries.append(e)

# declaring global variables
offset = 0
num_rows_per_page = 10
curr_dataframe = None
table_entries = []

#Setting window 
window = Tk()
window.title('Student Monitoring System')
window.geometry('525x400')

#Defining buttons
graph_viz_button = Button(window, text='Test',command=grade_viz_display)
perf_button = Button(window, text= 'Perf',command=abs_and_rela_display)
under_perf_button = Button(window, text= 'Under',command = under_perform)
hardwork_button = Button(window, text= 'Hard',command = hard_work) 
exit_button = Button(window, text = 'Exit',command=exit_)
clear_scr_button = Button(window,text='Clear',command=quit_)
table_previous_button = Button(window, text='<<<',\
                               command=prevous_button_clicked)
table_next_button = Button(window, text='>>>',command=next_button_clicked)
researchid_search_button = Button(window, text="search", command=grade_viz)
researchid_search_button2 = Button(window, text="search", \
                                   command=abs_and_rela)
test_search_button2 = Button(window, text='search', command=abs_and_rela)


#Defining labels
researchid_label = Label(window, text="Research ID")
researchid_label2 = Label(window, text="Research ID")
test_label = Label(window, text="Test")
hard_researchid_column = Label(window,text='ID')
hard_summative_column = Label(window,text='Sum\ntest')
hard_level_column = Label(window,text='Level')
under_researchid_column = Label(window,text='ID')
under_test1_column = Label(window,text='Test1')
under_test2_column = Label(window,text='Test2')
under_test3_column = Label(window,text='Test3')
under_test4_column = Label(window,text='Test4')
under_testmock_column = Label(window,text='Test\nmock')
under_sumtest_column = Label(window,text='Sum\ntest')
under_lowestscore_column = Label(window,text='Lowest\nscore')
input_explanation = Label(window,text = 'Test: [Test_1, Test_2, Test_3, Test_4, Test_mock, Sum_test]')

#Defining Entries
researchid_entry = Entry(window, width=10)
researchid_entry2 = Entry(window, width=10)
test_entry = Entry(window, width=10)

#Position necessary widgets
graph_viz_button.grid(row=0,column=0)
perf_button.grid(row=0,column=1)
under_perf_button.grid(row=0,column=2)
hardwork_button.grid(row=0,column=3)
exit_button.grid(row=0,column=6)
clear_scr_button.grid(row=0,column=5)


#hiding necessary label,entry and buttons
researchid_label.grid_forget()
researchid_entry.grid_forget()
researchid_search_button.grid_forget()
researchid_label2.grid_forget()
researchid_entry2.grid_forget()
researchid_search_button2.grid_forget()
test_label.grid_forget()
test_entry.grid_forget()
table_previous_button.grid_forget()
table_next_button.grid_forget()
hard_researchid_column.grid_forget()
hard_summative_column.grid_forget()
hard_level_column.grid_forget()
under_researchid_column.grid_forget()
under_test1_column.grid_forget()
under_test2_column.grid_forget()
under_test3_column.grid_forget()
under_test4_column.grid_forget()
under_testmock_column.grid_forget()
under_sumtest_column.grid_forget()
under_lowestscore_column.grid_forget()
input_explanation.grid_forget()


window.mainloop()
