import random

segments = [ (random.randint(1, 8), random.randint(2, 9)) for _ in range(10) ]

def print_segments(segments):
    for segment in segments:
        print(f"({segment[0]}, {segment[1]})")

def initialize_segments():
    return [ (random.randint(1, 8), random.randint(2, 9)) for _ in range(10) ]

def main():
    segments = initialize_segments()

    print("Исходные отрезки:")
    print_segments(segments)

    segments.sort(key=lambda x: x[1])  # Сортировка по правому концу

    current_segment = segments[0]
    print(f"\nМинимальный отрезок: ({current_segment[0]}, {current_segment[1]})")

    for i in range(1, len(segments)):
        if segments[i][0] > current_segment[1]:
            current_segment = segments[i]
            print(f"({current_segment[0]}, {current_segment[1]})")

if __name__ == "__main__":
    main()