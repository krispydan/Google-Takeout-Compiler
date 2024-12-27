#!/usr/bin/env python3

"""
Google Takeout Organizer
A script to reorganize and deduplicate Google Takeout exported files into a clean folder structure.
"""

import os
import shutil
from pathlib import Path
import hashlib
import argparse

def get_file_hash(filepath):
    """
    Calculate MD5 hash of a file to check for duplicates.
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        str: MD5 hash of the file
    """
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        # Read file in chunks to handle large files efficiently
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def organize_files(source_root, destination_root):
    """
    Organize files from Google Takeout folders into a single structure.
    
    Args:
        source_root (str): Root directory containing Takeout folders
        destination_root (str): Destination directory for organized files
    """
    # Create destination root if it doesn't exist
    Path(destination_root).mkdir(parents=True, exist_ok=True)
    
    # Dictionary to track processed files using their hashes
    processed_files = {}  # hash -> destination_path
    
    # Walk through all Takeout folders
    for root, dirs, files in os.walk(source_root):
        for file in files:
            # Skip system files and browser archives
            if file == '.DS_Store' or file == 'archive_browser.html':
                continue
                
            source_path = os.path.join(root, file)
            
            # Skip if the file is already in the destination directory
            if destination_root in source_path:
                continue
            
            # Extract the relative path after "Drive" folder
            rel_path = None
            path_parts = Path(source_path).parts
            
            if 'Drive' in path_parts:
                drive_index = path_parts.index('Drive')
                rel_path = os.path.join(*path_parts[drive_index + 1:])
            else:
                # If not in a Drive folder, just use the filename
                rel_path = file
            
            # Construct destination path
            dest_path = os.path.join(destination_root, rel_path)
            dest_dir = os.path.dirname(dest_path)
            
            # Create destination directory structure
            Path(dest_dir).mkdir(parents=True, exist_ok=True)
            
            # Handle file copying and deduplication
            if os.path.exists(source_path) and os.path.isfile(source_path):
                file_hash = get_file_hash(source_path)
                
                # Skip if we've already processed this file
                if file_hash in processed_files:
                    print(f"Skipping duplicate file: {source_path}")
                    continue
                    
                processed_files[file_hash] = dest_path
                
                # Copy file to destination
                try:
                    if not os.path.exists(dest_path):
                        shutil.copy2(source_path, dest_path)
                        print(f"Copied: {source_path} -> {dest_path}")
                    else:
                        print(f"File already exists: {dest_path}")
                except Exception as e:
                    print(f"Error copying {source_path}: {str(e)}")

def cleanup_empty_folders(path):
    """
    Remove empty folders from the directory structure.
    
    Args:
        path (str): Root path to start cleaning from
    """
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if not os.listdir(dir_path):  # Check if directory is empty
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
            except Exception as e:
                print(f"Error removing directory {dir_path}: {str(e)}")

def main():
    """Main function to handle script execution and user input."""
    parser = argparse.ArgumentParser(
        description='Organize and deduplicate Google Takeout exported files.'
    )
    parser.add_argument(
        '--source', 
        type=str, 
        required=True,
        help='Source directory containing Google Takeout folders'
    )
    parser.add_argument(
        '--destination', 
        type=str, 
        required=True,
        help='Destination directory for organized files'
    )
    
    args = parser.parse_args()
    
    print("Starting file organization...")
    organize_files(args.source, args.destination)
    
    print("\nCleaning up empty folders...")
    cleanup_empty_folders(args.destination)
    
    print("\nOrganization complete!")

if __name__ == "__main__":
    main()