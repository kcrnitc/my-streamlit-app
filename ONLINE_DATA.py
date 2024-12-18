import subprocess
import os

def commit_and_push_changes(repo_path, commit_message="Update Streamlit app"):
    try:
        # Change the current working directory to the repository path
        os.chdir(repo_path)

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes with a message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Pull the latest changes from the remote repository to avoid conflicts
        subprocess.run(["git", "pull", "--rebase"], check=True)

        # Push the changes to the repository
        subprocess.run(["git", "push"], check=True)

        print("Changes have been committed and pushed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Make sure your repository path is correct and that your remote repository is set up.")
    except FileNotFoundError:
        print(f"Error: The path '{repo_path}' does not exist.")

# Specify the path to your Git repository
repo_path = r"C:\Users\user\Desktop\Streamlit"

# Call the function with the repository path and a commit message
commit_and_push_changes(repo_path, "Update Streamlit app with latest changes")
