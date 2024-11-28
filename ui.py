# ui.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QCheckBox, QMessageBox, QSpinBox, QApplication, QProgressBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from generator import PasswordGenerator
from strength_checker import PasswordStrengthChecker
import pyperclip
import os

class PasswordGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generator de Parole")
        self.setWindowIcon(QIcon('resources/icon.png'))
        self.init_ui()
        self.apply_stylesheet()

    def init_ui(self):
        layout = QVBoxLayout()

        # Lungimea parolei
        length_layout = QHBoxLayout()
        length_label = QLabel("Lungimea parolei:")
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 128)
        self.length_spinbox.setValue(12)
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_spinbox)
        layout.addLayout(length_layout)

        # Tipuri de caractere
        self.uppercase_checkbox = QCheckBox("Litere mari (A-Z)")
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox = QCheckBox("Litere mici (a-z)")
        self.lowercase_checkbox.setChecked(True)
        self.digits_checkbox = QCheckBox("Cifre (0-9)")
        self.digits_checkbox.setChecked(True)
        self.symbols_checkbox = QCheckBox("Simboluri (!@#...)")
        self.symbols_checkbox.setChecked(True)

        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.lowercase_checkbox)
        layout.addWidget(self.digits_checkbox)
        layout.addWidget(self.symbols_checkbox)

        # Butonul de generare
        self.generate_button = QPushButton("Generează Parola")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        # Afișarea parolei generate
        self.password_output = QLineEdit()
        self.password_output.setReadOnly(True)
        layout.addWidget(self.password_output)

        # Indicator de putere a parolei
        strength_layout = QHBoxLayout()
        strength_label = QLabel("Puterea parolei:")
        self.strength_bar = QProgressBar()
        self.strength_bar.setRange(0, 100)
        strength_layout.addWidget(strength_label)
        strength_layout.addWidget(self.strength_bar)
        layout.addLayout(strength_layout)

        # Butoane suplimentare
        buttons_layout = QHBoxLayout()
        self.copy_button = QPushButton("Copiază în Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.save_button = QPushButton("Salvează Parola")
        self.save_button.clicked.connect(self.save_password)
        buttons_layout.addWidget(self.copy_button)
        buttons_layout.addWidget(self.save_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def apply_stylesheet(self):
        if os.path.exists('style.qss'):
            with open('style.qss', 'r') as file:
                self.setStyleSheet(file.read())
        else:
            QMessageBox.warning(self, "Eroare", "Fișierul style.qss nu a fost găsit.")

    def generate_password(self):
        length = self.length_spinbox.value()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_lowercase = self.lowercase_checkbox.isChecked()
        use_digits = self.digits_checkbox.isChecked()
        use_symbols = self.symbols_checkbox.isChecked()

        try:
            generator = PasswordGenerator(
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase,
                use_digits=use_digits,
                use_symbols=use_symbols
            )
            password = generator.generate(length)
            self.password_output.setText(password)
            self.update_strength_bar(password)
        except ValueError as e:
            QMessageBox.warning(self, "Eroare", str(e))

    def update_strength_bar(self, password):
        checker = PasswordStrengthChecker()
        strength = checker.check_strength(password)
        strength_percentage = int(strength * 100)
        self.strength_bar.setValue(strength_percentage)

    def copy_to_clipboard(self):
        password = self.password_output.text()
        if password:
            pyperclip.copy(password)
            QMessageBox.information(self, "Copiere", "Parola a fost copiată în clipboard.")
        else:
            QMessageBox.warning(self, "Eroare", "Nu există nicio parolă de copiat.")

    def save_password(self):
        password = self.password_output.text()
        if password:
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")
            QMessageBox.information(self, "Salvare", "Parola a fost salvată în passwords.txt.")
        else:
            QMessageBox.warning(self, "Eroare", "Nu există nicio parolă de salvat.")
