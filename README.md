# Google Takeout Organizer
A simple Python script to fix Google Takeout's messy folder structure when exporting large Google Drive folders.

## The Problem
When you export large folders from Google Drive using Google Takeout, it splits them into multiple Takeout folders (Takeout, Takeout (1), Takeout (2), etc.). This creates a mess of duplicate folders and scattered files, making it difficult to work with your exported data. This script solves that problem by combining and organizing all your Takeout folders into a clean structure.

## What This Script Does
- Merges all your Takeout folders into one clean structure
- Removes duplicate files automatically
- Maintains original folder organization
- Cleans up empty folders
- Handles large exports efficiently
- Preserves file metadata

## Setup Instructions

### 1. Install Python on Mac
1. Open Terminal
2. Install Homebrew if you haven't already:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Install Python:
```bash
brew install python
```
4. Verify installation:
```bash
python --version
```

### 2. Download and Run the Script
1. Download `takeout_organizer.py` from this repository
2. Open Terminal and navigate to where you saved the script:
```bash
cd /path/to/script/folder
```
3. Run the script with your directories:
```bash
python takeout_organizer.py --source "/path/to/takeout/folders" --destination "/path/to/destination"
```

Example:
```bash
python takeout_organizer.py --source "/Users/me/Downloads/takeout_folder" --destination "/Users/me/Dropbox/Organized_Drive"
```

### Entering Your Directories

1. **Source Directory** (`--source`): 
   - This is where your Google Takeout folders are
   - To find this path:
     1. Open Finder
     2. Navigate to your Takeout folders
     3. Right-click any folder
     4. Hold Option key and select "Copy as Pathname"
   - This should be the parent folder containing all your Takeout folders

2. **Destination Directory** (`--destination`):
   - This is where you want your organized files to go
   - Follow the same steps as above to copy the path
   - The script will create this folder if it doesn't exist
   - Make sure you have write permissions for this location

## How It Works
1. The script scans through all your Takeout folders
2. It identifies the original folder structure
3. Creates a clean directory structure at the destination
4. Copies files while checking for duplicates
5. Removes empty folders after organization
6. Preserves all file metadata and dates

## Common Issues and Solutions

### "Permission denied" error
- Make sure you have read access to source files
- Ensure you have write access to the destination directory
- Try running with `sudo` if needed (be careful with this)

### "File already exists" messages
- This is normal - the script is protecting existing files
- Duplicate files are automatically skipped

### "Source directory not found" error
- Double-check your source path
- Make sure you copied the full path correctly
- Verify the folders exist at that location

## Usage Tips
- Keep your original Takeout folders until you verify the organization
- Run a small test first with a subset of folders
- Make sure you have enough disk space at the destination
- For very large exports, the script may take some time to run

## Requirements
- Python 3.x
- macOS, Linux, or Windows
- No additional Python packages needed

## License

MIT License

---

Found this helpful? Please star the repository!

For issues or feature requests, please open an issue on GitHub.