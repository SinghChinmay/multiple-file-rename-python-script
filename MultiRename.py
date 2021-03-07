# Pythono3 Code by Studboo Senapi from Studboo.com
# To rename the file add xx11 in the number you want to rename.
# [Moozzi2] Given - 01 (BD 1920x1080 x.264 Flac).ass => [Moozzi2] Given - xx11 (BD 1920x1080 x.264 Flac).ass

# importing os module 
import os 
from pprint import pprint
import shutil
from shutil import copyfile


# Function to rename multiple files 
def main():
    i = 1
    directory = input("Enter the destination folder location : ")
    #Adding Slash in the end of the pathname
    if(directory[-1] != "\\"):
        directory = directory + '\\';
        if os.path.isdir(directory) == False:
            pprint ('Path is incorrect! Run script again.')
            exit(1)
    
    #Getting File Names
    pprint('File order below:')
    filenames = os.listdir(directory)
    pprint(filenames)

    #Check The File order
    check = input("Is the fileorder correct?(y/n)")

    

    if check == 'y' or check == 'Y':
        print("To rename the file add xx11 in the number you want to rename. mark number with xx11.\n\n[Moozzi2] Given - 01 (BD 1920x1080 x.264 Flac).ass => [Moozzi2] Given - xx11 (BD 1920x1080 x.264 Flac).ass\n\n")
        ################################ xx11 will repaced by numbers #################################
        fileN = input("make sure to add extensions :")
        for n in range(len(fileN)):
            
            if fileN[n] == 'x' and fileN[n+1] == 'x' and fileN[n+2] == '1' and fileN[n+3] == '1':
                s = fileN[:n]
                e = fileN[n+4:]
                
                
                for filename in filenames: 
                    dst =s + str(i) + e
                    dst1 = dst
                    if i < 10:
                        dst =s+'0' + str(i) + e 
                        dst1 = dst
                    src =directory+ filename 
                    dst =directory+ dst 
                    
                    # rename() function will rename all the files 
                    os.rename(src, dst) 
                    print(filename,'is replaced with :',dst1)
                    i += 1
    else:
        print("Exiting")
        exit()

    
    

# Driver Code 
if __name__ == '__main__': 
	pprint("Once renamed this cannot go back!!")
	# Calling main() function 
	main() 
