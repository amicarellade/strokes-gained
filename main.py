from calculate_strokes_gained import *

def main(data):
    num_holes = int(input("Enter the number of holes played (1 or 18): "))

    round_data = []  # To store data for each hole
    hole_totals = []  # To store hole-by-hole totals

    sg_categories = {
        'off-the-tee': 0,
        'approach-the-green': 0,
        'around-the-green': 0,
        'putting': 0,
        'tee-to-green': 0,
        'total': 0
    }

    for hole in range(1, num_holes + 1):
        print(f"\nHole {hole}")
        par = int(input("Enter the par for the hole: "))
        num_shots = int(input("Enter the number of shots taken: "))
        hole_data = []
        hole_total = 0  # To store hole-by-hole total strokes gained
        previous_strokes = None

        for shot in range(num_shots):
            distance = int(input("Enter the distance from the pin in yards: "))
            shot_surface = input("Enter the shot surface (tee, fairway, rough, sand, recovery, green): ")

            current_strokes = calculate_strokes_gained(distance, shot_surface, data)
            if current_strokes is not None:
                current_strokes = float(current_strokes)
                hole_data.append((distance, shot_surface, current_strokes))

                if previous_strokes is not None:
                    strokes_gained = (previous_strokes - current_strokes) - 1
                    hole_total += strokes_gained

                    # Categorize strokes gained
                    if shot == 0 and (par == 4 or par == 5):
                        sg_categories['off-the-tee'] += strokes_gained
                    elif shot_surface == 'green':
                        sg_categories['putting'] += strokes_gained
                    elif distance < 30:
                        sg_categories['around-the-green'] += strokes_gained
                    else:
                        sg_categories['approach-the-green'] += strokes_gained

                previous_strokes = current_strokes
            else:
                print("Invalid input. Shot data not recorded.")

        # Handle the final putt separately
        if len(hole_data) > 1:
            last_distance, last_surface, last_strokes = hole_data[-1]
            if last_surface == 'green':
                strokes_gained = last_strokes - 1
                hole_total += strokes_gained
                sg_categories['putting'] += strokes_gained
            elif last_distance > 30:
                strokes_gained = last_strokes - 1
                hole_total += strokes_gained
                sg_categories['approach-the-green'] += strokes_gained

        round_data.append(hole_data)
        hole_totals.append(hole_total)
        sg_categories['tee-to-green'] = sg_categories['off-the-tee'] + sg_categories['approach-the-green'] + sg_categories['around-the-green']
        sg_categories['total'] = sg_categories['tee-to-green'] + sg_categories['putting']

    print("\nStrokes Gained Totals by Category:")
    for category, total in sg_categories.items():
        print(f"{category.replace('-', ' ').capitalize()}: {round(total, 2)}")

    print("\nRunning Total Strokes Gained:")
    running_total = 0
    for total in hole_totals:
        running_total += total
        print(f"Hole {hole_totals.index(total) + 1}: {round(running_total, 2)}")

if __name__ == "__main__":
    main(data)
