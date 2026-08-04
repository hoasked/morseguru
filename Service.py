# Sound Options
DOTIME = 150
FREQUENCY = 750

# Languages Available
LANGUAGES = [
    "English",
    "Русский",
    "Ελληνικά",
    "العربية",
    "עברית",
    "日本語",
    "한국어",
    "Polski",
    "Español",
    "Français",
    "Deutsch",
    "Italiano",
    "Türkçe",
    "Português",
    "Українська"
]

# -----------------------------------------------------------
# 15 languages with Morse variants different from English
# Each entry: (forward_dict, reverse_dict)
# forward_dict:   { character : morse_code }
# reverse_dict:   { morse_code : character }  (may overwrite duplicates)
# ------------------------------------------------------------

# ---------- base building blocks ----------
_ENG_LATIN = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
}

_NUMBERS = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}


def _make_forward(base, extras):
    """Merge base Latin + numbers + language-specific extras."""
    d = {}
    d.update(base)
    d.update(_NUMBERS)
    d.update(extras)
    return d


def _make_reverse(forward):
    """Reverse the forward dict (morse -> char)."""
    return {v: k for k, v in forward.items()}


# ---------- language‑specific extra mappings ----------

# 1. English (standard international, no extras)
_ENG_EXTRAS = {}
ENG_FWD = _make_forward(_ENG_LATIN, _ENG_EXTRAS)
ENG_REV = _make_reverse(ENG_FWD)

# 2. Русский (Russian Cyrillic)
_RU_EXTRAS = {
    "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..",
    "Е": ".", "Ж": "...-", "З": "--..", "И": "..", "Й": ".---",
    "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---",
    "П": ".--.", "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
    "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.", "Ш": "----",
    "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..",
    "Ю": "..--", "Я": ".-.-.",
}
RU_FWD = _make_forward({}, _RU_EXTRAS)   # no Latin base for Russian
RU_REV = _make_reverse(RU_FWD)

# 3. Ελληνικά (Greek)
_GR_EXTRAS = {
    "Α": ".-", "Β": "-...", "Γ": "--.", "Δ": "-..", "Ε": ".",
    "Ζ": "--..", "Η": "....", "Θ": "-.-.", "Ι": "..", "Κ": "-.-",
    "Λ": ".-..", "Μ": "--", "Ν": "-.", "Ξ": "-..-", "Ο": "---",
    "Π": ".--.", "Ρ": ".-.", "Σ": "...", "Τ": "-", "Υ": "-.--",
    "Φ": "..-.", "Χ": "----", "Ψ": "--.-", "Ω": ".--.-",
}
GR_FWD = _make_forward({}, _GR_EXTRAS)
GR_REV = _make_reverse(GR_FWD)

# 4. العربية (Arabic)
_AR_EXTRAS = {
    "ا": ".-", "ب": "-...", "ت": "-", "ث": "-.-.", "ج": ".---",
    "ح": "....", "خ": "-.-.", "د": "-..", "ذ": "--..", "ر": ".-.",
    "ز": "--.-", "س": "...", "ش": "----", "ص": "-.--", "ض": "...-",
    "ط": "..-", "ظ": ".--.", "ع": ".-.-.", "غ": "--.", "ف": "..-.",
    "ق": "--.-", "ك": "-.-", "ل": ".-..", "م": "--", "ن": "-.",
    "ه": "..-..", "و": ".--", "ي": "..--",
}
AR_FWD = _make_forward({}, _AR_EXTRAS)
AR_REV = _make_reverse(AR_FWD)

# 5. עברית (Hebrew)
_HE_EXTRAS = {
    "א": ".-", "ב": "-...", "ג": "--.", "ד": "-..", "ה": ".",
    "ו": "...-", "ז": "--..", "ח": "....", "ט": "-", "י": "..",
    "כ": "-.-", "ל": ".-..", "מ": "--", "נ": "-.", "ס": "...",
    "ע": ".---", "פ": ".--.", "צ": ".-..", "ק": "--.-", "ר": ".-.",
    "ש": "----", "ת": "-",
}
HE_FWD = _make_forward({}, _HE_EXTRAS)
HE_REV = _make_reverse(HE_FWD)

# 6. 日本語 (Japanese Wabun – Hiragana subset)
_JA_EXTRAS = {
    "ア": ".-", "イ": "..", "ウ": "..-", "エ": "-...-", "オ": ".-...",
    "カ": ".-..", "キ": "-.-..", "ク": "...-", "ケ": "-.-.", "コ": "----",
    "サ": "-.-.-", "シ": "--.-.", "ス": "---.-", "セ": ".---.", "ソ": "---.",
    "タ": "-.", "チ": "..-.", "ツ": ".--.", "テ": ".-.-", "ト": "..-..",
    "ナ": ".-.", "ニ": "-.-.", "ヌ": "....", "ネ": "--.-", "ノ": "..--",
    "ハ": "-...", "ヒ": "--..", "フ": "--..", "ヘ": ".", "ホ": "-..",
    "マ": "-..-", "ミ": "..-.-", "ム": "-", "メ": "-...-", "モ": "-..-.",
    "ヤ": ".--", "ユ": "-..--", "ヨ": "--.", "ラ": "...", "リ": "--.",
    "ル": "-.-.", "レ": "---.", "ロ": ".-.-", "ワ": "-.-", "ヲ": ".---",
    "ン": ".-.-.",
}
JA_FWD = _make_forward({}, _JA_EXTRAS)
JA_REV = _make_reverse(JA_FWD)

