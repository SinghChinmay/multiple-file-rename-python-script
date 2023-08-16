# MultiRename.py

This script is used to rename multiple files in a directory according to a specific pattern.

## Usage

1. Run the script: `python MultiRename.py`
2. When prompted, enter the destination folder location.
3. The script will display the current file order. Confirm if the order is correct.
4. If the order is correct, enter the new filename template. Make sure to include 'xx11' in the template where you want the file number to appear. Also, don't forget to include the file extension.

## Example

```

> python MultiRename.py
> Warning: Once renamed, this cannot be undone!!
> Enter the destination folder location : C:\\Studboo\\test
> File order below:
> apple 01.jpg
> apple 02.jpg
> ...
> Is the file order correct? (y/n) y
> To rename the file, add xx11 in the number you want to rename. For example:
> \[Moozzi2\] Given - 01 (BD 1920x1080 x.264 Flac).ass => \[Moozzi2\] Given - xx11 (BD 1920x1080 x.264 Flac).ass
> Enter new filename template (make sure to add extensions): apple xx11.jpg
> apple 01.jpg is replaced with : apple 01.jpg
> apple 02.jpg is replaced with : apple 02.jpg
> ...

```

## Issues

If you encounter any issues, please report them.
