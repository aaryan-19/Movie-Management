# for os module
import os

# for creating the path file for the project
def get_complete_file_path():
    """complete path of the file."""
    # creating foldername
    folder_name = 'movieproject'
    
    # creating file_name
    file_name = 'moviefile.txt'
    
    # for separator
    separator = "/"
    
    # adding folder name, separator and file name 
    complete_path = folder_name + separator + file_name

    # returning the path for the project file
    return complete_path

# function for checking if the project file exist or not
def is_project_exists(complete_path):
    """Check project"""

    # checking for project file - exist or not using os module
    if os.path.exists(complete_path):
        return True
    # if project file does not exist
    return False

# function for displaying all the movies entered
def display_all_the_movies(complete_path):
    """Display all the movies."""

    # calling function to verify if project file exist or not
    if is_project_exists(complete_path=complete_path):
        # opening the file in read mode
        with open(complete_path, "r") as file1:
            # using enumerate() for displaying movieno
            for movieno,mname in enumerate(file1):
                print(movieno + 1, ': ', mname)
    else:
        print("Project does not exists")

# function for checking that entered movie name already exist or not
def is_movie_exists(complete_path, name):
    """Is movie exists or not."""
    is_exists = False
    # opening file in read mode
    file_read = open(complete_path, 'r')
    # reading the file
    read_movie = file_read.readlines()
    # using loop to iterate over the movie file
    for movie_name in read_movie:
        # checking if the movie name already exist or not
        if (movie_name.strip('\n') == name):
            print("Movie Name Already Added")
            is_exists = True
            break

    return is_exists

# function to add a movie name to the file
def add_new_movie(complete_path):
    """Adding new Movie"""
    # opening th efile in append mode
    with open(complete_path, "a") as file2:
        # adding the movie name
        name = input("Enter the movie name:")
        # calling function to see if the movie already exist or not 
        is_exists = is_movie_exists(complete_path=complete_path, name=name)
        # if it does'nt exist then add the movie name in the file
        if not is_exists:
            # write the movie name in the file 
            file2.write(name)
            file2.write("\n")

# function to delete the movie name from the file
def deleting_movie(complete_path):
    """Deleting A Movie"""
    # using if condition -calling function to check if the movie name is already in the file or not
    if is_project_exists(complete_path=complete_path):
        # get list of lines
        # opening file in read mode
        a_file = open(complete_path, "r")
        # reading the file
        lines = a_file.readlines()
        # closing the file in read format
        a_file.close()
        # opening the file in write mode
        with open(complete_path, "w") as file3:
            del_name = input("Enter the  name of the movie you want to delete=")
            # searching the movie name to delete 
            for line in lines:
                # if it's found then except that every other movie name is again written
                if(line.strip('\n') != del_name):
                    file3.write(line)
    else:
        print("Project does not exists")

# function for removing the project
def remove_project(complete_path):
    """Deleting the whole project""" 
    # using if condition to check if the project exist or not
    if is_project_exists(complete_path=complete_path):
        # using os to remocve the whole path
        os.remove(complete_path)
    else:
        print("\nProject does not exist")

# function to check if the user want to continue or not
def is_continue():
    """User should continue or not."""
    print("\nDo you want to continue: Yes or No=")
    # taking input for the user to continue or not
    user_choice = input()
    return user_choice


#mai n() function
def main():
    """Main function."""
    # Do all the things here
    """Creating the file"""
    complete_path = get_complete_file_path()
    # user_choice is used for loop
    user_choice = 'Yes'
    # using while loop
    while(user_choice.lower() == 'yes'):

        # call all other functions
        print("Menu\n1. Display All The Movies\n2. Add New Movie\n3. Delete a Movie\n4. Remove The Project\n5. Exit")
        menu_choice = int(input("Enter your choice= "))
        complete_path = get_complete_file_path()

        # for displaying all the entered movies
        if (menu_choice == 1):
            # for calling the display function
            display_all_the_movies(complete_path=complete_path)
            
            # for calling the function to check if user wants to continue or not 
            user_choice = is_continue()

        # for adding a new movie
        elif (menu_choice == 2):
            
            # calling function to add a new movie name
            add_new_movie(complete_path=complete_path)
            
            # for calling the function to check if user wants to continue or not 
            user_choice = is_continue()

        # for deleting a movie
        elif(menu_choice == 3):
            
            # calling function to delete a movie name
            deleting_movie(complete_path=complete_path)
            
            # for calling the function to check if user wants to continue or not 
            user_choice = is_continue()

        # for removing the project
        elif(menu_choice == 4):

            #calling function to remove the project
            remove_project(complete_path=complete_path)

            # for calling the function to check if user wants to continue or not 
            user_choice = is_continue()

        # for exit
        elif(menu_choice == 5):
            print("\nThank you")

            #to exit the program
            exit()

        # if wrong choice entered
        else:
            print("\nWrong Choice Entered")
            print("\nDo you want to continue: Yes or No=")
            user_choice = input()
    
    else:
        print("Thank You")

# main
if __name__ == "__main__":
    main()