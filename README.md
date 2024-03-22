**File Encryption and Decryption Service**


This project is a Flask-based web service for encrypting and decrypting files using AES encryption with CBC mode. It also incorporates OTP (One-Time Password) verification for decryption.

Features:

File Encryption: Allows users to upload a file and encrypt it using a password.

File Decryption: Supports decrypting encrypted files using the decryption password and OTP verification.

AES Encryption: Utilizes AES encryption with CBC mode for secure encryption and decryption.

OTP Verification: Incorporates OTP verification using the PyOTP library to enhance security during decryption.

Prerequisites:

Python 3.x
Flask
cryptography library
pyotp library
hashlib library
Installation:
Clone the repository:

```
git clone <repository-url>
cd <repository-directory>
```

Install dependencies:

```
pip install flask cryptography pyotp
```

Usage:

Run the Flask server:

```
python app.py
```

Access the application via a web browser:

Open http://localhost:5000 in your web browser.
Upload a file for encryption and provide a password. Click the "Encrypt" button.

To decrypt a file, upload the encrypted file, provide the decryption password, and enter the OTP generated by your authenticator app. Click the "Decrypt" button.

Upon successful decryption, the decrypted file will be available for download or display.

Configuration:

The encryption and decryption passwords are passed as form parameters. Ensure strong passwords are used to enhance security.
The OTP secret key should be stored securely and shared only with authorized users.
