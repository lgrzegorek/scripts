"""
TL;DR 
python multipleReplace.py file_with_words_to_replace.txt
Script will return output file_with_words_to_replace_modified.txt
"""
import re
import sys
import os

def multipleReplace(text, wordDict):
    """
    take a text and replace words that match the key in a dictionary
    with the associated value, return the changed text
    """
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text

"""
create new out file by appending _modified word 
"""
str1=open(sys.argv[1]).read()
changed = open("%s_modified.txt" %(sys.argv[1].split(".")[0]), "w") 

wordDic = {
'192.168.1.0': 'VLAN 10',
'192.168.2.0': 'VLAN 20',
'192.168.3.0': 'VLAN 30'
}


str2 = multipleReplace(str1, wordDic)
changed.write(str2)
changed.close()
