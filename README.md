# 🔓 Bypass403 - Advanced 403 Forbidden Bypass Tool

**Bypass403** is a Python-based tool designed for bug bounty hunters and penetration testers to automate the detection of 403 Forbidden bypass vulnerabilities. It uses a wide range of payloads and headers to test restricted endpoints and find potential access misconfigurations.

---

🚀 Features

- ✅ 50+ curated payloads for 403 bypass (path obfuscation, encoding, WAF/CDN tricks)
- ✅ Tests header-based bypasses (`X-Forwarded-For`, `X-Original-URL`, etc.)
- ✅ Supports single URL or file input
- ✅ Highlights successful `[200 OK]` responses in green
- ✅ Final summary of all successful bypass attempts
- ✅ Simple, readable Python code — easy to modify or extend

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/bypass403.git
cd bypass403
chmod +x bypass403.py
To make it globally executable:

bash
Copy
Edit
sudo mv bypass403.py /usr/local/bin/bypass403
🧪 Usage
▶️ Test a single URL:
bash
Copy
Edit
bypass403 -u https://target.com/secret
📁 Test multiple URLs from a file:
bash
Copy
Edit
bypass403 -f urls.txt
📌 Make sure each line in urls.txt is a full URL with path, for example:

arduino
Copy
Edit
https://admin.example.com/hidden
http://api.example.com/private
📝 Output Example
csharp
Copy
Edit
[+] Testing: https://target.com/admin
[403] https://target.com/admin
[200] https://target.com/admin/..;
[403] https://target.com/admin;%2f
...

==================================================
🟢 Bypass Summary:
- https://target.com/admin/..;
⚠️ Disclaimer
This tool is intended for educational purposes and authorized security testing only.
Using it against systems without permission is illegal and unethical.
