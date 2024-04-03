def select_eye():
    # Ask the user to select an eye, with "right" as the default
    choice = input("Please select an eye to process (left/right). Default is right: ").lower().strip()
    
    # Return the corresponding slice based on the user's input
    # Default to the right eye if the input is unrecognized
    if choice == "left":
        return (slice(300, 800), slice(300, 1100)), "Left"
    else:
        # Default to right eye
        return (slice(300, 800), slice(700, 1500)), "Right"

def saccade_detection(coordinates):
    
    regular = 0
    irregular = 0

    # Loop through the coordinates starting at 132 and checking every 282 points
    for i in range(131, len(coordinates), 282):

        change_within_9 = False
        
        # Check if there are at least 9 points after the current index
        if i + 9 < len(coordinates):
            # Check the next 9 points for any change
            for j in range(i+1, i+10):
                if coordinates[i] != coordinates[j]:
                    change_within_9 = True
                    break  # Stop checking further if a change is found within 9 points

            # Update counters based on whether a change was found within 9 points
            if change_within_9:
                regular += 1
            else:
                irregular += 1

    return regular, irregular


