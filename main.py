import otp.otp as otp
from otp.print_blocks import print_text_blocks
import re
import unittest

from otp.otp import (
    one_time_pad,
    otp_encrypt,
    subtract_modulo_alphabet,
    add_modulo_alphabet,
)

def Create_Empty_List():
    """ creates a list with a 1000 dashes for each character """
    list = []
    for i in range(1000):
        list.append('-')
    return (list)

#three objects to keep track of the values for otp, M1 and M2 we have found so far
class Tracker:
    pass

tracker_otp = Tracker()
tracker_m1 = Tracker()
tracker_m2 = Tracker()
tracker_otp.list = Create_Empty_List()
tracker_m1.list = Create_Empty_List()
tracker_m2.list = Create_Empty_List()

def Update_List(tracker, string, index):
    """ updates the list of the tracker with the found character on a specific index """
    for i in range(len(string)):
        tracker.list[index+i] = string[i]

def Print_Updated(tracker):
    """ prints the list of the tracker  """
    print(tracker.list)

def Back_Up():
    """ makes a back up using deepcopy """
    Empty_List = copy.deepcopy(Empty_List)

def tracker_to_txt(trackerlist, filename):
    """ saves trackerlist as textfile for later use """
    with open(filename, "w") as txt:
        for char in trackerlist:
            txt.write("".join(char))
    
#Adding the Cyphertexts    
cyphertexta = open("cyphertext0.txt","r")
cyphertext1 = cyphertexta.read()

cyphertextb = open("cyphertext1.txt","r")
cyphertext2 = cyphertextb.read()

#Take the difference between the cyphertexts
d = subtract_modulo_alphabet(cyphertext2, cyphertext1)

def append_new_line(file_name, text_to_append):
    """Appends given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
        
def filteredsearch(d, guess, b):
    """tries a guess in all possible locations and removes all unwanted and 
    unrealistic words from the search output """
    with open("FilteredOutput.txt", "a") as text_file:
        text_file.write("This is the output of the filteredsearch function with the guess:")
    with open("FilteredOutput.txt", "a") as text_file:
        text_file.write(guess)
    for i in range(len(cyphertext1)):
        filteredtryout(d, guess, i, b)

def filteredtryout(d, guess, i, b): 
    """ outputs the fragment of the other text for your guess for one text. 
    If your guess is of a fragment in M1, put True. If your guess is of a 
    fragment in M2, put False. Filters the output"""
    if b: #this is the case when we are guessing that the word is in M1
        m2frag = add_modulo_alphabet(d[i:i+len(guess)], guess)
        if filtercharacters(m2frag) and filterspace(m2frag):
            output = str(i) + " " + m2frag
            print(output)
            append_new_line("FilteredOutput.txt", output)
    else: #this is the case when we are guessing that the word is in M2
        m1frag = subtract_modulo_alphabet(guess, d[i:i+len(guess)])
        if filtercharacters(m1frag) and filterspace(m1frag):
            output = str(i) + " " + m1frag
            print(output)
            append_new_line("FilteredOutput.txt", output)

# a string with characters unlikely to appear in a book
wrongcharacters = "@#$%^&*-_=+<>/|\\}][{1234567890"
# a string with characters after which there should be a space
spacecharacters = ".!?;:,"

def filtercharacters(output):
    """ returns False for all inputs with a character in wrongcharacters in it """
    for character in output:
        if character in wrongcharacters:
            return False
    else:
        return True
          
def filterspace(output):
    """ returns False for all inputs with capital letters that do not have
    a space in front and characters in spacecharacters that do not have a space 
    after it."""
    for i in range(len(output)-1):
        if output[i] != " " and output[i+1].isupper():
            return False
        if output[i+1] != " " and output[i] in spacecharacters:
            return False
    else:
        return True

class Testfilter(unittest.TestCase): 
    """ unittests for the filtercharacters and filterspace function """
    
    def setUp(self):
        pass
    
    def test_fc1(self): 
        self.assertEqual(filtercharacters('@hi'), False)
    
    def test_fc2(self): 
        self.assertEqual(filtercharacters('hey'), True)  
        
    def test_fs1(self): 
        self.assertEqual(filterspace(' Hi'), True)
    
    def test_fs2(self): 
        self.assertEqual(filterspace('Hey'), True)
    
    def test_fs3(self): 
        self.assertEqual(filterspace('eeH'), False)
    
    def test_fs4(self): 
        self.assertEqual(filterspace('e. '), True)
    
    def test_fs5(self): 
        self.assertEqual(filterspace('. e'), True)
        
    def test_fs6(self): 
        self.assertEqual(filterspace('e.e'), False)
        

if __name__ == '__main__':
    unittest.main()
