#!/usr/bin/env python3
# Copyright (C) 2023 Tom Wolfskämpf. Licensed under the EUPL.
"""
The CLI interface for `pypercrypt`.

`pypercrypt` uses battle-tested cryptography to encrypt your data with the passphrase
of your choice and stores the ciphertext inside a QR code.
"""

import base64
import io
import json
import os
from typing import Annotated

import typer
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

app = typer.Typer()


def turn_passphrase_into_key(
    passphrase: str,
    salt: bytes | None = None,
) -> tuple[bytes, bytes]:
    """Derive key from passphrase.

    May use provided salt.

    Return key and salt.
    """
    if not salt:
        salt = base64.urlsafe_b64encode(os.urandom(16))

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    encoded_passphrase = passphrase.encode("utf-8")

    key = base64.urlsafe_b64encode(kdf.derive(encoded_passphrase))

    return key, salt


def read_cleartext_from_file(file: io.BufferedReader) -> bytes:
    """Read cleartext from a file-like object."""
    return file.read()


def read_ciphertext_from_file(file: io.TextIOWrapper) -> tuple[str, bytes]:
    """Read ciphertext and salt from a file-like object."""
    ciphertext_dict = json.loads(file.read())

    ciphertext = ciphertext_dict.get("ciphertext")
    salt = ciphertext_dict.get("salt").encode("utf-8")

    return ciphertext, salt


def encrypt_fernet(cleartext: bytes, key: str | bytes) -> bytes:
    """Encrypt cleartext with Fernet using the provided key."""
    f = Fernet(key)
    token = f.encrypt(cleartext)
    return token


def decrypt_fernet(ciphertext: str, key: bytes) -> bytes:
    """Decrypt ciphertext with Fernet using the provided key."""
    f = Fernet(key)
    cleartext = f.decrypt(ciphertext)
    return cleartext


@app.command()
def encrypt(
    input_file: Annotated[typer.FileBinaryRead, typer.Option()],
    output_file: Annotated[typer.FileTextWrite, typer.Option()],
) -> None:
    """Encrypt file content and output ciphertext to stdout."""
    cleartext = read_cleartext_from_file(input_file)
    passphrase = input("Enter passphrase: ")
    key, salt = turn_passphrase_into_key(passphrase)
    ciphertext = encrypt_fernet(cleartext=cleartext, key=key)
    result_dict = {"ciphertext": ciphertext.decode(), "salt": salt.decode()}
    output_file.write(json.dumps(result_dict))


@app.command()
def decrypt(
    input_file: Annotated[typer.FileText, typer.Option()],
    output_file: Annotated[typer.FileBinaryWrite, typer.Option()],
) -> None:
    """Decrypt file content and output cleartext to stdout."""
    ciphertext, salt = read_ciphertext_from_file(input_file)
    passphrase = input("Enter passphrase: ")
    key, _ = turn_passphrase_into_key(passphrase, salt)
    cleartext = decrypt_fernet(ciphertext=ciphertext, key=key)
    output_file.write(cleartext)


if __name__ == "__main__":
    app()
