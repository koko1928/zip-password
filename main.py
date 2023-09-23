import zipfile
import itertools

zip_file_path = "example.zip"

min_password = "password1"
max_password = "password3"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:'\"<>,.?/\\|"

with zipfile.ZipFile(zip_file_path) as zip_file:
    for length in range(len(min_password), len(max_password)+1):
        for password in itertools.product(chars, repeat=length):
            password = "".join(password)
            if password >= min_password and password <= max_password:
                try:
                    zip_file.extractall(pwd=password.encode())
                    print("Success! Password is: " + password)
                    break
                except:
                    continue
