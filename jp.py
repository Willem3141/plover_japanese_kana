import re

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key):
    assert len(key) <= LONGEST_KEY
    
    if key[0] == "*":
        raise KeyError
    
    p = re.compile("([STKPWHR]*)([-AOEU*]*)([FRPBLGTSDZ]*)")
    m = p.match(key[0])
    if not m:
        raise KeyError
    initial = m.group(1)
    vowel = m.group(2)
    final = m.group(3)
    
    hiragana = {
        "": "あいうえお",
        "K": "かきくけこ",
        "TKPW": "がぎぐげご",  # G
        "S": "さしすせそ",
        "STKPW": "ざじずぜぞ",  # Z
        "T": "たちつてと",
        "TK": "だぢづでど",  # D
        "TPH": "なにぬねの",  # N
        "H": "はひふへほ",
        "PW": "ばびぶべぼ",  # B
        "P": "ぱぴぷぺぽ",
        "TP": ["ふぁ","ふぃ","ふ","ふぇ","ふぉ"],  # F
        "PH": "まみむめも",  # M
        "KWR": ["や","ぃ","ゆ","いぇ","よ"],  # Y
        "R": "らりるれろ",
        "W": ["わ","うぃ","う","うぇ","を"],
        "KP": ["ぁ","ぃ","ぅ","ぇ","ぉ"],
        # palatalized sounds
        "KR": ["きゃ","きぃ","きゅ","きぇ","きょ"],
        "TKPWR": ["ぎゃ","ぎぃ","ぎゅ","ぎぇ","ぎょ"],
        "SH": ["しゃ","し","しゅ","しぇ","しょ"],
        "SKWR": ["じゃ","じ","じゅ","じぇ","じょ"],
        "KH": ["ちゃ","ち","ちゅ","ちぇ","ちょ"],
        "TPHR": ["にゃ","にぃ","にゅ","にぇ","にょ"],
        "HR": ["ひゃ","ひぃ","ひゅ","ひぇ","ひょ"],
        "PWR": ["びゃ","びぃ","びゅ","びぇ","びょ"],
        "PR": ["ぴゃ","ぴぃ","ぴゅ","ぴぇ","ぴょ"],
        "PHR": ["みゃ","みぃ","みゅ","みぇ","みょ"],
        "WR": ["りゃ","りぃ","りゅ","りぇ","りょ"],
        }
    if not hiragana[initial]:
        raise KeyError
    
    result = ""
    
    # short vowel
    if vowel == "A":
        result = hiragana[initial][0]
    elif vowel == "AE":
        result = hiragana[initial][0] + "あ"
    elif vowel == "AOEU":
        result = hiragana[initial][0] + "い"
    elif vowel == "EU":
        result = hiragana[initial][1]
    elif vowel == "AOE":
        result = hiragana[initial][1] + "い"
    elif vowel == "U":
        result = hiragana[initial][2]
    elif vowel == "AOU":
        result = hiragana[initial][2] + "う"
    elif vowel == "E":
        result = hiragana[initial][3]
    elif vowel == "AEU":
        result = hiragana[initial][3] + "い"
    elif vowel == "O":
        result = hiragana[initial][4]
    elif vowel == "OE":
        result = hiragana[initial][4] + "う"
    elif vowel == "OEU":
        result = hiragana[initial][4] + "い"
    
    if result == "":
        raise KeyError
    
    final = final.replace("FPL", "ー")
    final = final.replace("FP", "ち")
    final = final.replace("RB", "し")
    final = final.replace("PBLG", "じ")
    final = final.replace("PB", "ん")
    final = final.replace("BG", "く")
    final = final.replace("TS", "つ")

    final = final.replace("F", "ふ")
    final = final.replace("R", "る")
    final = final.replace("P", "ぷ")
    final = final.replace("B", "ぶ")
    final = final.replace("L", "っ")
    final = final.replace("G", "ぐ")
    final = final.replace("T", "と")
    final = final.replace("S", "す")
    final = final.replace("D", "ど")
    final = final.replace("Z", "ず")
    result += final
    
    return "{^" + result + "^}"

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
    return []

