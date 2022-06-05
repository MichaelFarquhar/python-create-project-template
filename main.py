import os 
import sys
import shutil

def print_e(err: str):
    '''Prints an error to the console and exits the program.'''
    print(err)
    sys.exit()

def main():
    if len(sys.argv) < 2:
        print_e("Error: Please provide a directory name as the first argument.")
    else:
        # Template directory to be copied
        template_dir = os.path.join(sys.path[0], 'template')

        # Get path to new directory with the file name provided from the script argument
        dir_name = sys.argv[1]
        dest_dir = os.path.join(os.getcwd(), dir_name)

        try:
            # Copy template folder to a new specified directory. If directory name already exists, it will through an error.
            shutil.copytree(template_dir, dest_dir)
        except FileExistsError:
            print_e("Directory with this name already exists.")

if __name__ == "__main__":
    main()
