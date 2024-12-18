import subprocess
import os
import time
from datetime import datetime, timedelta

def commit_and_push_changes(repo_path, commit_message="Update Streamlit app"):
    try:
        # Change the current working directory to the repository path
        os.chdir(repo_path)

        # Check if there are any changes
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - No changes detected. Waiting for changes...")
            return

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes with a message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Pull the latest changes from the remote repository to avoid conflicts
        subprocess.run(["git", "pull", "--rebase"], check=True)

        # Push the changes to the repository
        subprocess.run(["git", "push"], check=True)

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Changes have been committed and pushed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Make sure your repository path is correct and that your remote repository is set up.")
    except FileNotFoundError:
        print(f"Error: The path '{repo_path}' does not exist.")

# Specify the path to your Git repository
repo_path = r"C:\Users\user\Desktop\Streamlit"

# Duration to run the script (in seconds)
run_duration = 3600  # 1 hour

# Continuous loop to check for changes and commit/push repeatedly within the time period
start_time = datetime.now()
end_time = start_time + timedelta(seconds=run_duration)

try:
    while datetime.now() < end_time:
        commit_and_push_changes(repo_path, "Update Streamlit app with latest changes")
        time.sleep(60)  # Check for changes every 60 seconds

    print(f"Script finished after running for {run_duration // 60} minutes.")
except KeyboardInterrupt:
    print("Stopped by user.")
