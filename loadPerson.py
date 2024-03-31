from libs.load import upload_file
import sys

people = sys.argv[1]
filePath = sys.argv[2]
upload_file(file_path=filePath, identification=people)
