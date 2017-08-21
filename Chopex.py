import os
import shutil
import pickle


try:
    Rawdef = pickle.load(open("default.p","rb"))
    print "Default path is set as " + Rawdef
except IOError:
    print "no default path set yet"

def changedir():
    #part of creating a complete experience is to think not only one instance of directory change
    print "1. Default"
    print "2. Other"
    Choices = input("Which path would you like to change? ")

    if Choices == 1:
        NewPath = raw_input("New Path: ")
        pickle.dump(NewPath,open("default.p","wb"))
        print NewPath + " has been setup as default path"
    if Choices == 2:
        File = raw_input("What file would you like to change?" )
        NewPath = raw_input("New Path: ")
        pickle.dump(NewPath,open(File + ".p","wb"))
        print NewPath + " has been setup as " + File + " path"


def copy():
        #1. Inputing all necessary things to do the copying. More intuitive.
        Filetype = raw_input("Specify File Type: ")
        Rawpath = raw_input("Enter Path: ")
        Filename = raw_input("Filename:")
        Destination = raw_input("Enter Destination: ")
        # 2. Using the choices of the user to do the copying
        if Rawpath == "" :
            shutil.copy(Rawdef + Filename + Filetype,Destination + Filename + Filetype)
            # additional input to help users open the files they copied, these are the command
            print 'start "" "' + Rawdef + Filename + Filetype + '"'
            print 'start "" "' + Destination + Filename + Filetype + '"'
        try:
            Rawsaved = pickle.load(open(Rawpath + ".p","rb"))
            shutil.copy(Rawsaved + Filename + Filetype,Destination + Filename + Filetype)
            print 'start "" "' + Rawsaved + Filename + Filetype + '"'
            print 'start "" "' + Destination + Filename + Filetype + '"'
        except IOError:
            shutil.copy(Rawpath + Filename + Filetype, Destination + Filename + Filetype)
            print 'start "" "' + Rawpath + Filename + Filetype + '"'
            print 'start "" "' + Destination + Filename + Filetype + '"'
        # 3. Allows the user to save the path so he/she can call that path faster next time.
        Loadopt = raw_input("Would you like to save path?(Y/N): ")
        if Loadopt == "Y":
            print "1. Save as Default"
            print "2. Custom Name"
            Number = input("Pick save point: ")

            if Number ==1:
                pickle.dump(Rawpath,open("default.p","wb"))
                print Rawpath + " has been setup as default path"
            if Number ==2:
                Savename = raw_input("Path name: ")
                pickle.dump(Rawpath,open(Savename + ".p","wb"))
