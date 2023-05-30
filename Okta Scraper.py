
#### No License Has been assigned. Please ask if this can be shared

## Parsing Data
#### Given a user who has individual permissions assigned to them, extract the groups of the user from the HTML Data
#### The purpose of this is to scrape a Given portion of Okta to get the Permission Sets for a User making it easier to copy and Paste
#### Author: JoJo (Jordan) Kirkwood

import  re,pyperclip
from time import sleep



def contentExtraction(clipboard_content):
    ## This function is for using regular expressions to get the Permission Sets and return them as a list 
    Ogroups=re.compile(r">\w+<")
    secondPass=re.compile(r"\w+")
    fileEX="DataExtracted"
    with open(fileEX,"w+") as FWrite:
        FWrite.write(clipboard_content)
    for line in open(fileEX,"r"):
        result=re.findall(Ogroups,line)   
    if len(result) != 0:
        extractedGroups=[] 
        for groupName in result:
            extractedGroups.append(re.findall(secondPass,groupName)[0])        
        print("\n\t\tPreview of groups added that will be checked:\n",extractedGroups,"\n\n")
        #
        return extractedGroups



def controlledPaste(content,):
    ## This Function is used for Copying Each of the Okta Groups, one-by-one into the clipboard to paste
    curIndex=0
    ccount=len(content)
    while curIndex < (ccount):
        input("\nWaiting for user to press ENTER to copy the next Permission Set Group to clipboard\n")
        toclipboard=content[curIndex]
        pyperclip.copy(toclipboard)        
        print (f"{toclipboard} has just been copied.  [{curIndex+1}/{ccount}]")
        curIndex += 1 
        sleep(.5)
    if ccount !=0 :
        print(f"\n\n\t\t All {ccount} Permission Set Groups have been Copied. Exiting the Program.......\n\n")

def comparerator(Mcontent,Ucontent):
    Mset=set()
    Uset=set()
    try:
        for group in Mcontent:
            Mset.add(group)
        for group in Ucontent:
            Uset.add(group)
        
        dList=list(Mset.difference(Uset))
        dList.sort()
        if len(dList) != 0:        
            print ("\n\tMISSING PERMISSIONS FOUND!! \n\tThe Permissions that are assigned to the User 1 that are not assigned to User 2 are listed as follows:\n\t\t",dList,"\n\n")
            controlledPaste(dList)
        elif (len(dList) == 0)&(len(Ucontent)>len(Mcontent)):
            print("\n\nAll of the permissions from the MIRROR are already assigned to the USER. You may have copied the Permission Sets in the wrong order.\nQuitting Program\n\n")
        elif (len(dList) == 0):
            print("\nPARITY ACHIEVED: All of the permissions from the MIRROR are already assigned to the USER. Only using the Permission Sets of the Mirror")
            continuePaste=input("\n\t\tWould you like to continue?? [Press y  ENTER to continue. Any Other key will quit the program]")
            try:
                if continuePaste == "y":
                    controlledPaste(list(Mset))
            except: 
                print("Nice Job Syncing The Permission Sets. Closing Program\n\n")
        else:
            print("An Unusual Error Occurred. Quitiitng Program")
    except:
        print("\n\nError with copying groups.Try to restart the program and follow the instructions\n\n")
        
if __name__=="__main__":
    print ("Welcome to the Okta Group Extraction for Permission Sets")
    print("\n\nWhen you are ready press ENTER to paste the Data of the MIRROR")
    input("\t\tPress ENTER to continue...")    
    clipboard_content = pyperclip.paste() # Use F12 to copy the Permission Sets, and assign the data to this variable
    Mcontent=contentExtraction(clipboard_content)  #Extract the needed information from the HTML Format with this Function
    print("\n\nWhen you are ready press ENTER to paste the Data of the USER")
    input("\t\tPress ENTER to continue...")    
    clipboard_content = pyperclip.paste() # Use F12 to copy the Permission Sets, and assign the data to this variable
    Ucontent=contentExtraction(clipboard_content)  #Extract the needed information from the HTML Format with this Function
    compareContent=comparerator(Mcontent,Ucontent)
    