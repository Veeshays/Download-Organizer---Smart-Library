<<<<<<< HEAD
# Download Organizer – Smart Library

**Automatically organize your downloads into a clean, searchable Smart Library.**

Download Organizer – Smart Library is a Python-based Windows application that monitors a designated folder, categorizes newly added files in real time, and creates a structured digital library. Designed with a modular architecture, the project is built to evolve beyond simple file organization into an intelligent file management system with AI-powered classification, duplicate detection, metadata indexing, and semantic search.

---

## ✨ Features

### Current Features

* 📁 Real-time folder monitoring
* ⚡ Automatic file categorization
* 🖼️ Support for common file types (Images, PDFs, Documents, Videos, Music, Archives, Programs, etc.)
* 📂 Automatic category folder creation
* 📝 Logging stored separately from the library
* 🖥️ Cross-user compatibility (works on any Windows user account)
* 🧩 Modular project structure for easy expansion

### Planned Features

* File metadata extraction
* SQLite database for indexing
* SHA-256 duplicate detection
* AI-powered file classification
* Semantic file search
* Download analytics dashboard
* Desktop GUI
* Risk analysis for downloaded files

---

# 📂 Project Structure

```text
Download Organizer-Smart Library/
│
├── main.py
├── watcher.py
├── organizer.py
├── logger.py
├── config.py
├── metadata.py
├── duplicate_detector.py
├── database.py
├── classifier.py
├── risk_analyzer.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/download-organizer-smart-library.git
```

Navigate to the project folder:

```bash
cd download-organizer-smart-library
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# 🚀 First Launch

On the first run, the application automatically creates a library folder inside your user directory.

Default location:

```text
C:\Users\<YourUsername>\Smart Library
```

The following category folders are created automatically:

```text
Smart Library
│
├── Images
├── Documents
├── PDFs
├── Spreadsheets
├── Videos
├── Music
├── Programs
├── Archives
├── Python
├── Text
└── Others
```

Application data (logs and future databases) is stored separately inside Windows AppData:

```text
C:\Users\<YourUsername>\AppData\Local\DownloadOrganizer\
```

This keeps the Smart Library clean while preventing recursive file-watching events.

---

# 📥 Using the Application

There are two simple ways to use Download Organizer – Smart Library:

### Option 1 – Manual (Recommended while testing)

Save or drag files directly into the **Smart Library** folder.

The application will automatically detect the new file and move it into the appropriate category.

### Option 2 – Browser Downloads

Set your browser's default download location to the Smart Library folder.

Every new download will be organized automatically without any additional steps.

---

# 📍 Changing the Library Location

By default, the Smart Library is created in your home directory.

To use another location, open **config.py** and edit the following line:

```python
PROJECT_FOLDER = HOME / "Smart Library"
```

Examples:

```python
PROJECT_FOLDER = Path(r"D:\Smart Library")
```

or

```python
PROJECT_FOLDER = Path(r"E:\Downloads\My Library")
```

No other files need to be modified.

---

# 🛠 Technologies Used

* Python 3
* Watchdog
* pathlib
* shutil
* Object-Oriented Programming

---

# 🗺 Roadmap

* [x] Real-time folder monitoring
* [x] Automatic file categorization
* [x] Automatic folder creation
* [x] Cross-user compatibility
* [x] Windows AppData support
* [ ] Metadata extraction
* [ ] SQLite database
* [ ] Duplicate detection (SHA-256)
* [ ] AI-powered file classification
* [ ] Semantic search
* [ ] Download analytics dashboard
* [ ] Desktop GUI

---

# 🤝 Contributing

Contributions, suggestions, and bug reports are welcome. Feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.
=======
# Download-Organizer---Smart-Library
Automatically organizes downloads into a structured Smart Library with real-time monitoring.
>>>>>>> 5396c4a12cb52773acc706c3c89f84812a88fd9f
