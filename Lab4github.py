#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: To simulate a web browser
#
# Author: Matthew Mullen
# Collaborators/references:big na
#----------------------------------------------------

def getAction():
    '''
    Inputs: no arguments taken by this function.
    Returns: string containing users input if he has chosen one of the correct input options
    '''
    correct_input=False
    while correct_input==False:
        user_input=input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        if user_input =='q' or user_input =='>' or user_input =='<' or user_input =='=':
            correct_input=True
         
        if correct_input==False:
            print('Invalid entry.')
    return user_input
            
    
def goToNewSite(current, pages):
    '''
    Inputs: index of the current website (int), reference to list containing the webpage addresses to go back and forth between
    Returns: address inputted by user as a string
    '''
    
    new_web_address=input('Enter a new website address ')
    for i in range(current+1,len(pages)):
        pages.pop()
    pages.append(new_web_address)
    #pages[current+1]=new_web_address
    #pages=pages[:current+1]
    
    return current+1
    

    
def goBack(current, pages):
    '''
    Inputs: index of the current website (int),reference to list containing the webpage addresses to go back and forth between
    Returns: index of the previous webpage (int)
    '''
    # alternatively this could be done by checking if current-1>=0
    if current-1>=0:
        return current-1

    else:
        print('Cannot go backward')
        return current
    
    
    

def goForward(current, pages):
    '''
    Inputs: index of the current website (int),reference to list containing the webpage addresses to go back and forth between
    Returns: index of the previous webpage (int)
    '''  
    # alternatively this could be done by checking if current +1 in range(len(pages))
    if current+1<len(pages):
        return current+1

    else:
        print('Cannot go forward')
        return current
    
    


def main():
    '''
    Inputs: None
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
            
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()


# In[ ]:




