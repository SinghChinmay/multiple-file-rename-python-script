# Python3 Code to rename multiple files in a directory
# Author: Studboo Senapi from Studboo.com

import os
import sys

def main():
    directory = input("Enter the destination folder location : ")
    directory = os.path.normpath(directory) + os.sep  # Normalize path and add separator

    if not os.path.isdir(directory):
        print('Path is incorrect! Run script again.')
        sys.exit(1)

    print('File order below:')
    filenames = sorted(os.listdir(directory))
    print('\n'.join(filenames))

    check = input("Is the file order correct? (y/n)").lower()
    if check != 'y':
        print("Exiting")
        sys.exit()

    print("To rename the file, add xx11 in the number you want to rename. For example:\n\n[Moozzi2] Given - 01 (BD 1920x1080 x.264 Flac).ass => [Moozzi2] Given - xx11 (BD 1920x1080 x.264 Flac).ass\n\n")
    fileN = input("Enter new filename template (make sure to add extensions): ")

    if 'xx11' not in fileN:
        print("Invalid template. Please include 'xx11' in your template.")
        sys.exit()

    prefix, suffix = fileN.split('xx11')

    for i, filename in enumerate(filenames, start=1):
        new_name = f"{prefix}{str(i).zfill(2)}{suffix}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)
        print(f"{filename} is replaced with : {new_name}")

if __name__ == '__main__':
    print("Warning: Once renamed, this cannot be undone!!")
    main()