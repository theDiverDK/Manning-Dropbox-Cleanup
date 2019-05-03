import os
import datetime
import re


def GetFiles(path):
    result = {}

    for r, d, f in os.walk(path):

        for directory in d:
            path = os.path.join(r, directory)

            for root, directories, files in os.walk(path):
                filesInDirectory = []

                for file in files:
                    timestamp = os.path.getmtime(os.path.join(root, file))
                    filesInDirectory.append(os.path.join(root, file))

            result[path] = sorted(filesInDirectory, key=os.path.getmtime, reverse=True)

    return result


def DeleteFiles(files, extension):
    for key, value in files.items():
        filteredFiles = [file for file in value if extension in file]
        
        for file in filteredFiles[1:]:
            os.remove(file)
            print("Deleted: ", file)


def RenameFile(files, extension):
    for key, value in files.items():
        filteredFiles = [file for file in value if extension in file]
   
        if(len(filteredFiles) == 0):
            continue

        oldFilename = filteredFiles[0]
        newFilename = re.sub('\s\([0-9]\)', '', oldFilename)
     
        if(oldFilename != newFilename):
            os.rename(oldFilename, newFilename)
            print("Renamed: ", oldFilename, " -> ", newFilename)


def main():
    files = GetFiles("Books")

    DeleteFiles(files, "pdf")
    RenameFile(files, "pdf")

    DeleteFiles(files, "mobi")
    RenameFile(files, "mobi")

    DeleteFiles(files, "epub")
    RenameFile(files, "epub")

if __name__ == "__main__":
    main()
