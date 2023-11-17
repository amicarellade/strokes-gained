# Strokes Gained 

from calculate_strokes_gained import *

def main(data):
    num_holes = int(input("Enter the number of holes played (9 or 18): "))
    if num_holes not in [2, 18]:
        print("Invalid number of holes. Please enter 9 or 18.")
        return

    round_data = []  # To store data for each hole
    hole_totals = []  # To store hole-by-hole totals
    surface_totals = {'tee': 0, 'fairway': 0, 'rough': 0, 'sand': 0, 'recovery': 0, 'green': 0}  # To store surface-by-surface totals

    for hole in range(1, num_holes + 1):
        print(f"\nHole {hole}")
        num_shots = int(input("Enter the number of shots taken: "))
        hole_data = []
        hole_total = 0  # To store hole-by-hole total strokes gained

        for _ in range(num_shots):
            distance = int(input("Enter the distance from the pin in yards: "))
            shot_surface = input("Enter the shot surface (tee, fairway, rough, sand, recovery, green): ")

            strokes_gained = calculate_strokes_gained(distance, shot_surface, data)
            if strokes_gained is not None:
                strokes_gained = float(strokes_gained) 
                hole_data.append((distance, shot_surface, strokes_gained))
                hole_total += strokes_gained  # Update hole total strokes gained
                surface_totals[shot_surface] += strokes_gained  # Update surface totals
            else:
                print("Invalid input. Shot data not recorded.")

        round_data.append(hole_data)
        hole_totals.append(hole_total)

    print("\nStrokes Gained Data for the Round:")
    for hole, data in enumerate(round_data, start=1):
        print(f"\nHole {hole}:")
        total_strokes_gained = hole_totals[hole - 1]
        print(f"Hole Strokes Gained: {total_strokes_gained}")
        for item in data:
            print(f"Distance: {item[0]} yards, Surface: {item[1]}, Strokes Gained: {item[2]}")

    print("\nSurface-by-Surface Strokes Gained Totals:")
    for surface, total in surface_totals.items():
        print(f"{surface.capitalize()}: {total}")

    print("\nRunning Total Strokes Gained:")
    running_total = 0
    for total in hole_totals:
        running_total += total
        print(f"Hole {hole_totals.index(total) + 1}: {running_total}")

if __name__ == "__main__":
    main(data)
