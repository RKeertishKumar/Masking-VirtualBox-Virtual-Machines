# README: Masking VirtualBox Virtual Machines

This guide helps you hide virtualization details in VirtualBox VMs so that all software can run smoothly.

## **Purpose**
Some software is designed to detect and restrict functionality in virtualized environments, which can hinder testing, development, or compatibility. This guide provides practical steps to mask virtualization details in VirtualBox, enabling seamless operation of all applications within the VM.

---

## **Requirements**
- VirtualBox (version 6.x or later).
- A configured VM.
- Access to `VBoxManage`.

---

## **Steps**

### **1. Locate VBoxManage**
- **Windows**: `C:\Program Files\Oracle\VirtualBox\VBoxManage.exe`
- **Linux/macOS**: Accessible via `VBoxManage` in the terminal.

### **2. Shut Down the VM**
Ensure the VM is powered off before making changes.

### **3. Run Commands**

#### **Configuration Parameters and Their Purpose**
The table below describes the configuration parameters that can be modified using `VBoxManage` and their respective purposes.

| Parameter Name       | Description                                  |
|----------------------|----------------------------------------------|
| `DmiBIOSVersion`     | Masks the BIOS version.                     |
| `DmiSystemVendor`    | Sets a custom system vendor name.           |
| `DmiSystemProduct`   | Changes the system product name.            |
| `DmiSystemVersion`   | Updates the system version.                 |
| `DmiBoardVendor`     | Sets a custom board vendor name.            |
| `DmiBoardProduct`    | Modifies the board product name.            |

#### **Option 1: Copy-Paste Commands**
Replace `VM_NAME` with your VM name (e.g., `ubuntukk`):

1. **Set custom BIOS version**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion" "CustomBIOS"
   ```

2. **Set custom system vendor**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor" "CustomVendor"
   ```

3. **Set custom system product**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemProduct" "CustomProduct"
   ```

4. **Set custom system version**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVersion" "1.0"
   ```

5. **Set custom board vendor**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiBoardVendor" "CustomBoardVendor"
   ```

6. **Set custom board product**:
   ```bash
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "VM_NAME" "VBoxInternal/Devices/pcbios/0/Config/DmiBoardProduct" "CustomBoard"
   ```

#### **Option 2: Use a Python Script**
For automating the configuration, you can use the following Python script:

```python
import os

# Path to VBoxManage.exe
vboxmanage_path = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"

# Prompt user for the VM name
vm_name = input("Enter the name of the VM: ")

# Configuration settings
commands = [
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion" "CustomBIOS"',
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor" "CustomVendor"',
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemProduct" "CustomProduct"',
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVersion" "1.0"',
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiBoardVendor" "CustomBoardVendor"',
    f'setextradata "{vm_name}" "VBoxInternal/Devices/pcbios/0/Config/DmiBoardProduct" "CustomBoard"',
]

# Execute each command
for command in commands:
    full_command = f'"{vboxmanage_path}" {command}'
    print(f"Executing: {full_command}")
    os.system(full_command)

print("All settings applied successfully.")
```

### **4. Verify Changes**
Start the VM and use tools like `dmidecode` (Linux) or system properties (Windows) to confirm the modifications.

---

## **Troubleshooting**
- **Command Not Found**: Ensure `VBoxManage` path is correct.
- **Changes Not Applied**: Verify the VM name matches VirtualBox Manager.
