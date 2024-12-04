import os
import subprocess

def reencode_video(input_file):
    # Temporary output file for re-encoded video
    output_file = input_file + "_temp.mp4"
    
    # Run the ffmpeg command to re-encode
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-y",  # Overwrite without asking
        output_file
    ]
    
    try:
        print(f"Re-encoding: {input_file}")
        subprocess.run(command, check=True)
        
        # Replace the original file with the re-encoded file
        os.replace(output_file, input_file)
        print(f"Re-encoded successfully: {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error re-encoding {input_file}: {e}")
        # Clean up the temporary file if something went wrong
        if os.path.exists(output_file):
            os.remove(output_file)

def reencode_videos_in_directory(root_dir):
    # Walk through the directory structure
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(subdir, file)
                reencode_video(file_path)

if __name__ == "__main__":
    # Root directory containing the video files
    root_directory = "/home/suhail/Documents/Robotics Perception - Part B/catkin_ws/src/EMSGC/result"
    
    # Re-encode all MP4 videos in the directory
    reencode_videos_in_directory(root_directory)
