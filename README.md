# pypercrypt 📄🔐

[![Checked with mypy](https://img.shields.io/badge/mypy-checked-green)](https://mypy-lang.org/)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-success?logo=pre-commit)](./.pre-commit-config.yaml)
[![License EUPL](https://img.shields.io/badge/license-EUPL-green)](./LICENSE)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

`pypercrypt` uses battle-tested cryptography to encrypt your data with the passphrase of your choice
and stores the ciphertext inside a QR code.

Now you can store the printed QR code wherever you would trust other encrypted data to stay safe.

# Benefits

- 🔐 Makes encrypted long-term storage easy
- 📵 Truly offline backups
- 🖨️ Use what you already have
- 🔓 No lock-in, no proprietary formats—you don't need this tool to decrypt your data!

# Peer-Review

A peer review is pending, so keep that in mind when using `pypercrypt` for truly sensitive data.
Get in touch if you have the required expertise to review this tool.

# Roadmap

## Now

- Encrypt input data and turn it into a printable QR code
- Decrypt the data, relying on an external QR code scanner like `zbarimg`
- Reach 100 % test coverage of the critical code paths before adding new features

## Next

- Decrypt the data straight from an image file containing a QR code
- Instructions on how to decrypt the data purely with standard tools
- Maintain 100 % test-coverage of the critical code paths

## Later

- Let relevant experts perform an audit of this software
- Keep `pypercrypt` small and auditable by anyone
- A small scope is a feature
- Resist temptation to add more features

## Never

The following features will never be added to `pypercrypt`, either because they go against its goals or would
make the scope too large.

- Do not generate passphrases for the user
- Do not add asymmetric encryption support
- Do not add a GUI or TUI (if I can't resist, then i)

# Alternatives

- [`papercrypt`](https://github.com/TMUniversal/papercrypt) fulfills a similar purpose, is written in Go and
  not affiliated with this project

# License

Licensed under the EUPL. See [LICENSE](./LICENSE).