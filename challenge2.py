import operator
from collections import Counter 
import sys
import webbrowser
import bs4
import requests
import os
#
#
#
# Author: Justin ossai
#


#Dictionary for word | Freq
dictionary_for_books = dict() 

#Declaring variables
num_of_books_to_search = 0
bts_input = ""
count = 0



def run_app():
    '''
    This function introduces the application and its relative methods for UI activity.
    This method prompts for user input. The first prompt takes in a numeric value to determine how many books will be referenced.
    The second prompt takes in a specific Books URL that is referenced from the website gutenberg.com.
    '''
    count = 0
    isTrue = True

    print("\nWelcome to the word frequency Application!\nReferenced below is a list of Book URLs from the gutenberg website that we can test in this application. Enjoy!!\n\n\nhttp://www.gutenberg.org/cache/epub/26348/pg26348.txt\nhttp://www.gutenberg.org/cache/epub/4602/pg4602.txt\nhttp://www.gutenberg.org/cache/epub/5741/pg5741.txt\nhttp://www.gutenberg.org/cache/epub/15167/pg15167.txt\nhttp://www.gutenberg.org/cache/epub/40894/pg40894.txt\n")
    while isTrue: 
        try:
            #Requests the user to enter a number for books to search through
            num_of_books_to_search = int(input("How many books do you want to search through? "))
            #loop will break once a valid input is entered (numeric values only)
            isTrue = False 
        #An exception will be thrown if the user inputs values that are not numeric
        except ValueError:
            print ("A numeric value was not entered. Please retry")
            

    #loops continue to request for book input based on the number of books needing to be searched, then adds it to the book dictionary
    while count < num_of_books_to_search:
        try:
            count +=1
            #Accepts user input for a numeric value to reference the number of books to check
            print("Enter the URL for book " + str(count) + ": ") 
            bts_input = input()
            check_freq_of_word_in_book(bts_input) 
        except Exception:
            print ("Book URL invalid. Nothing will return for " + bts_input + "\n")
            
    #Calling the output_word_and_freq() function to display the results
    output_word_and_freq(num_of_books_to_search)



def check_freq_of_word_in_book(the_book_URL):
    '''
    This method will take in a book paramater, then add its content into the dictionary_for_books
    '''
    #Creates a temp file(if not already present) to temporarly store the scraped data returned 
    temp_file = open("temp_file.txt", "w+")
    #Gettting the web scraped data based on the URL entered from the user
    temp_file.write(get_scraped_data(the_book_URL))
    #changed temp_file to read mode
    temp_file = open("temp_file.txt", "r")
    
    # Loop through each line of the text file 
    for line in temp_file: 
        # Remove the leading spaces and newline character 
        line = line.strip() 
    
        # Convert the characters in line to  
        # lowercase to avoid a case mismatch 
        line = line.lower() 
    
        # Split the line into words 
        words = line.split(" ") 

        # Iterate over each word in line 
        for word in words:
            #Checks each word in the list to see if it is an alpha character, not "", not an article of 'a', and not 'i'
            if word.isalpha and word != "a" and word != "i" and word != "" and word != "?" and word != "æ" and word != "*" and word != "," and word != "," and word != "." and word != '"' and word != "!" and word != "'" and word != "_" and word != "[" and word != "]" and word != "(" and word != ")"and word != "/" and word != "<" and word != ">" and word != "@" and word != "$" and word != "#" and word != "#" and word != "%" and word != "·" and word != ":" and word != ";" and word != "-":
                # Check if the word is already in dictionary 
                if word in dictionary_for_books: 
                    # Increment count of word by 1 
                    dictionary_for_books[word] = dictionary_for_books[word] + 1
                else: 
                    # Add the word to dictionary with count 1 
                    dictionary_for_books[word] = 1
            else:
                continue
    # closing, then removing temp file created for cleanup
    temp_file.close()
    os.remove("temp_file.txt")


def get_scraped_data(book_URL):
    '''
    This function accepts a book URL paramater. It takes the paramater, and returns the string. this function utilizes the Beautifulshop library
    '''
    r = requests.get(book_URL) 
    soup = str(bs4.BeautifulSoup(r.content, 'html5lib')) 
    return soup



def output_word_and_freq(the_book_count):
    '''
    This method outputs the word and frequency that is returned from dictionary_for_books. 
    '''
    k = Counter(dictionary_for_books)
    # Finding highest 10 values. Changing this number is dynamic to the application. Change it to whaterver number you like.  
    highest_values = k.most_common(10)

    
    print("\nWords with the highest frequency within the " + str(the_book_count) + " book(s)\n") 
    print("   Word   | Freq\n") 

    # Print the contents of dictionary 
    count = 0
    for i in highest_values:
        count +=1
        print(str(count) + ") " + i[0],"   : ", i[1], " ") 


if __name__ == '__main__':
    run_app()