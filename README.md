AtomicLib — Minimal Atomic File I/O for Python

A clean, zero‑dependency Python micro‑library providing true atomic file operations for both text and binary data.
Built for reliability, readability, and simplicity — no bloat, no noise, just correct atomicity.

(See https://softwareprograms.sell.app/product/pyatomic to purchase the product)

⚙️ Features

Atomic Write — temp‑write → flush → fsync → atomic replace

Atomic Read — thread‑safe reads with local locks

Atomic Delete — safe removal without race conditions

Binary Support — atomic bytes I/O included

Zero Dependencies — drop it in and use it instantly

Perfect for configs, vaults, local databases, automation tools, and anything that needs safe, guaranteed writes.

🧠 Why AtomicLib Exists

Atomic file operations are easy to get wrong.
AtomicLib gives you a minimal, production‑ready implementation that’s readable, stable, and correct — no frameworks, no over‑engineering.

💻 Quick Start After Download
from AtomicLib import file

# Atomic text write/read

file.atomicwrite("config.txt", "hello world")
print(file.atomicread("config.txt"))

# Atomic binary write/read

binaryfile.writebinary("data.bin", b"\x00\x01")
print(binaryfile.readbinary("data.bin"))

📦 Included in Download
Ready‑to‑use ZIP package containing AtomicLib.py



🔐 License
MIT — free for commercial and personal use.
