import os
import datetime


def GetFiles(path):
    result = {}

    for r, d, f in os.walk(path):
        for directory in d:
            path = os.path.join(r, directory)

            for root, directories, files in os.walk(path):
                filesInDirectory = []

                for file in files:
                    filesInDirectory.append(file)

            result[path] = filesInDirectory

    return result


def FilesToRemove(files, extension):
    for key, value in files.items():
        filteredFiles = [file for file in value if extension in file]

        for file in filteredFiles:
            fullPath = os.path.join(key, file)
            print(modification_date(fullPath), file)

    return ""


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def main():
    files = GetFiles("Books")

    pdfFilesToRemove = FilesToRemove(files, "pdf")
#    print(pdfFilesToRemove)


if __name__ == "__main__":
    main()
