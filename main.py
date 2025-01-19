import os
import pytube
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import traceback

def sanitize_filename(name):
    """
    Sanitize file names to avoid issues with invalid characters.
    """
    return "".join(c for c in name if c.isalnum() or c in " ._-").strip()

def transcribe_video(video_id):
    """
    Fetch the transcript of the video using YouTube Transcript API.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        return formatter.format_transcript(transcript)
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def transcribe_playlist(playlist_url, output_dir):
    """
    Transcribe all videos in a playlist and save the transcriptions as text files.
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Get playlist
        playlist = Playlist(playlist_url)

        # Loop through videos in the playlist
        for video in playlist.videos:
            try:
                print(video)
                video_title = sanitize_filename(video.title)
                print(f"Processing: {video_title}")

                # Check if transcription already exists
                output_file_path = os.path.join(output_dir, f"{video_title}.txt")
                if os.path.exists(output_file_path):
                    print(f"Transcription already exists for '{video_title}', skipping.")
                    continue

                # Transcribe video
                print(f"Transcribing video '{video_title}'...")
                transcription = transcribe_video(video.video_id)
                if transcription is None:
                    print(f"Transcription failed for '{video_title}'.")
                    continue

                # Save transcription
                with open(output_file_path, "w", encoding="utf-8") as file:
                    file.write(transcription)
                print(f"Saved transcription for '{video_title}' to {output_file_path}.")

            except Exception as e:
                print(f"An error occurred with video '{video.title}': {e}")
                traceback.print_exc()

    except Exception as e:
        print(f"Failed to process playlist: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    # Example usage
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_directory = "The Buying Experience Everything You Need to Work with Buyers"
    transcribe_playlist(playlist_url, output_directory)
