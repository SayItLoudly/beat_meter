
import librosa
import numpy as np

def get_bpm(file_path):
    """
    Analyzes a song to determine its beats per minute (BPM).

    Args:
        file_path (str): The absolute path to the audio file.

    Returns:
        float: The estimated BPM of the song.
    """
    try:
        # To get a more representative sample, we'll analyze the middle of the song.
        analysis_duration = 60.0 # We'll analyze a 60-second clip.

        # First, get the total duration without loading the whole file.
        total_duration = librosa.get_duration(path=file_path)

        # Calculate the offset to center the analysis window in the middle of the song.
        # If the song is shorter than our analysis window, we start from the beginning.
        offset = max(0, (total_duration / 2) - (analysis_duration / 2))

        # Load the calculated segment of the song.
        y, sr = librosa.load(file_path, offset=offset, duration=analysis_duration)

        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        # tempo can be a numpy array (e.g., [120.0]) or a float.
        # Convert to a standard float to handle both cases before rounding.
        return round(float(tempo))
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        bpm = get_bpm(file_path)
        if bpm:
            print(f"The estimated BPM of the song is: {bpm}")
    else:
        print("Please provide the path to a song file.")
