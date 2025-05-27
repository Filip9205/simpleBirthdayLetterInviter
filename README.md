# 🎂 Simple Birthday Letter Inviter

Welcome to **Simple Birthday Letter Inviter** — a fun and beginner-friendly Python project that automatically generates personalized birthday invitation letters for your friends and loved ones! 🥳💌

---

## ✨ Features

- 📄 Reads a list of names from a text file
- 📝 Uses a customizable letter template
- ✂️ Automatically replaces placeholders with real names
- 📂 Saves individual letters for each recipient
- 💡 Great for learning Python basics: file I/O, loops, string manipulation

---

## 🗂️ Project Structure

simpleBirthdayLetterInviter/
├── .idea/ # IDE configuration files (optional)
├── Input/
│ ├── names.txt # List of invitee names (one per line)
│ └── letter_template.txt # Template letter with a [name] placeholder
├── Output/
│ └── (generated letters) # Personalized letters are saved here
├── main.py # Main script that runs the logic
└── .gitattributes # Git attributes file

## 🛠 How It Works

1. The script reads the `names.txt` file to get a list of names.
2. It loads the letter template from `letter_template.txt`.
3. For each name, it replaces `[name]` in the template with the actual name.
4. The personalized letters are saved in the `Output/` directory.
