# Library

# _Library Management System_

_This project is a console library management system. It offers basic functions for managing a collection of books, with data saved in a text file._


---

## Features

### Core Functionalities
**Add a Book**  
Users can add a new book to the library by specifying:
- Title *(required)*
- Author *(required)*
- Year of publication *(required)*  
Books are assigned a unique ID and a default status of `"available"`.

**Delete a Book**  
Removes a book from the library by its ID.

**Search for Books**  
Allows searching for books by:
* Title
* Author
* Year of publication

**Display All Books**  
Shows a formatted list of all books with the following details:
- ID
- Title
- Author
- Year
- Status (either `"available"` or `"borrowed"`)

**Update Book Status**  
Changes the status of a book from `"available"` to `"borrowed"` or vice versa.

### Persistent Storage
- Book data is saved to a text file (`library_data.txt`) to ensure it persists across program sessions.
- Existing data is loaded at startup, and new books are appended without overwriting the file.

### Error Handling
- Handles invalid inputs gracefully, such as:
  - Non-numeric values for numeric fields.
  - Attempting to delete or update books that don’t exist.
- Accepts empty inputs for optional fields like title and author, replacing them with placeholders.

---

## How to Run

### **Clone the Repository**  
   ```bash
   
   git clone https://github.com/Vildan07/Library.git
   ```

After cloning the repository, run the `library_editor.py` Python file.

