# main.py

import sys
from PyQt5.QtWidgets import QApplication
from ui import PasswordGeneratorUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorUI()
    window.show()
    sys.exit(app.exec_())
