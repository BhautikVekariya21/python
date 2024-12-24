import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import certifi

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MongoDB URI is not set in the .env file")

# Initialize MongoDB client with SSL
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

# Database and collection
db = client["pymongovideos"]
video_collection = db["videos"]

# Helper functions
def list_videos():
    """
    List all videos in the database.
    """
    videos = video_collection.find()
    if video_collection.count_documents({}) == 0:
        print("\nNo videos available.\n")
        return

    print("\nList of YouTube Videos:")
    print("-" * 70)
    for video in videos:
        print(f"ID: {video['_id']} | Name: {video['name']} | Duration: {video['time']}")
    print("-" * 70)


def add_video():
    """
    Add a new video to the database.
    """
    name = input("Enter video name: ").strip()
    time = input("Enter video duration (e.g., 10:00): ").strip()

    video_collection.insert_one({"name": name, "time": time})
    print(f"Video '{name}' added successfully.")


def update_video():
    """
    Update details of an existing video.
    """
    list_videos()
    video_id = input("Enter the ID of the video to update: ").strip()

    try:
        video = video_collection.find_one({"_id": ObjectId(video_id)})
        if video:
            name = input(f"Enter new name (current: {video['name']}): ").strip()
            time = input(f"Enter new duration (current: {video['time']}): ").strip()

            video_collection.update_one(
                {"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}}
            )
            print(f"Video ID {video_id} updated successfully.")
        else:
            print("Video not found.")
    except Exception as e:
        print(f"Error updating video: {e}")


def delete_video():
    """
    Delete a video from the database.
    """
    list_videos()
    video_id = input("Enter the ID of the video to delete: ").strip()

    try:
        video = video_collection.find_one({"_id": ObjectId(video_id)})
        if video:
            confirmation = input(f"Are you sure you want to delete '{video['name']}'? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                video_collection.delete_one({"_id": ObjectId(video_id)})
                print(f"Video ID {video_id} deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Video not found.")
    except Exception as e:
        print(f"Error deleting video: {e}")


def search_videos():
    """
    Search for videos by name.
    """
    query = input("Enter a keyword to search for: ").strip().lower()
    results = video_collection.find({"name": {"$regex": query, "$options": "i"}})

    print("\nSearch Results:")
    print("-" * 70)
    found = False
    for video in results:
        print(f"ID: {video['_id']} | Name: {video['name']} | Duration: {video['time']}")
        found = True

    if not found:
        print(f"No videos found matching '{query}'.")
    print("-" * 70)


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
        print("6. Exit")
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
            print("Exiting YouTube Video Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    client.close()


if __name__ == "__main__":
    main()