# 7. Polski (Polish)
_PL_EXTRAS = {
    "Ą": ".-.-", "Ć": "-.-..", "Ę": "..-..", "Ł": ".-..-",
    "Ń": "--.--", "Ó": "---.", "Ś": "...-...", "Ź": "--..-.",
    "Ż": "--..-",
}
PL_FWD = _make_forward(_ENG_LATIN, _PL_EXTRAS)
PL_REV = _make_reverse(PL_FWD)

# 8. Español (Spanish)
_ES_EXTRAS = {
    "Ñ": "--.--", "Á": ".--.-", "É": "..-..", "Í": "..-..",
    "Ó": "---.", "Ú": "..--", "Ü": "..--",
}
ES_FWD = _make_forward(_ENG_LATIN, _ES_EXTRAS)
ES_REV = _make_reverse(ES_FWD)

# 9. Français (French)
_FR_EXTRAS = {
    "À": ".--.-", "Â": ".-.-", "Ç": "-.-..", "É": "..-..",
    "È": ".-..-", "Ê": "..-..", "Ë": ".-..-", "Î": "..-..",
    "Ï": "..-..", "Ô": "---.", "Œ": ".--.-", "Ù": "..--",
    "Ü": "..--",
}
FR_FWD = _make_forward(_ENG_LATIN, _FR_EXTRAS)
FR_REV = _make_reverse(FR_FWD)

# 10. Deutsch (German)
_DE_EXTRAS = {
    "Ä": ".-.-", "Ö": "---.", "Ü": "..--", "ß": "...-..",
}
DE_FWD = _make_forward(_ENG_LATIN, _DE_EXTRAS)
DE_REV = _make_reverse(DE_FWD)

# 11. Italiano (Italian)
_IT_EXTRAS = {
    "À": ".--.-", "È": ".-..-", "É": "..-..", "Ì": "..-..",
    "Ò": "---.", "Ó": "---.", "Ù": "..--",
}
IT_FWD = _make_forward(_ENG_LATIN, _IT_EXTRAS)
IT_REV = _make_reverse(IT_FWD)

# 12. Türkçe (Turkish)
_TR_EXTRAS = {
    "Ç": "-.-..", "Ğ": "--.-.", "İ": "..-..", "Ö": "---.",
    "Ş": "...-...", "Ü": "..--",
}
TR_FWD = _make_forward(_ENG_LATIN, _TR_EXTRAS)
TR_REV = _make_reverse(TR_FWD)

# 13. Português (Portuguese)
_PT_EXTRAS = {
    "À": ".--.-", "Á": ".--.-", "Â": ".-.-", "Ã": ".-.-",
    "Ç": "-.-..", "É": "..-..", "Ê": "..-..", "Í": "..-..",
    "Ó": "---.", "Ô": "---.", "Õ": "---.", "Ú": "..--",
}
PT_FWD = _make_forward(_ENG_LATIN, _PT_EXTRAS)
PT_REV = _make_reverse(PT_FWD)

# 14. Українська (Ukrainian)
_UK_EXTRAS = {
    "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Ґ": "--.",
    "Д": "-..", "Е": ".", "Є": "..-..", "Ж": "...-", "З": "--..",
    "И": "-.--", "І": "..", "Ї": ".---.", "Й": ".---", "К": "-.-",
    "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
    "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.",
    "Х": "....", "Ц": "-.-.", "Ч": "---.", "Ш": "----", "Щ": "--.-",
    "Ь": "-..-", "Ю": "..--", "Я": ".-.-.",
}
UK_FWD = _make_forward({}, _UK_EXTRAS)
UK_REV = _make_reverse(UK_FWD)

# 15. Norsk (Norwegian)
_NO_EXTRAS = {
    "Æ": ".-.-", "Ø": "---.", "Å": ".--.-",
}
NO_FWD = _make_forward(_ENG_LATIN, _NO_EXTRAS)
NO_REV = _make_reverse(NO_FWD)


# ---------- Final dictionary ----------
LANG_MORSE_MAPS = {
    "English":    (ENG_FWD, ENG_REV),
    "Русский":    (RU_FWD, RU_REV),
    "Ελληνικά":   (GR_FWD, GR_REV),
    "العربية":    (AR_FWD, AR_REV),
    "עברית":      (HE_FWD, HE_REV),
    "日本語":      (JA_FWD, JA_REV),
    "Polski":     (PL_FWD, PL_REV),
    "Español":    (ES_FWD, ES_REV),
    "Français":   (FR_FWD, FR_REV),
    "Deutsch":    (DE_FWD, DE_REV),
    "Italiano":   (IT_FWD, IT_REV),
    "Türkçe":     (TR_FWD, TR_REV),
    "Português":  (PT_FWD, PT_REV),
    "Українська": (UK_FWD, UK_REV),
    "Norsk":      (NO_FWD, NO_REV),
}
