# 🚀 YouTube Automation System

A fully automated multi-channel YouTube Shorts uploader built with Python, Google Drive, Firestore, GitHub Actions, and the YouTube Data API.

The system automatically downloads videos from Google Drive, generates metadata, uploads videos to YouTube, and tracks uploaded videos using Firestore to prevent duplicate uploads.

---

# ✨ Features

- 📁 Google Drive Integration
- ▶️ Automatic YouTube Uploads
- 🔥 Firestore Upload Tracking
- 🤖 Metadata Generator
- 🔄 Duplicate Upload Prevention
- ☁️ GitHub Actions Automation
- 📊 Multi Channel Support
- ⚡ Fast & Modular Architecture
- 🔒 OAuth Authentication
- 📅 Scheduled Uploads (GitHub Actions)

---

# 🏗 Project Architecture

```
Google Drive
      │
      ▼
List Videos
      │
      ▼
Firestore
(Check uploaded?)
      │
      ▼
Metadata Generator
      │
      ▼
YouTube Upload
      │
      ▼
Firestore
(Store upload history)
      │
      ▼
Completed
```

---

# 📂 Project Structure

```
youtube-automation-run/

│
├── app/
│   ├── database/
│   ├── drive/
│   ├── logger/
│   ├── metadata/
│   ├── schemas/
│   ├── utils/
│   ├── youtube/
│   ├── config.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── pipeline.py
│   └── main.py
│
├── assets/
│   ├── credentials/
│   └── tokens/
│
├── temp/
│
├── .github/
│   └── workflows/
│       └── upload.yml
│
├── requirements.txt
├── run.py
└── README.md
```

---

# 🔥 Workflow

```
Google Drive

↓

Download Video

↓

Generate Metadata

↓

Check Firestore

↓

Already Uploaded?

├── Yes → Skip
└── No

↓

Upload to YouTube

↓

Save Upload Details

↓

Delete Local Temporary File

↓

Next Channel
```

---

# 🎯 Supported Channels

Currently supports **8 independent YouTube channels**.

Example:

```
Channel 1 – Movie Explain

Channel 2 – Hulk AI

Channel 3 – Natural Lofi

Channel 4 – Anime AI

Channel 5 – Tom & Jerry

Channel 6 – Animation Comedy

Channel 7 – Creepy Stories

Channel 8 – Cartoon
```

Each channel has:

- Google Drive Folder
- OAuth Token
- Metadata Generator
- Privacy Configuration

---

# 🔐 Technologies Used

- Python 3.11
- Google Drive API
- YouTube Data API v3
- Firebase Firestore
- Firebase Admin SDK
- GitHub Actions
- OAuth 2.0
- Google Service Account

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/saurabhkr1825-svg/youtube-automation-run.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create the following folders:

```
assets/
    credentials/
    tokens/
```

Required files

```
service_account.json

youtube_client.json

channel1.json

channel2.json

...

channel8.json
```

---

# ⚙ GitHub Secrets

Store the following secrets in GitHub Actions.

```
SERVICE_ACCOUNT_JSON

YOUTUBE_CLIENT_JSON

CHANNEL1_TOKEN
CHANNEL2_TOKEN
CHANNEL3_TOKEN
CHANNEL4_TOKEN
CHANNEL5_TOKEN
CHANNEL6_TOKEN
CHANNEL7_TOKEN
CHANNEL8_TOKEN
```

---

# ☁ GitHub Actions

Runs automatically.

Current schedule

```
08:00 AM IST

08:00 PM IST
```

Also supports manual execution from the Actions tab.

---

# 🔥 Firestore

Collection

```
uploads
```

Document Example

```
channel1_1AbCDeFgHi

channel
filename
drive_file_id
youtube_video_id
title
uploaded_at
```

---

# 📈 Current Features

- Google Drive Video Listing
- Google Drive Download
- Multi Channel Upload
- Metadata Generator
- Firestore Integration
- Duplicate Detection
- OAuth Authentication
- Automatic Upload
- GitHub Actions Deployment

---

# 🚧 Future Improvements

- Telegram Notifications
- AI Generated Titles
- AI Generated Descriptions
- AI Generated Tags
- Upload Dashboard
- Retry Mechanism
- Analytics Dashboard
- Automatic Scheduling
- Error Reporting

---

# 👨‍💻 Author

**Saurabh Kumar**

B.Tech Civil Engineering  
Indian Institute of Technology Patna

GitHub

https://github.com/saurabhkr1825-svg

---

# ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub.
