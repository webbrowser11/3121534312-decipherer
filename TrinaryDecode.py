# =====================================================
#  3121534312's Cipher - Trinary Text Encoder/Decoder
# =====================================================

def encode_text(text: str) -> str:
    """Encode the given text using 3121534312's trinary cipher."""
    encoded = ""
    for i in text:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            idx = "abcdefghijklmnopqrstuvwxyz".index(i.lower())
            code = "123"[idx // 9] + "123"[(idx % 9) // 3] + "123"[idx % 3]
            encoded += code
        elif i == " ":
            encoded += "0"
        elif i.isdigit():
            if i in "123456789":
                idx = "123456789".index(i)
                code = "123"[idx // 3] + "8" + "123"[idx % 3]
                encoded += code
            else:
                encoded += "118"
        elif i in ".?!,-;:@#/%$\\'\"()+-_*=^÷":
            punctuation_codes = {
                '.': '117', '?': '227', '!': '337', ',': '127', '-': '217',
                ';': '237', ':': '317', '@': '711', '#': '712', '/': '713',
                '%': '721', '$': '722', '\\': '723', "'": '171', '"': '272',
                '(': '373', ')': '474', '+': '811', '_': '812', '*': '813',
                '÷': '821', '=': '822', '^': '823'
            }
            encoded += punctuation_codes[i]
        else:
            # Unicode fallback encoding
            codepoint = f"{ord(i):X}"
            unicode_code = "791"
            for digit in codepoint:
                unicode_code += encode_text(digit)
            unicode_code += "791"
            encoded += unicode_code

    # Compact the cipher
    encoded = encoded.replace("11", "4").replace("22", "5").replace("33", "6")
    return encoded


def decode_text(code: str) -> str:
    """Decode text from 3121534312's trinary cipher."""
    code = code.replace("4", "11").replace("5", "22").replace("6", "33").replace("0", "000")

    decoded = ""
    unimode = False
    unichar = ""
    i = 0

    while i < len(code):
        chunk = code[i:i+3]
        if chunk == "000":
            decoded += " "
        elif len(chunk) != 3:
            decoded += "�"
        elif chunk == "791":
            if unimode:
                unimode = False
                unichar = decode_text(unichar)
                decoded += chr(int(unichar, 16))
                unichar = ""
            else:
                unimode = True
                unichar = ""
        elif unimode:
            unichar += chunk
        elif all(c in "123" for c in chunk):
            idx = (int(chunk[0]) - 1) * 9 + (int(chunk[1]) - 1) * 3 + (int(chunk[2]) - 1)
            decoded += "abcdefghijklmnopqrstuvwxyz"[idx]
        elif chunk[1] == "8":
            idx = (int(chunk[0]) - 1) * 3 + (int(chunk[2]) - 1)
            decoded += "123456789"[idx]
        elif chunk == "118":
            decoded += "0"
        elif chunk in (
            '117', '227', '337', '127', '217', '237', '317',
            '711', '712', '713', '721', '722', '723', '171',
            '272', '373', '474', '811', '812', '813', '821',
            '822', '823'
        ):
            punctuation_map = {
                '117': '.', '227': '?', '337': '!', '127': ',', '217': '-',
                '237': ';', '317': ':', '711': '@', '712': '#', '713': '/',
                '721': '%', '722': '$', '723': '\\', '171': "'", '272': '"',
                '373': '(', '474': ')', '811': '+', '812': '_', '813': '*',
                '821': '÷', '822': '=', '823': '^'
            }
            decoded += punctuation_map[chunk]
        else:
            decoded += '�'
        i += 3
    return decoded


if __name__ == "__main__":
    print("=== 3121534312's Trinary Cipher ===")
    print("Type text to encode or numeric code to decode.")
    print("Type 'exit' to quit.\n")

    while True:
        text = input("> ")
        if text.lower() == "exit":
            break
        if all(c in "0123456789" for c in text):
            print("Decoded:", decode_text(text))
        else:
            print("Encoded:", encode_text(text))
