import os


def print_second_last(dir=None):
    if dir is None or not os.path.isdir(dir):
        print("\nPlease enter a valid path, for example: '/Users/Name/Documents.'\n"
              "We'll be searching your current directory instead.\n")
        dir = os.getcwd()
    list_of_files = []
    for file in os.listdir(dir):
         if file.endswith(".txt"):
            list_of_files.append(os.path.join(dir, file))
    print("Total number of .txt files found is {0}\n".format(len(list_of_files)))
    for name in list_of_files:
        file = open(name, 'r')
        list_of_strings = file.readlines()
        try:
            print("The second last line in the file {0} is: \n {1}".format(name, list_of_strings[-2]))
        except(IndexError):
            print("File {0} do not have 2 lines \n".format(name))
        file.close()


def main():
    dir = raw_input("Please insert the directory you want to search for .txt files:\n")
    print_second_last(dir)


if __name__ == '__main__':
    main()
