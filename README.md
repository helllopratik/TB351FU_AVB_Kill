# Lenovo Tab Plus (TB351FU) AVB-Kill Suite

A standalone, completely open-source toolset to permanently disable **Android Verified Boot (AVB)** and stop "Device is Corrupt" (dm-verity) boot errors on the Lenovo TB351FU.

## 💡 Why use this?
When you unlock your bootloader or modify your boot/vendor partitions (e.g., for TWRP, Magisk Root, or a Custom Kernel), the tablet's security system detects the change. This results in:
1. **dm-verity failure**: The tablet refuses to boot into Android.
2. **"Device is Corrupt" message**: A red/black warning screen.

By running this patcher, you generate modified `vbmeta` images that set the hardware security flags to `0x03` (Disabled). This tells the MediaTek CPU to ignore all signature checks.

---

## 🛠️ How to Use (3 Simple Steps)

### Step 1: Provide Your Stock Images
To avoid copyright issues, we do not distribute Lenovo's proprietary `.img` files. 
You must extract the following three files from your **Stock Firmware** folder and place them directly into this `TB351FU_AVB_Kill` folder:
*   `vbmeta.img`
*   `vbmeta_system.img`
*   `vbmeta_vendor.img`

### Step 2: Run the Patcher
Once your three stock images are in the folder, run the Python script to patch them. This works on Linux, Windows, or macOS.

```bash
python3 patch_vbmeta.py
```
*The script will read your files and automatically generate `vbmeta_disabled.bin`, `vbmeta_system_disabled.bin`, and `vbmeta_vendor_disabled.bin` in the same folder.*

### Step 3: Flash the Patched Images
Reboot your tablet into **Fastboot Mode** (Power off, then hold **Volume Down + Power**).

If you are on Linux or macOS, you can use the automated installer:
```bash
chmod +x install.sh
./install.sh
```

**If you prefer to flash manually (or are on Windows), run these commands:**
```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta_disabled.bin
fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system_disabled.bin
fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor_disabled.bin
fastboot erase metadata
fastboot reboot
```

## ⚖️ License
The Python patcher and shell scripts are completely open-source and free to share. Do not upload your stock `.img` or patched `.bin` files to public repositories to avoid DMCA takedowns.
