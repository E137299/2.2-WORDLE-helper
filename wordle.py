'''
Import New York Times' wordbank
'''
words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.

