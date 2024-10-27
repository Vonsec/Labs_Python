from collections import Counter, OrderedDict
from typing import Dict

# TODO  Напишите функцию count_letters
def count_letters(text: str) -> Dict[str, int]:
    letters = (char.lower() for char in text if char.isalpha())
    counts = Counter(letters)
    ordered_counts = OrderedDict()
    for char in text.lower():
        if char.isalpha() and char not in ordered_counts:
            ordered_counts[char] = counts[char]
    return ordered_counts


# TODO Напишите функцию calculate_frequency
def calculate_frequency(counts: Dict[str, int]) -> Dict[str, float]:
    total = sum(counts.values())
    if total == 0:
        return {}
    return {letter: count / total for letter, count in counts.items()}


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

counts = count_letters(main_str)
frequencies = calculate_frequency(counts)
for letter, count in counts.items():
    freq = frequencies.get(letter, 0)
    if freq > 0:
        print(f"{letter}: {freq:.2f}")
