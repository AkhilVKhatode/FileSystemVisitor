# File System Visitor Pattern in Python

This project demonstrates the use of the **Visitor Pattern** to traverse a simple file system structure, including files and folders. The pattern allows for operations such as indexing, virus scanning, and size calculation to be applied across a hierarchical file system.

## Features

- **Visitor Pattern**: Allows adding new operations without modifying the classes for files or folders.
- **File System Structure**: Consists of `File` and `Folder` elements, with folders containing multiple files or other folders.
- **Visitors**:
  - **Size Calculation**: Computes the total size of all files in a folder and its subfolders.
  - **Virus Scanning**: Scans for files with names containing "virus" and flags them as suspicious.

## File System Classes

- **File**: Represents a file with a name and size.
- **Folder**: Represents a folder that can contain multiple files and subfolders.

## Visitors

- **SizeVisitor**: Calculates the total size of all files in the folder.
- **VirusScanVisitor**: Scans files for the term "virus" in the file name to identify suspicious files.

## Example Output
Size Calculation:
```yaml
Folder: Folder1
File: document.txt, Size: 100 KB
File: image.png, Size: 200 KB
Folder: Folder2
File: virus_report.doc, Size: 50 KB
Total Size: 350 KB
```

Virus Scanning:
```yaml
Scanning Folder: Folder1
Scanned File: document.txt
Scanned File: image.png
Scanning Folder: Folder2
Scanned File: virus_report.doc
Suspicious Files: ['virus_report.doc']
```
