from os import listdir
from os.path import isdir, isfile, join
import sys
from libs.load import upload_file

directory = sys.argv[1]

if isdir(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for f in onlyfiles:
        upload_file(identification=f.split('.')[0], file_path=join(directory, f))
else:
    print(f"{directory} isn't a directory")
