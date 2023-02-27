"""
The shutil module in Python is a standard library that provides several high-level operations for copying and moving
files and directories. Some common use cases of the shutil module include:

1. Copying files and directories: You can use the shutil.copy() method to copy a single file,
and shutil.copytree() method to copy an entire directory.

2. Moving files and directories: You can use the shutil.move() method to move a file or a directory to a new location.
This method also works for renaming files or directories.

3. Removing files and directories: You can use the shutil.rmtree() method to remove a directory and its contents, and
the os.remove() method to remove a single file.

4. Archiving files and directories: You can use the shutil.make_archive() method to create an archive of a file or a
directory, with supported formats such as ZIP, TAR, and GZ.

"""
import shutil
import os

# Copy a file
shutil.copy('source_file.txt', 'destination_file.txt')

# Copy a directory
shutil.copytree('source_directory', 'destination_directory')

# Move a file
shutil.move('source_file.txt', 'new_location/new_file.txt')

# Remove a file
os.remove('file_to_remove.txt')

# Remove a directory
shutil.rmtree('directory_to_remove')

# Archive a file or directory
shutil.make_archive('archive_name', 'zip', 'source_directory')
