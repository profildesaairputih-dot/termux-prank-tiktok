#!/usr/bin/env python3
import subprocess, time, os, sys

def vibrate(dur=3000):
    subprocess.run(["termux-vibrate", "-f", "-d", str(dur)])

def toast(text, pos="top", color="red"):
    subprocess.run(["termux-toast", "-g", pos, "-b", color, text])

def flash_bg(color_code):
    """isi seluruh layar dengan warna latar ANSI"""
    os.system("clear")
    # cetak baris penuh background
    print(f"\033[{color_code}m" + " " * os.get_terminal_size().columns, end="")
    # geser kursor ke tengah (kasar)
    h = os.get_terminal_size().lines
    print(f"\033[{h//2}H", end="")

def main():
    vibrate(3000)
    toast("Baterai overload!\\nHP akan meledak dalam 5 detik ...")

    # hitung mundur + flashing hijau/merah
    for i in range(5, 0, -1):
        # hijau
        flash_bg(42)
        print(f"\033[1;30m{i}")   # teks hitam di tengah
        time.sleep(0.25)
        # merah
        flash_bg(41)
        print(f"\033[1;30m{i}")
        time.sleep(0.25)

    # selesai → warna normal
    os.system("clear")
    print("\033[0m", end="")      # reset ANSI
    toast("Prank! Santai bro 😎", pos="center", color="green")

if __name__ == "__main__":
    main()
