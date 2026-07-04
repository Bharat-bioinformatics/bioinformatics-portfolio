def analyze_sequence(sequence):
    print("Length:", len(sequence))
    print("A:", sequence.count("A"))
    print("T:", sequence.count("T"))
    print("G:", sequence.count("G"))
    print("C:", sequence.count("C"))
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100
    print("GC content:", gc_percentage, "%")
    unexpected = 0
    for letter in sequence:
        if letter != "A" and letter != "T" and letter != "G" and letter != "C":
            unexpected += 1
    print("Unexpected:", unexpected)
    print("Total valid:", len(sequence) - unexpected)
    print("Reverse:", sequence[::-1])
    print("---")

# Example usage
analyze_sequence("ATGCNTGACN")
