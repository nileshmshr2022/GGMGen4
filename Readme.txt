

To create python package:
<python-install-dir>\pyinstaller --noconfirm --onedir --console --add-data "C:/GGM-Gen4/Code/GGMGen4/config.ini;." --hidden-import "win32timezone"  "C:/GGM-Gen4/Code/GGMGen4/gnnservice.py"

To delete service:
sc delete <servicename>

