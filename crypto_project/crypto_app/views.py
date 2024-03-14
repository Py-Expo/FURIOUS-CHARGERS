from django.shortcuts import render, redirect
from django.http import HttpResponse
from Crypto import Random
from Crypto.Cipher import AES
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
import os

# Defined Functions

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

# View functions

def index(request):
    return render(request, 'crypto_app/index.html')

def encrypt_file(request):
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.FILES['file']
        
        # Create an instance of the Encryptor class
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        enc = Encryptor(key)
        
        # Encrypt the file
        encrypted_data = enc.encrypt(uploaded_file.read(), key)
        
        # Return the encrypted data as a file for download
        response = HttpResponse(encrypted_data, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}.enc"'.format(uploaded_file.name)
        
        return response
    
    return render(request, 'crypto_app/encrypt.html')

def decrypt_file(request):
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.FILES['file']
        
        # Create an instance of the Encryptor class
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        enc = Encryptor(key)
        
        # Decrypt the file
        decrypted_data = enc.decrypt(uploaded_file.read(), key)
        
        # Return the decrypted data as a file for download
        response = HttpResponse(decrypted_data, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(uploaded_file.name[:-4])
        
        return response
    
    return render(request, 'crypto_app/decrypt.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'crypto_app/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'crypto_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'crypto_app/signup.html', {'form': form})
