import sqlite3

# Database connection
DB_NAME = 'videos.db'
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
conn.commit()

# Helper functions
def list_videos():
    """
    Display all videos in the database.
    """
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("\nNo videos available.\n")
        return

    print("\nList of YouTube Videos:")
    print("-" * 70)
    for video in videos:
        print(f"ID: {video[0]} | Name: {video[1]} | Duration: {video[2]}")
    print("-" * 70)


def add_video():
    """
    Add a new video to the database.
    """
    name = input("Enter video name: ").strip()
    time = input("Enter video duration (e.g., 10:00): ").strip()

    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"Video '{name}' added successfully.")


def update_video():
    """
    Update details of an existing video.
    """
    list_videos()
    video_id = input("Enter the ID of the video to update: ").strip()

    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if video:
        name = input(f"Enter new name (current: {video[1]}): ").strip()
        time = input(f"Enter new duration (current: {video[2]}): ").strip()

        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        conn.commit()
        print(f"Video ID {video_id} updated successfully.")
    else:
        print("Invalid video ID.")


def delete_video():
    """
    Delete a video from the database.
    """
    list_videos()
    video_id = input("Enter the ID of the video to delete: ").strip()

    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if video:
        confirmation = input(f"Are you sure you want to delete '{video[1]}'? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
            conn.commit()
            print(f"Video ID {video_id} deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid video ID.")


def search_videos():
    """
    Search for videos by name.
    """
    query = input("Enter a keyword to search for: ").strip().lower()
    cursor.execute("SELECT * FROM videos WHERE LOWER(name) LIKE ?", (f"%{query}%",))
    results = cursor.fetchall()

    if results:
        print("\nSearch Results:")
        print("-" * 70)
        for video in results:
            print(f"ID: {video[0]} | Name: {video[1]} | Duration: {video[2]}")
        print("-" * 70)
    else:
        print(f"No videos found matching '{query}'.")


def sort_videos():
    """
    Sort videos by name or duration.
    """
    print("\nSort Options:")
    print("1. Sort by Name")
    print("2. Sort by Duration")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        cursor.execute("SELECT * FROM videos ORDER BY name ASC")
    elif choice == '2':
        cursor.execute("SELECT * FROM videos ORDER BY time ASC")
    else:
        print("Invalid choice.")
        return

    videos = cursor.fetchall()

    if videos:
        print("\nSorted Videos:")
        print("-" * 70)
        for video in videos:
            print(f"ID: {video[0]} | Name: {video[1]} | Duration: {video[2]}")
        print("-" * 70)
    else:
        print("No videos available to sort.")


# Main application
def main():
    """
    Main function to run the YouTube Video Manager application.
    """
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
            list_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            search_videos()
        elif choice == '6':
            sort_videos()
        elif choice == '7':
            print("Exiting YouTube Video Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()


if __name__ == "__main__":
    main()
