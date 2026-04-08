#!/usr/bin/env python3
import os
import sys

def kill_avb(name, filename, out_filename):
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(base_dir, filename)
    output_path = os.path.join(base_dir, out_filename)
    
    print(f"Looking for {filename}...")
    if not os.path.exists(file_path):
        print(f"  [!] ERROR: Could not find '{filename}' in the current folder.")
        print(f"      Please copy your stock '{filename}' into this folder and try again.\n")
        return False

    try:
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())
        
        # Offset 120 (0x78) is the standard AVB flag location
        # Setting to 0x03 disables both DM-Verity and Verification
        data[0x78] = 0x00
        data[0x79] = 0x00
        data[0x7A] = 0x00
        data[0x7B] = 0x03
        
        with open(output_path, 'wb') as f:
            f.write(data)
            
        print(f"  [SUCCESS] Patched {name} -> {out_filename}\n")
        return True
        
    except Exception as e:
        print(f"  [!] FATAL ERROR patching {name}: {e}\n")
        return False

def main():
    print("====================================================")
    print("   Lenovo TB351FU AVB-Kill Patcher (Standalone)")
    print("====================================================\n")
    
    success_count = 0
    
    # 1. Main VBMeta
    if kill_avb('VBMeta', 'vbmeta.img', 'vbmeta_disabled.bin'):
        success_count += 1
        
    # 2. VBMeta System
    if kill_avb('VBMeta System', 'vbmeta_system.img', 'vbmeta_system_disabled.bin'):
        success_count += 1
        
    # 3. VBMeta Vendor
    if kill_avb('VBMeta Vendor', 'vbmeta_vendor.img', 'vbmeta_vendor_disabled.bin'):
        success_count += 1

    print("====================================================")
    if success_count == 3:
        print("   ALL FILES PATCHED SUCCESSFULLY!")
        print("   You can now run ./install.sh to flash them via Fastboot.")
    else:
        print(f"   WARNING: Only {success_count}/3 files were patched.")
        print("   Please ensure all stock images are placed in this folder.")
    print("====================================================")

if __name__ == "__main__":
    main()
