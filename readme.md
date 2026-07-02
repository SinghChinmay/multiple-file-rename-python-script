# MultiRename.py

A Python script to batch rename multiple files in a directory using a numbered template.

## Requirements

- Python 3

## Usage

```bash
python MultiRename.py
```

1. Enter the path to the folder containing the files you want to rename.
2. Review the displayed file order and confirm.
3. Enter a filename template using `xx11` as a placeholder for the incrementing number (zero-padded to 2 digits).
4. Files are renamed sequentially — `xx11` becomes `01`, `02`, `03`, etc.

## Example

**Before:** A folder with inconsistently named files:

```
IMG_8492.jpg
IMG_8501.jpg
IMG_8510.jpg
photo1.png
photo10.png
photo2.png
```

**Run the script:**

```
Warning: Once renamed, this cannot be undone!!

Enter the destination folder location : /home/user/vacation-photos

File order below:
IMG_8492.jpg
IMG_8501.jpg
IMG_8510.jpg
photo1.png
photo10.png
photo2.png

Is the file order correct? (y/n) y

Enter new filename template (make sure to add extensions): Vacation xx11.jpg

IMG_8492.jpg is replaced with : Vacation 01.jpg
IMG_8501.jpg is replaced with : Vacation 02.jpg
IMG_8510.jpg is replaced with : Vacation 03.jpg
photo1.png is replaced with : Vacation 04.jpg
photo10.png is replaced with : Vacation 05.jpg
photo2.png is replaced with : Vacation 06.jpg
```

**After:** All files renamed cleanly:

```
Vacation 01.jpg
Vacation 02.jpg
Vacation 03.jpg
Vacation 04.jpg
Vacation 05.jpg
Vacation 06.jpg
```

## Template rules

- `xx11` is **required** in the template — it will be replaced with `01`, `02`, `03`, ...
- Include the file extension at the end of the template (e.g., `.jpg`, `.png`).
- Numbers are always zero-padded to 2 digits.
