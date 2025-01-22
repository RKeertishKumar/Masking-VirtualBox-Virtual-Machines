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
