#!/bin/bash

# TB351FU AVB Kill - Standalone Flasher
# This script disables Android Verified Boot (AVB) to stop "Device is Corrupt" errors.

echo "===================================================="
echo "   Lenovo TB351FU AVB-Kill (Universal Disabler)"
echo "===================================================="

# Check for fastboot
if ! command -v fastboot &> /dev/null; then
    echo "Error: fastboot not found. Please install platform-tools."
    exit 1
fi

echo "1. Put your tablet in Fastboot Mode (Hold Vol Down + Power)."
echo "2. Connect the USB cable."
read -p "Press Enter to start flashing..."

echo -e "\n[1/4] Disabling Main Verification..."
fastboot --disable-verity --disable-verification flash vbmeta vbmeta_disabled.bin

echo -e "\n[2/4] Disabling System Verification..."
fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system_disabled.bin

echo -e "\n[3/4] Disabling Vendor Verification..."
fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor_disabled.bin

echo -e "\n[4/4] Clearing Metadata (Required to reset security flags)..."
fastboot erase metadata

echo -e "\n===================================================="
echo "   AVB-KILL COMPLETE!"
echo "   You can now flash custom kernels and bootloaders."
echo "===================================================="
fastboot reboot
