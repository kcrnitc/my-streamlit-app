import os
import time
import git
from git import Repo

# Define the path to your local repository and the Excel file
repo_path = "C:/Users/user/Desktop/Streamlit"  # Path to your local Git repository
excel_file_path = "C:/Users/user/Desktop/Streamlit/data/EDM_DATA.xlsx"  # Path to your Excel file

# GitHub repository URL (https://github.com/username/repo_name)
remote_repo_url = "https://github.com/kcrnitc/my-streamlit-app.git"  # Your GitHub repo URL

# Local GitHub credentials
username = 'kcrnitc'  # Replace with your GitHub username
token = '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'  # Replace with your GitHub personal access token

def check_file_update():
    """
    Check if the Excel file has been modified since the last commit.
    """
    last_modified_time = os.path.getmtime(excel_file_path)
    return last_modified_time

def commit_and_push_changes():
    """
    Commit changes to the Excel file and push them to the GitHub repository.
    """
    try:
        # Initialize Git repo and check the status
        repo = Repo(repo_path)
        repo.git.add(excel_file_path)  # Stage the Excel file
        
        # Commit the changes
        repo.index.commit("Update EDM_DATA.xlsx")
        
        # Push the changes to GitHub
        origin = repo.remotes.origin
        origin.push()

        print("Changes pushed to GitHub successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    """
    Main function that checks for file updates and pushes changes.
    """
    last_check_time = None

    while True:
        try:
            current_file_time = check_file_update()

            if last_check_time is None:
                last_check_time = current_file_time
            elif current_file_time > last_check_time:
                print("Excel file updated. Committing and pushing changes...")
                commit_and_push_changes()
                last_check_time = current_file_time

        except Exception as e:
            print(f"Error: {e}")
        
        # Sleep for 10 seconds before checking again
        time.sleep(10)

if __name__ == "__main__":
    main()
