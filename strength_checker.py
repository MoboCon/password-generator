# strength_checker.py

import re

class PasswordStrengthChecker:
    def check_strength(self, password):
        length_score = min(len(password) / 12, 1)
        variety_score = self._calculate_variety_score(password)
        strength = (length_score + variety_score) / 2
        return strength

    def _calculate_variety_score(self, password):
        score = 0
        patterns = [
            r'[a-z]',           # Litere mici
            r'[A-Z]',           # Litere mari
            r'\d',              # Cifre
            r'[!@#$%^&*(),.?":{}|<>]'  # Simboluri
        ]
        for pattern in patterns:
            if re.search(pattern, password):
                score += 0.25
        return score
