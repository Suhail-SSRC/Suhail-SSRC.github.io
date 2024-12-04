import os

# Base directory containing the datasets
base_dir = "."

# Output HTML file
output_file = "index.html"

# Start writing the HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event-Based Camera Capture for High Amplitude and Abnormal Motion Events</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        h2, h3 {
            color: #555;
        }
        video {
            display: block;
            margin: 10px 0;
            max-width: 100%;
        }
        .container {
            margin-bottom: 40px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>Event-Based Camera Capture for High Amplitude and Abnormal Motion Events</h1>
    <p>This page showcases raw event IWEs and segmented event IWEs from various scenes captured using event-based cameras.</p>
"""

# Walk through the directory structure
for root, dirs, files in os.walk(base_dir):
    # Check for combined_IWEs.mp4 in the folder
    video_files = [file for file in files if file == "combined_IWEs.mp4"]
    if video_files:
        # Extract the relative path and scene name
        relative_path = os.path.relpath(root, base_dir)
        scene_name = os.path.basename(root)

        # Add a section for this scene
        html_content += f"""
        <div class="container">
            <h2>Scene: {scene_name}</h2>
        """

        # Add a video for raw IWEs if it exists
        if "raw_IWEs.mp4" in files:
            raw_video_path = os.path.relpath(os.path.join(root, "raw_IWEs.mp4"), base_dir)
            html_content += f"""
            <h3>Raw Event IWE</h3>
            <video controls autoplay loop>
                <source src="{raw_video_path}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            """

        # Add a video for segmented IWEs if it exists
        if "seg_IWEs.mp4" in files:
            seg_video_path = os.path.relpath(os.path.join(root, "seg_IWEs.mp4"), base_dir)
            html_content += f"""
            <h3>Segmented Event IWE</h3>
            <video controls autoplay loop>
                <source src="{seg_video_path}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            """

        # Close the container div
        html_content += "</div>\n"

# Close the HTML structure
html_content += """
</body>
</html>
"""

# Write the HTML content to a file
with open(output_file, "w") as f:
    f.write(html_content)

print(f"HTML page generated: {output_file}")
