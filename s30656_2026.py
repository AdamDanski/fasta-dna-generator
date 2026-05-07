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

def get_complementary_sequence(sequence: str) -> str:
    """Zwraca sekwencję komplementarną DNA"""

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    new_sequence = ""

    for nucleotide in sequence:
        new_sequence += complement[nucleotide]

    return new_sequence

def get_reverse_complement(sequence: str) -> str:
    """Zwraca odwrotnie komplementarną sekwencję DNA"""

    complementary = get_complementary_sequence(sequence)

    reverse_complement = complementary[::-1]

    return reverse_complement

def insert_name(sequence: str, name: str) -> str:
    """wstawia imię w losową pozycję sekwencji"""

    position = random.randint(0, len(sequence))

    name = name.lower()

    new_sequence = sequence[:position] + name + sequence[position:]

    return new_sequence


def format_fasta(seq_id: str, description: str, sequence: str, line_width: int = 80) -> str:
    """Zwraca sformatowany rekord FASTA w formie tekstu"""

    if description == "":
        fasta_text = ">" + seq_id + "\n"
    else:
        fasta_text = ">" + seq_id + " " + description + "\n"

    for i in range(0, len(sequence), line_width):
        line = sequence[i:i + line_width]
        fasta_text += line + "\n"

    return fasta_text

def transcribe_to_mrna(sequence: str) -> str:
    """Zwraca sekwencję mRNA na podstawie nmaszego DNA"""

    mrna = sequence.replace("T", "U")

    return mrna

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


def find_motif(sequence: str, motif: str) -> list:
    """Zwraca pozycje wystąpień motywu w sekwencji. Pozycje liczone są od 1."""

    positions = []

    motif = motif.upper()

    for i in range(len(sequence) - len(motif) + 1):
        fragment = sequence[i:i + len(motif)]

        if fragment == motif:
            positions.append(i + 1)

    return positions

def main():
    """Cytując "Wiadomo." po prostu main"""

    length = validate_positive_int("Podaj długość sekwencji: ")

    seq_id = input("Podaj ID sekwencji: ")

    while " " in seq_id:
        print("ID nie może zawierać spacji.")
        seq_id = input("Podaj ID sekwencji: ")

    description = input("Podaj opis sekwencji: ")

    name = input("Podaj imię: ")

    motif = input("Podaj motyw do wyszukania, np. ATG: ")

    sequence = generate_sequence(length)
    sequence_with_name = insert_name(sequence, name)
    stats = calculate_stats(sequence)

    complementary_sequence = get_complementary_sequence(sequence)

    reverse_complement = get_reverse_complement(sequence)
    mrna_sequence = transcribe_to_mrna(sequence)
    motif_positions = find_motif(sequence, motif)



    print()
    print("Sekwencja komplementarna:")
    print(complementary_sequence)

    print()
    print("Sekwencja odwrotnie komplementarna:")
    print(reverse_complement)

    print()
    print("Sekwencja mRNA:")
    print(mrna_sequence)

    fasta_text = format_fasta(seq_id, description, sequence_with_name)

    fasta_text += format_fasta(
        seq_id + "_complement",
        "Sekwencja komplementarna",
        complementary_sequence
    )

    fasta_text += format_fasta(
        seq_id + "_reverse_complement",
        "Sekwencja odwrotnie komplementarna",
        reverse_complement
    )

    fasta_text += format_fasta(
        seq_id + "_mRNA",
        "Sekwencja mRNA",
        mrna_sequence
    )

    file_name = seq_id + ".fasta"

    with open(file_name, "w") as file:
        file.write(fasta_text)

    print()
    print("Sekwencja zapisana do pliku: " + file_name)

    print()
    print(f"Statystyki sekwencji (n={length}):")
    print(f"  A: {stats['A']:.2f}%")
    print(f"  C: {stats['C']:.2f}%")
    print(f"  G: {stats['G']:.2f}%")
    print(f"  T: {stats['T']:.2f}%")
    print(f"  GC-content: {stats['GC']:.2f}%")

    print()
    print("Pozycje motywu " + motif.upper() + ":")

    if len(motif_positions) == 0:
        print("Brak wystąpień.")
    else:
        print(motif_positions)

if __name__ == "__main__":
    main()