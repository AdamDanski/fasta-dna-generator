# Numer albumu: s30656
# Data: 07.05.2026
#Opis Generator losowych sekwencji DNA zapisanych w formacie FASTA

import random


def generate_sequence(length: int) -> str:
    """Zwraca losową sekwencję DNA o danej długości"""

    nucleotides = ["A", "C", "G", "T"]
    sequence = ""

    for _ in range(length):
        sequence += random.choice(nucleotides)

    return sequence


def calculate_stats(sequence: str) -> dict:
    """Zwraca statysytke procentowa nukleortydow i GC-content."""

    length = len(sequence)
    count_a = sequence.count("A")
    count_c = sequence.count("C")
    count_g = sequence.count("G")
    count_t = sequence.count("T")

    a_percent = (count_a / length) * 100
    c_percent = (count_c / length) * 100
    g_percent = (count_g / length) * 100
    t_percent = (count_t / length) * 100

    gc_content = ((count_g + count_c) / length) * 100

    return {
        "A": a_percent,
        "C": c_percent,
        "G": g_percent,
        "T": t_percent,
        "GC": gc_content
    }


def insert_name(sequence: str, name: str) -> str:
    """wstawia imię w losową pozycję sekwencji"""

    position = random.randint(0, len(sequence))

    name = name.lower()

    new_sequence = sequence[:position] + name + sequence[position:]

    return new_sequence


def format_fasta(seq_id: str, description: str, sequence: str, line_width: int = 80) -> str:
    """Zwraca sformatowany rekord FASTA jako tekst."""
    pass


def validate_positive_int(prompt: str, min_val: int = 1, max_val: int = 100_000) -> int:
    """Pobiera od użytkownika liczbę całkowitą i sprawdza czy miesi sie w danym przedziale"""

    while True:
        value = input(prompt)
        try:
            number = int(value)

            if min_val <= number <= max_val:
                return number

            print(f"Błąd: wartość musi być liczbą całkowitą z zakresu [{min_val}, {max_val}].")

        except ValueError:
            print(f"Błąd: wartość musi być liczbą całkowitą z zakresu [{min_val}, {max_val}].")


def main():
    """Cytując "Wiadomo." po prostu main"""

    length = validate_positive_int("Podaj długość sekwencji: ")

    seq_id = input("Podaj ID sekwencji: ")

    while " " in seq_id:
        print("ID nie może zawierać spacji.")
        seq_id = input("Podaj ID sekwencji: ")

    description = input("Podaj opis sekwencji: ")

    name = input("Podaj imię: ")

    sequence = generate_sequence(length)
    sequence_with_name = insert_name(sequence, name)
    stats = calculate_stats(sequence)

    print(sequence_with_name+"\n")
    print("Statystyki sekwencji:")

    print(f"A: {stats['A']:.2f}%")
    print(f"C: {stats['C']:.2f}%")
    print(f"G: {stats['G']:.2f}%")
    print(f"T: {stats['T']:.2f}%")
    print(f"GC-content: {stats['GC']:.2f}%")

if __name__ == "__main__":
    main()