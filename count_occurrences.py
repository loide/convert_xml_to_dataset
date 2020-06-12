"""
Read a .txt file and count the occurrence of a keyword
"""
def main():
    filename = 'log-20200611.txt'
    keyword = "SELECT"

    file = open(filename)

    # read content of file to string
    data = file.read()

    # get number of occurrences of the substring in the string
    occurrences = data.count(keyword)

    print("Number of occurrences: {}".format(occurrences))

if __name__ == "__main__":
    main()
