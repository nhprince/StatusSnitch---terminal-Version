<h1 align="center">🕵️‍♂️ StatusSnitch (Terminal Edition)</h1>

<p align="center">
  <i>Facebook Messenger এর অনলাইন/অফলাইন স্টেটাস ট্র্যাক করুন রিয়েল-টাইমে — টার্মিনাল থেকেই!</i><br>
  <b>লাইটওয়েট, হ্যাকার-ফ্রেন্ডলি এবং সম্পূর্ণ প্রাইভেট 🛡️</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Selenium-Automation-success?style=for-the-badge&logo=selenium">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge&logo=windows">
</p>

---

## 🔍 What is StatusSnitch?

**StatusSnitch** is a Python-based terminal tool that allows you to monitor the **active (online/offline) status** of Facebook Messenger users in real-time by automating browser interactions with **Selenium**. It's designed for ethical hacking, personal use, and research, especially for those who love the command line interface (CLI).

---

## ✨ Key Features

- 📡 Real-time **Messenger status** tracking
- 🧠 **No password needed** – uses live browser session
- 🖥️ **CLI-based interface** – no GUI required
- 🕓 Accurate **timestamp** with logs
- 📁 Export logs as **CSV** and **TXT**
- 🚨 **CAPTCHA detection** & terminal warning
- 💨 Optional **headless (stealth) mode**

---

## 🛠️ প্রয়োজনীয়তা (Requirements)

**Python Version:**
- Python 3.9 বা তার বেশি

**Install dependencies:**
```bash
pip install -r requirements.txt
```

### Tools Required:
```bash
✅ Google Chrome Browser  
✅ ChromeDriver (same version as Chrome)
```

---

## ⚙️ Installation & Setup

### 🪟 Windows Users

#### 🔻 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/StatusSnitch.git
cd StatusSnitch
```

Or download as ZIP and extract manually.

#### 🧩 Step 2: Install Python & Dependencies
Make sure Python 3.9+ is installed.  
Install requirements:
```bash
pip install -r requirements.txt
```

#### 🌐 Step 3: ChromeDriver
- Check your Chrome version: `⋮ > Help > About Chrome`
- Download matching ChromeDriver from: https://chromedriver.chromium.org/downloads
- Place `chromedriver.exe` in the project directory or add it to PATH.

#### 🚀 Step 4: Run the Tool
```bash
python main.py
```

You’ll be prompted to enter a Facebook username or profile URL.  
Real-time updates will show in the terminal.

---

### 🐧 Linux Users

#### 🔻 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/StatusSnitch.git
cd StatusSnitch
```

#### 🧩 Step 2: Install Python & Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt
```

#### 🌐 Step 3: Chrome & ChromeDriver
```bash
# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
sudo apt --fix-broken install

# Check version
google-chrome --version

# Download matching ChromeDriver
wget https://chromedriver.storage.googleapis.com/124.0.6367.91/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver /usr/local/bin/
```

#### 🚀 Step 4: Run the Tool
```bash
python3 main.py
```

Enter the username or profile URL. Status will be printed live.

---

## 🧪 Example Terminal Output

```bash
[10:02:11] Target: prince.2024 - Status: ONLINE
[10:08:03] Target: prince.2024 - Status: OFFLINE
```

---

## 📁 Log Files

When you stop the script, the following files will be saved:
```bash
status_logs.csv
status_logs.txt
```

**Format:**
```bash
Timestamp | Username | Status
```

---

## 🚨 CAPTCHA Warning System

If Facebook triggers CAPTCHA:
- ⚠️ Terminal will display a warning.
- 🛑 You must solve it manually in the browser.
- 💡 CAPTCHA is more likely in headless mode or if requests are too frequent.

---

## ⚙️ Optional Settings (config.json)

```json
{
  "refresh_interval": 30,
  "headless": false
}
```

Use `--headless` flag for stealth mode:
```bash
python main.py --headless
```

---

## ✅ Best Practices

- 🧪 Use only for educational or ethical research.
- 🕵️ Do not violate anyone's privacy or Facebook policies.
- 🔐 Your password is **never stored** or accessed by this tool.

---

## 👨‍💻 Developer Info

**NH Prince Pradhan** aka **Nihal Cipher**  
💻 Ethical Hacker & Python Programmer  
🌐 [nhprince.blogspot.com]  
📧 nurulhudaprince18@gmail.com  

---

## 📜 License

**MIT License** — বিস্তারিত দেখুন `LICENSE` ফাইল

---

## 💬 Contact & Contribution

- 🐞 Report issues via GitHub [Issues]
- 🤝 Want to help? Fork & Pull Request!

---

<p align="center"> ⚠️ <b>ডিসক্লেইমার:</b> এই টুলটি শুধুমাত্র শিক্ষামূলক কাজে ব্যবহারের জন্য। দয়া করে আইন বা Facebook-এর নিয়ম লঙ্ঘন করবেন না। </p>  
<p align="center"> 🌙 Stay Smart • Stay Legal • Stay Curious 🌙 </p>
