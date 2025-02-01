from cryptography.fernet import Fernet
import os
from dotenv import dotenv_values, set_key


class SecureConfigManager:
    def __init__(self, env_file=".env", key_file=".key", connection_details=None):
        self.env_file = env_file
        self.key_file = key_file
        self.fernet = self.load_or_generate_key()
        self.create_env()
        self.connection_details = connection_details


    def load_or_generate_key(self):
        """Load existing encryption key or generate a new one."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
        return Fernet(key)

    def create_env(self):
        """Create an empty .env file if it doesn't exist."""
        if not os.path.exists(self.env_file):
            with open(self.env_file, "w") as f:
                f.write("# .env file for storing encrypted configuration settings\n")

    def encrypt(self, value):
        """Encrypt a value."""
        return self.fernet.encrypt(value.encode()).decode()

    def decrypt(self, value):
        """Decrypt a value."""
        return self.fernet.decrypt(value.encode()).decode()

    def write(self, key, value):
        """Encrypt and write a key-value pair to the .env file."""
        encrypted_value = self.encrypt(value)
        set_key(self.env_file, key, encrypted_value)

    def read(self, key):
        """Read and decrypt a value from the .env file."""
        config = dotenv_values(self.env_file)
        if key in config and config[key]:
            try:
                return self.decrypt(config[key])
            except Exception:
                return None
        return None

    def delete(self, key):
        """Remove a key from the .env file."""
        config = dotenv_values(self.env_file)
        if key in config:
            del config[key]
            with open(self.env_file, "w") as f:
                for k, v in config.items():
                    f.write(f"{k}={v}\n")

    def get_all(self):
        """Retrieve all stored keys and their decrypted values."""
        config = dotenv_values(self.env_file)
        decrypted_config = {}
        for k, v in config.items():
            try:
                decrypted_config[k] = self.decrypt(v)
            except Exception:
                decrypted_config[k] = None
        return decrypted_config


