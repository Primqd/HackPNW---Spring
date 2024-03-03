from PySide6.QtWidgets import QApplication
from PromptWindow import PromptWindow
import sys

def main() -> None: # Opening window code
    app = QApplication(sys.argv)
    main_window = PromptWindow()
    main_window.show()
    sys.exit(app.exec()) # close the app when app.exec() (clicking the x button) is called

if __name__ == "__main__":
    main()