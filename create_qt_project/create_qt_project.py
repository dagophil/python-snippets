import sys
import os

# Check input arguments.
assert len(sys.argv) >= 3, "Usage: python create_qt_project.py sourcefolder projname.pro"
folder = sys.argv[1]
proj_filename = sys.argv[2]
assert os.path.isdir(folder), folder + " is not a folder."
proj_dir = os.path.dirname(os.path.join(folder, proj_filename))

# Create the lists with header and source files.
header_list = ["HEADERS += \\"]
source_list = ["SOURCES += \\"]

# Walk trough the given directory and add the .hxx and .cxx files.
print "Reading contents of", folder
for dir_name, subdir_list, file_list in os.walk(folder):
    for file_name in file_list:
        file_path = os.path.relpath(os.path.join(dir_name, file_name), proj_dir)
        file_ext = os.path.splitext(file_path)[1]
        if file_ext in [".hxx", ".hpp", ".h"]:
            header_list.append("    " + file_path + " \\")
        if file_ext in [".cxx", ".cpp", ".c"]:
            source_list.append("    " + file_path + " \\")

# Show some output and ask if the file shall really be created.
print "Found", len(header_list)-1, "header files."
print "Found", len(source_list)-1, "source files."
user_input = raw_input("Are you sure you want to create " + os.path.abspath(proj_filename) + "? [y|n] ")
if not user_input in ["y", "Y"]:
    print "Aborting. No files were created."
    sys.exit()

# Create the strings that are to be written.
header_string = os.linesep.join(header_list)
source_string = os.linesep.join(source_list)

# Create the project directory.
if not os.path.isdir(proj_dir):
    os.makedirs(proj_dir)

# Write the project file.
with open(proj_filename, "w") as proj_file:
    proj_file.write(header_string + os.linesep)
    proj_file.write(os.linesep)
    proj_file.write(source_string + os.linesep)

print "Success, output written to", proj_filename
