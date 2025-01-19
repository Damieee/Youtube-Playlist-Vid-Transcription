# YouTube Playlist Video Transcription

This project allows you to transcribe all videos in a YouTube playlist using the YouTube Transcript API. The transcriptions are saved as text files in a specified output directory.

## Features

- Fetches transcripts for all videos in a YouTube playlist.
- Saves transcriptions as text files.
- Handles errors gracefully and skips problematic videos.

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

    Alternatively, you can install the dependencies manually:
    ```sh
    pip install pytube youtube-transcript-api
    ```

## Usage

1. **Run the script**:
    ```sh
    python Youtube-Playlist-Vid-Transcription.py
    ```

2. **Enter the YouTube playlist URL** when prompted:
    ```
    Enter the YouTube playlist URL: <your-playlist-url>
    ```

3. **Transcriptions will be saved** in the specified output directory.

## Example

```sh
C:\Users\Dami\Documents\python> python Youtube-Playlist-Vid-Transcription.py
Enter the YouTube playlist URL: https://youtube.com/playlist?list=PLZ_hZbjsE92u7egiCJ-WEReJ3r4cgUOYC&si=l0fxrrnGrllk73SV
Processing: Video Title 1
Transcribing video 'Video Title 1'...
Saved transcription for 'Video Title 1' to transcriptions/Video Title 1.txt.
Processing: Video Title 2
Transcribing video 'Video Title 2'...
Saved transcription for 'Video Title 2' to transcriptions/Video Title 2.txt.
...
```

## Troubleshooting

- **Error accessing video title**: If you encounter an error related to accessing the video title, ensure you have the latest version of `pytube` installed:
    ```sh
    pip install --upgrade pytube
    ```

- **Platform independent libraries error**: Ensure that Python is correctly installed and added to your system's PATH. Consider using a virtual environment to avoid conflicts.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.