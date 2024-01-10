import os
import subprocess
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--editor', help='Path to the FlaxEditor.exe')
parser.add_argument('extra', nargs=argparse.REMAINDER, help='Extra arguments for the application')

# Parse the command-line arguments
args = parser.parse_args()

if not args.editor:
    print("No editor path provided, please use -e or --editor")
    exit(1)

project_file = None
for file_name in os.listdir('.'):
    if not file_name.endswith('.flaxproj'):
        continue
    
    project_file = file_name
    print(f"Found project file: {project_file}")
    break

if not project_file:
    print("No project file found, please create a new project first")
    exit(1)

print(f"Editor:     {args.editor}")
print(f"Project:    {project_file}")
print(f"Arguments:  {args.extra}")

try:
    process = subprocess.Popen([args.editor, '-project', project_file] + args.extra)
except Exception as e:
    print(f"Failed to start editor: {args.editor}")
    print(f"Error message: {str(e)}")
    input("Press Enter to close...")
    exit(1)