import os
import tempfile

keys = {'a':'aaaaa', 'b':'aaaab', 'c':'aaaba', 'd':'aaabb',
        'e':'aabaa',  'f':'aabab', 'g':'aabba', 'h':'aabbb',
        'i':'abaaa', 'j':'abaab','k':'ababa', 'l':'ababb',
        'm':'abbaa', 'n':'abbab', 'o':'abbba','p':'abbbb',
        'q':'baaaa', 'r':'baaab', 's':'baaba', 't':'baabb' ,
        'u':'babaa', 'v':'babab', 'w':'babba', 'x':'babbb',
        'y':'bbaaa', 'z':'bbaab', ' ':'bbaba'}

class Shifr: 

    @staticmethod
    def shifr_text_ROT(text:str) -> str:
        """Функция шифрации/дешифрации текста шифром ROT13"""
        result = ''
        for char in text:
            if 'a' <= char <= 'z':
                start = ord('a')
            elif 'A' <= char <= 'Z':
                start = ord('A')
            else:
                result += char
                continue

            shifted_char = chr((ord(char) - start + 13) % 26 + start)
            result += shifted_char
        return result

    @staticmethod
    def shifr_text_bekon(text:str) -> str:
        """Функция шифрации текста шифром Бекона"""
        encrypt = ""
        for char in text.lower():
            if char in keys:
                encrypt += keys[char]
            else:
                encrypt += " "
        return encrypt

    @staticmethod
    def deshifr_text_bekon(text:str) -> str:
        """Функция дешифрации текста из шифра Бекона"""
        decrypt = ""
        if len(text) % 5 != 0:
            raise ValueError("Длина текста должна быть кратна 5.")

        for i in range(0, len(text), 5):
            chunk = text[i:i + 5]
            found = False
            for key, value in keys.items():
                if value == chunk:
                    decrypt += key
                    found = True
                    break
            if not found:
                decrypt += "?"
        return decrypt
    
    @staticmethod
    def shifr_file_ROT(read_path: str, write_path: str) -> None:
        """Функция шифрации/дешифрации файла шифром ROT13"""
        try:
            with open(read_path, 'r') as f_in, open(write_path, 'w') as f_out:
                for line in f_in:
                    encrypted_line = Shifr.shifr_text_ROT(line)
                    f_out.write(encrypted_line)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {read_path}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    
    @staticmethod
    def shifr_file_bekon(read_path: str, write_path: str) -> None:
        """Функция шифрации файла шифром Бекона"""
        try:
            with open(read_path, 'r') as f_in, open(write_path, 'w') as f_out:
                for line in f_in:
                    encrypted_line = Shifr.shifr_text_bekon(line)
                    f_out.write(encrypted_line + '\n')
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {read_path}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    
    @staticmethod
    def deshifr_file_bekon(read_path: str, write_path: str) -> None:
        """Функция дешифрации файла из шифра Бекона"""
        try:
            with open(read_path, 'r') as f_in, open(write_path, 'w') as f_out:
                for line in f_in:
                    try:
                        decrypted_line = Shifr.deshifr_text_bekon(line.strip())
                        f_out.write(decrypted_line + '\n')
                    except ValueError as e:
                        print(f"Ошибка дешифрования строки: {e}")
                        f_out.write("Ошибка дешифрования\n")
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {read_path}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")