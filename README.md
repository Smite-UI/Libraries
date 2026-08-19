AtomicLib — True Atomic File I/O for Python
A zero‑dependency Python micro‑library providing real atomic file operations for text, bytes, binary blobs, and bytearrays.
Built for reliability, simplicity, and correctness — no bloat, no noise, just atomicity done right.

⚙️ Features
Atomic Write — temp‑write → flush → fsync → atomic replace

Atomic Read — thread‑safe reads with local locks

Atomic Delete — safe removal without race conditions

Binary Support — atomic bytes, bytearray, and binary blob I/O

Zero Dependencies — pure Python, drop‑in ready

Cross‑platform — Windows, macOS, Linux

Perfect for configs, vaults, local databases, ML checkpoints, automation tools, and anything that needs safe, guaranteed writes.

🧠 Why AtomicLib Exists
Normal Python file writes are not atomic.
If your program crashes mid‑write, you get:

corrupted files

partial writes

torn binary data

broken configs

invalid checkpoints

AtomicLib guarantees crash‑safe writes using the same strategy used by databases and secure storage systems:

write to a temp file

flush

fsync

atomic replace

This ensures your file is never left in a corrupted state, even during power loss or crashes.

📦 Download
AtomicLib is distributed as a ready‑to‑use ZIP package.

Purchase the full version here:  
https://softwareprograms.sell.app/product/pyatomic

💻 Quick Start
Import
python
from AtomicLib import file, binaryfile
Atomic text write/read
python
file.atomicwrite("config.txt", "hello world")
print(file.atomicread("config.txt"))
Atomic binary write/read
python
binaryfile.writebinary("data.bin", b"\x00\x01")
print(binaryfile.readbinary("data.bin"))
Atomic bytearray write/read
python
data = bytearray([10, 20, 30])
binaryfile.writebinary("buffer.bin", data)
print(binaryfile.readbinary("buffer.bin"))
🔐 License — Perpetual Personal‑Use License
You are granted a perpetual, non‑exclusive, non‑transferable license to use AtomicLib for personal, non‑commercial purposes only.

You may:
Use the software indefinitely for personal projects

Modify the software privately for personal use

You may NOT:
Use the software for commercial or organizational purposes

Sell, rent, lease, sublicense, or redistribute the software

Share the software publicly or include it in public repositories

Modify the software for distribution

Reverse‑engineer or bypass licensing restrictions

All rights not expressly granted remain the property of the author.
© 2026 Smite — All Rights Reserved.

🧩 Included in Download
AtomicLib.py

Ready‑to‑use ZIP package
