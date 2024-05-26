# In-Memory File System Documentation

## Implementation Overview

The implemented in-memory file system supports various file operations similar to a real file system. The system supports creating directories and files, navigating between directories, listing directory contents, and more. Here's an overview of the functionalities implemented:

1. **mkdir**: Create a new directory.
2. **cd**: Change the current directory, supporting relative paths, absolute paths, and special paths like `..` (parent directory) and `/` (root directory).
3. **ls**: List the contents of the current directory or a specified directory.
4. **cat**: Display the contents of a file.
5. **touch**: Create a new empty file.
6. **echo**: Write text to a file.
7. **mv**: Move a file or directory to another location.
8. **cp**: Copy a file or directory to another location.
9. **rm**: Remove a file or directory.

### Data Structures Used

- **Node Class**: Represents a generic node in the file system. It has attributes like `name`, `type` (file or directory), and `parent`.
- **FileNode Class**: Inherits from `Node` and represents a file. It has an additional attribute `content` to store file content.
- **DirectoryNode Class**: Inherits from `Node` and represents a directory. It has an additional attribute `children` to store child nodes (files or directories).
- **FileSystem Class**: Manages the file system operations. It keeps track of the root directory and the current working directory.

### Design Decisions

1. **Node Structure**: The decision to have a generic `Node` class with `FileNode` and `DirectoryNode` subclasses allows for a flexible and scalable file system where both files and directories can be managed uniformly.
2. **In-Memory Representation**: Using an in-memory structure makes operations fast and simplifies the implementation since there is no need for persistent storage.
3. **Path Navigation**: Implementing path navigation with support for relative and absolute paths, as well as special directories (`..` and `/`), provides a user-friendly interface similar to real file systems.
4. **Error Handling**: The implementation includes error handling for invalid paths, non-existent files or directories, and other edge cases to ensure robustness.

### Current Limitations

The `ls` command works only for a specified directory and not for the current directory. This is why the unit test cases pass, as they specify the directory explicitly. Additionally, the ls command in this implementation lists only the files present in a directory and does not list the directories. 

### Setting Up the Environment

To ensure the environment is set up correctly, a Dockerfile is provided to create a consistent environment for running the file system.

#### Dockerfile

Here's the Dockerfile to set up the environment:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the CLI script when the container launches
CMD ["python", "src/cli.py"]
```

### Running the File System

To run the file system, follow these steps:

1. **Build the Docker Image**:
    ```sh
    docker build -t in-memory-file-system .
    ```

2. **Run the Docker Container**:
    ```sh
    docker run -it in-memory-file-system
    ```

Alternatively, the provided batch script (`run.bat`) can be used if on Windows, or the manual setup and running steps can be followed.

### Manual Setup Instructions

If Docker is not preferred, the environment can be manually set up to run the file system. Follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd in-memory-file-system
    ```

2. **Set Up a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run Unit Tests**:
    ```sh
    python -m unittest discover -s tests
    ```

5. **Start the Interactive CLI**:
    ```sh
    python src/cli.py
    ```

### Conclusion

This in-memory file system provides a user-friendly interface and supports various file operations efficiently. The implementation ensures flexibility and scalability through a well-designed node structure and handles errors gracefully to ensure robustness. The provided Dockerfile and setup instructions make it easy to run the file system in a consistent environment.
