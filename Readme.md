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

#### **Option 3: Use the Command-Line Tool**
For integrating these changes into automated workflows, you can use this Python-based command-line tool:

```python
import argparse
import subprocess
import sys

def apply_settings(vm_name):
    """Apply VirtualBox settings to the specified VM."""
    vboxmanage_path = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
    commands = [
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion", "CustomBIOS"],
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor", "CustomVendor"],
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiSystemProduct", "CustomProduct"],
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiSystemVersion", "1.0"],
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiBoardVendor", "CustomBoardVendor"],
        [vboxmanage_path, "setextradata", vm_name, "VBoxInternal/Devices/pcbios/0/Config/DmiBoardProduct", "CustomBoard"],
    ]

    for command in commands:
        try:
            print(f"Executing: {' '.join(command)}")
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                print(f"Error executing command: {' '.join(command)}")
                print(f"Error details: {result.stderr.strip()}")
                sys.exit(1)  # Exit on first failure
        except FileNotFoundError:
            print("Error: VBoxManage.exe not found. Please ensure VirtualBox is installed.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            sys.exit(1)

    print("All settings applied successfully.")

def main():
    parser = argparse.ArgumentParser(
        description="Command-line tool to apply custom VirtualBox settings to a VM."
    )
    parser.add_argument(
        "vm_name",
        metavar="VM_NAME",
        type=str,
        help="Name of the VirtualBox virtual machine."
    )

    args = parser.parse_args()

    if not args.vm_name:
        print("Error: VM name is required. Use --help for usage information.")
        sys.exit(1)

    apply_settings(args.vm_name)

if __name__ == "__main__":
    main()
```

**Usage**:
1. Save the script as `apply_settings.py`.
2. Run the script from the command line:
   ```bash
   python apply_settings.py VM_NAME
   ```
3. This is ideal for automated workflows to configure VMs and avoid failures.

### **4. Verify Changes**
Start the VM and use tools like `dmidecode` (Linux) or system properties (Windows) to confirm the modifications.

---

## **Troubleshooting**
- **Command Not Found**: Ensure `VBoxManage` path is correct.
- **Changes Not Applied**: Verify the VM name matches VirtualBox Manager.

