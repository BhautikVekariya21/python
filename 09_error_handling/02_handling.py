import json

# File path for storing data
FILE_PATH = 'handle.txt'

def load_data():
    """
    Load video data from a file.
    Returns an empty list if the file doesn't exist.
    """
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    """
    Save video data to a file.
    """
    with open(FILE_PATH, 'w') as file:
        json.dump(videos, file)

def display_videos(videos):
    """
    Display all videos in a formatted list.
    """
    if not videos:
        print("\nNo videos available.\n")
        print("-" * 70)
        return

    print("\nList of YouTube Videos:")
    print("-" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} | Duration: {video['time']}")
    print("-" * 70)

def get_valid_index(prompt, videos):
    """
    Prompt the user for a valid index and validate the input.
    Returns the validated index.
    """
    while True:
        try:
            index = int(input(prompt))
            if 1 <= index <= len(videos):
                return index - 1
            else:
                print(f"Invalid index. Please enter a number between 1 and {len(videos)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_video(videos):
    """
    Add a new video to the list.
    """
    name = input("Enter video name: ").strip()
    time = input("Enter video duration (e.g., 10:00): ").strip()
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print(f"Video '{name}' added successfully.")

def update_video(videos):
    """
    Update an existing video's details.
    """
    if not videos:
        print("\nNo videos available to update.\n")
        return

    display_videos(videos)
    index = get_valid_index("Enter the video number to update: ", videos)
    name = input("Enter the new video name: ").strip()
    time = input("Enter the new video duration (e.g., 10:00): ").strip()
    videos[index] = {'name': name, 'time': time}
    save_data(videos)
    print(f"Video updated successfully to '{name}' with duration {time}.")

def delete_video(videos):
    """
    Delete a video from the list.
    """
    if not videos:
        print("\nNo videos available to delete.\n")
        return

    display_videos(videos)
    index = get_valid_index("Enter the video number to delete: ", videos)
    confirmation = input(f"Are you sure you want to delete '{videos[index]['name']}'? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        deleted_video = videos.pop(index)
        save_data(videos)
        print(f"Video '{deleted_video['name']}' deleted successfully.")
    else:
        print("Deletion cancelled.")

def search_videos(videos):
    """
    Search for videos by name.
    """
    query = input("Enter a keyword to search for: ").strip().lower()
    results = [video for video in videos if query in video['name'].lower()]

    if results:
        print("\nSearch Results:")
        print("-" * 70)
        for video in results:
            print(f"{video['name']} | Duration: {video['time']}")
        print("-" * 70)
    else:
        print(f"No videos found matching '{query}'.")

def sort_videos(videos):
    """
    Sort videos by name or duration.
    """
    if not videos:
        print("\nNo videos available to sort.\n")
        return

    print("\nSort Options:")
    print("1. Sort by Name")
    print("2. Sort by Duration")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        videos.sort(key=lambda x: x['name'].lower())
        print("\nVideos sorted by name.")
    elif choice == '2':
        videos.sort(key=lambda x: x['time'])
        print("\nVideos sorted by duration.")
    else:
        print("Invalid choice. Returning to main menu.")

    save_data(videos)

def main():
    """
    Main function to run the YouTube Manager application.
    """
    videos = load_data()

    while True:
        print("\nVideo Manager")
        print("-" * 70)
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video's details")
        print("4. Delete a YouTube video")
        print("5. Search for a video")
        print("6. Sort videos")
        print("7. Exit")
        print("-" * 70)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            search_videos(videos)
        elif choice == '6':
            sort_videos(videos)
        elif choice == '7':
            print("Exiting YouTube Video Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
