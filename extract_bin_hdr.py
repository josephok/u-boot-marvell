#!/usr/bin/env python3
"""
Extract raw bin_hdr from a Marvell kwbimage SPI flash dump.

Usage: extract_bin_hdr.py <firmware.bin>
Output: orig_bin_hdr_raw.bin (in current directory)

Image format:
  - Main header: 32 bytes
  - Extension header head (headExtBHR_t): 4 bytes
      type   (1B) + lenMsb (1B) + lenLsb (2B LE)
      total length = (lenMsb << 16) | lenLsb  (includes head + content + tail)
  - Raw bin_hdr content: ext_len - 8 bytes  (strip 4B head + 4B tail)
  - Extension header tail (tailExtBHR_t): 4 bytes
"""

import struct
import sys
import os

def extract(firmware_path, output_path="orig_bin_hdr_raw.bin"):
    with open(firmware_path, "rb") as f:
        data = f.read()

    # Extension header starts at offset 32 (right after main header)
    offset = 32
    ext_type = data[offset]
    len_msb  = data[offset + 1]
    len_lsb  = struct.unpack_from("<H", data, offset + 2)[0]
    ext_len  = (len_msb << 16) | len_lsb

    if ext_type != 0x02:
        print(f"Warning: unexpected extension type 0x{ext_type:02x} (expected 0x02 for BIN_HDR)")

    # Strip 4-byte head and 4-byte tail
    raw_data = data[offset + 4 : offset + ext_len - 4]

    with open(output_path, "wb") as out:
        out.write(raw_data)

    print(f"Extracted {len(raw_data)} bytes -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <firmware.bin>")
        sys.exit(1)
    extract(sys.argv[1])
