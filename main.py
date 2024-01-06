from calculate_strokes_gained import calculate_strokes_gained
from calculate_strokes_gained import data

def input_shot_data():
    distance = int(input("Enter the distance from the pin in yards: "))
    shot_surface = input("Enter the shot surface (tee, fairway, rough, sand, recovery, green): ")
    return distance, shot_surface

def process_hole_data(num_shots, hole_data, data):
    hole_total = 0
    for i in range(num_shots):
        distance, shot_surface = input_shot_data()

        strokes_gained_value = calculate_strokes_gained(distance, shot_surface, data)
        if strokes_gained_value is not None:
            strokes_gained_value = float(strokes_gained_value)

            if i == 0:
                strokes_gained_value -= 1
            else:
                strokes_gained_value -= float(hole_data[i - 1]['strokes_gained_value'])

            shot_data = {'distance': distance, 'surface': shot_surface, 'strokes_gained_value': strokes_gained_value}
            hole_data.append(shot_data)
            hole_total += strokes_gained_value
        else:
            print("Invalid input. Shot data not recorded.")

    return hole_total

def print_hole_data(hole, hole_data, hole_total):
    print(f"\nHole {hole}:")
    print(f"Hole Strokes Gained: {hole_total}")
    for item in hole_data:
        print(f"Distance: {item['distance']} yards, Surface: {item['surface']}, Strokes Gained Value: {item['strokes_gained_value']}")

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

        hole_total = process_hole_data(num_shots, hole_data, data)

        round_data.append(hole_data)
        hole_totals.append(hole_total)

        print_hole_data(hole, hole_data, hole_total)

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
