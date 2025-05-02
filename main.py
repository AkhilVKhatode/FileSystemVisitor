from abc import ABC, abstractmethod

# Visitor Interface
class FileSystemVisitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_folder(self, folder):
        pass

# Element Interface
class FileSystemElement(ABC):
    @abstractmethod
    def accept(self, visitor: FileSystemVisitor):
        pass

# File class
class File(FileSystemElement):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_file(self)

# Folder class
class Folder(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add(self, element: FileSystemElement):
        self.elements.append(element)

    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_folder(self)
        for element in self.elements:
            element.accept(visitor)

# Concrete Visitor: Size Calculation
class SizeVisitor(FileSystemVisitor):
    def __init__(self):
        self.total_size = 0

    def visit_file(self, file):
        self.total_size += file.size
        print(f"File: {file.name}, Size: {file.size} KB")

    def visit_folder(self, folder):
        print(f"Folder: {folder.name}")
        
    def get_total_size(self):
        return self.total_size

# Concrete Visitor: Virus Scanning
class VirusScanVisitor(FileSystemVisitor):
    def __init__(self):
        self.suspicious_files = []

    def visit_file(self, file):
        if "virus" in file.name.lower():  # A simple check for suspicious files
            self.suspicious_files.append(file.name)
        print(f"Scanned File: {file.name}")

    def visit_folder(self, folder):
        print(f"Scanning Folder: {folder.name}")

    def get_suspicious_files(self):
        return self.suspicious_files

# Usage example
if __name__ == "__main__":
    # Create a file system structure
    file1 = File("document.txt", 100)
    file2 = File("image.png", 200)
    file3 = File("virus_report.doc", 50)
    
    folder1 = Folder("Folder1")
    folder1.add(file1)
    folder1.add(file2)
    
    folder2 = Folder("Folder2")
    folder2.add(file3)

    # Size Calculation
    size_visitor = SizeVisitor()
    folder1.accept(size_visitor)
    folder2.accept(size_visitor)
    print(f"Total Size: {size_visitor.get_total_size()} KB")

    # Virus Scanning
    virus_scan_visitor = VirusScanVisitor()
    folder1.accept(virus_scan_visitor)
    folder2.accept(virus_scan_visitor)
    print(f"Suspicious Files: {virus_scan_visitor.get_suspicious_files()}")
