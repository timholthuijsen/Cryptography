# Assignment3: The Lazy Cryptographer

Team Members:
Tim, Yosef, Sarah, Kamiel & Joella

###Approach
We know that C1 - C2 = M1 - M2, with C for cyphertext and M for original message. Lets call this difference d. If we add common English words such as ' the ' to d, and the result seems to be an English word fragment, this might be a correct guess. That is what we did, we tried out common words over the whole length of d, and printed out all the results, and see if any of them seem to make sense. If any of the results seemed to be a word fragment, we tried to complete that word by guessing, and seeing if the results for the other message also make sense. This way, we could expand our range of known characters. We also kept track of those characters we have already found out, for the otp and both the messages. 

###Files in Repository
####Instructions for searching
This file contains an instruction on how to search for new possible words.

####Tracker 1 & 2
These two files contain the decoded symbols of the two cyphertexts.

####Tried out words
Contains a list of the words that were already used as a guess.

####Working plan Ass3
Gives an overview of our team approach on the assignment. It describes the problem and what steps to take. Within these steps there is also a description of what functions need to be written.

####main.py
The main.py file contains the program that uses the two cyphertexts(m1 & m2) inorder to crack the One-time pad. The Program can be split up into three parts. The first part keeps track of the already decoded symbols. There are three trackers one for the otp, m1 and m2. The second part tries out words as a guess to see if the outcome makes sense. It guesses a word in m1 and outputs the result of m2. The third part contains filter functions that filters capitals and characters.

####Rest files
The cyphertext files contain the encrypted passages of the mystery book. Test.txt is merely a test file for an initial test commit.


###Result
The cyphertexts are encrypted passages of the book:
**Ulysses by James Joyce**