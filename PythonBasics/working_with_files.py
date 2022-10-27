from typing import IO


def main():
    try:
        with open('newfile3.txt','w') as file:
            file.write("another test line :)")
    except IOError as e:
        print("Exception caught: Unable to write to file", e)
    except Exception as e:
        print("Another error ocurred", e)

if __name__ == '__main__':
    main()