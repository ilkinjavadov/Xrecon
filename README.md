# XRecon - GitHub Recon Tool for Ethical Hackers

**XRecon** is a lightweight, GitHub-based reconnaissance tool designed for red teamers, bug bounty hunters, and offensive security professionals. It scans public repositories of a given GitHub user or organization and identifies potentially sensitive files based on filename patterns.

---

## 🔍 Features

- Scans all public repositories of a target GitHub user/org
- Detects filenames that may contain secrets (e.g., `apikey`, `token`, `password`, etc.)
- Outputs a clean Markdown report with direct links to files
- Simple CLI interface

---

## 🚀 Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/xrecon.git
cd xrecon
```

### 2. Set up requirements
```bash
pip install -r requirements.txt
```

### 3. Set your GitHub token
```bash
export GITHUB_TOKEN=your_token_here
```

### 4. Run XRecon
```bash
python xrecon.py --target github_username --token $GITHUB_TOKEN
```

---

## 📁 Example Output
```
[+] Starting GitHub scan for target: openai
[+] Generating report...
[+] Scan complete. Report saved to output/results.md
```

---

## 📄 Output Report Format
```
# XRecon GitHub Scan Report

**2 potentially sensitive file(s) found.**

- 🔍 Repository: `internal-api`
  - 📄 File: `aws_secret_config.py`
  - 🔗 View File: https://github.com/target/internal-api/blob/main/aws_secret_config.py
```

---

## ⚠️ Disclaimer
This tool uses the GitHub API to fetch only **publicly available data**. It does not perform any unauthorized access or brute force attempts.

---

## 👨‍💻 Author
Made with ❤️ by Ilkin Javadov — World Class Ethical Hacker | Senior Penetration Tester

---

## 📜 License
MIT License
