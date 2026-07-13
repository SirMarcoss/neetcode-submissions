import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        undercase = s.lower().replace(" ", "").replace(",", "")
        testo_pulito = re.sub(r'[^a-zA-Z0-9]', '', undercase)
        i = 0
        j = len(testo_pulito) -1
        while i  < j:
            if testo_pulito[i] == testo_pulito[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        



        
        