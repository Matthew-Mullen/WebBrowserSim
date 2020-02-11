#!/usr/bin/env python
# coding: utf-8

# In[1]:


#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Write docstring to describe function
    Inputs: no arguments taken by this function.
    Returns: string containing users input if he has chosen one of the correct input options.
    '''

            
    correct_input=False
    while correct_input==False:
        user_input=input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        if user_input =='q' or user_input =='>' or user_input =='<' or user_input =='=':
            correct_input=True
         
        if correct_input==False:
            raise Exception('Invalid entry.')
    return user_input
        


def goToNewSite(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: current website (str), a reference to the Stack holding the webpage addresses to go back to, and a reference to the Stack holding the webpage addresses to go forward to.
    Returns: web address as a string
    '''   
    new_web_address=input('Enter a new website address ')
    fwd.clear()
    
    bck.push(current)
    return new_web_address
    
def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: current website (str), a reference to the Stack holding the webpage addresses to go back to, and a reference to the Stack holding the webpage addresses to go forward to.
    Returns: the current site as a string
    '''    
    
    try:
        #fwd.push(current)
        #bck.pop()
        #fwd.push(current)
        temp=bck.pop()
    except:
        print('Cannot go backward')
        return current
    else:
        fwd.push(current)
        return temp
    
    
    

def goForward(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    
    try:
        
        temp2=fwd.pop()
    except:
        print('Cannot go forward')
        return current
    else:
        bck.push(current)
        return temp2
        


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            elif action == '<':
                current = goBack(current, back,forward)
            elif action == '>':
                current = goForward(current, back,forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()


# In[ ]:




