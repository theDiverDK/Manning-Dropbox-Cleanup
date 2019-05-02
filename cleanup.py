import os


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


def GetSpecificFiles(files, extension):
    result = filter(lambda k: extension in k, files)
    return '\n'.join(map(str, result))


def main():
    files = GetFiles("Books")

    #pdfFiles = GetSpecificFiles(files, "pdf")

    print(files)


if __name__ == "__main__":
    main()
