import xml.dom.minidom # DOM for parsing CubeData.xml Data
import matplotlib.pyplot as plt # For Data Visualization in Options 3 - 5
import numpy as np # For Data Visualization in Options 3 - 5

file_path = "CubeData.xml"

print("========================================")
print("====== Rubik's Cube Data Analyzer ======")
print("========================================")
print("====== By Ian Brabbs (11/12/2023) ======")
print("========================================\n")

def option1():
    print("\nOption 1 Selected")
    print("\nView Solve Info Via Solve ID")
    print("==================================")
    
    def display_solve_info(solve_node):
        solve_number = solve_node.getElementsByTagName("ID")[0].childNodes[0].data
        solve_time = solve_node.getElementsByTagName("Time")[0].childNodes[0].data
        solve_scramble = solve_node.getElementsByTagName("Scramble")[0].childNodes[0].data
        solve_date = solve_node.getElementsByTagName("Date")[0].childNodes[0].data

        print(f"\nSolve ID: {solve_number}")
        print(f"Time: {solve_time}")
        print(f"Scramble: {solve_scramble}")
        print(f"Date: {solve_date}\n")

    def main():
        # Parse CubeData.xml and extract the solves.
        doc = xml.dom.minidom.parse(file_path)
    
        # Get all of the solve elements from CubeData.xml
        solve_elements = doc.getElementsByTagName("solve")

        # Ask the user to input a Solve ID.
        solve_number_input = input("Enter a Solve ID (1 - 6244): ")

        # Find the solve element with the specified solve number.
        for solve_element in solve_elements:
            solve_number = solve_element.getElementsByTagName("ID")[0].childNodes[0].data
            if solve_number == solve_number_input:
                display_solve_info(solve_element)
                break
        else:
            print(f"\nNo solve found with Solve ID {solve_number_input}.\n")

    if __name__ == "__main__":
        main()

def option2():
    print("\nOption 2 Selected")
    print("\nView Solve Info Via Time")
    print("===============================")

    def display_solve_info(solve_node):
        solve_number = solve_node.getElementsByTagName("ID")[0].childNodes[0].data
        solve_time = solve_node.getElementsByTagName("Time")[0].childNodes[0].data
        solve_scramble = solve_node.getElementsByTagName("Scramble")[0].childNodes[0].data
        solve_date = solve_node.getElementsByTagName("Date")[0].childNodes[0].data

        print(f"\nSolve ID: {solve_number}")
        print(f"Time: {solve_time}")
        print(f"Scramble: {solve_scramble}")
        print(f"Date: {solve_date}\n")

    def main():
        # Parse CubeData.xml and extract the solves.
        doc = xml.dom.minidom.parse(file_path)
    
        # Get all of the solve elements from CubeData.xml
        solve_elements = doc.getElementsByTagName("solve")

        # Ask the user for a time.
        solve_time_input = input("Enter a time (ex. 12.88): ")

        # Find the time element with the specified time.
        for solve_element in solve_elements:
            solve_time = solve_element.getElementsByTagName("Time")[0].childNodes[0].data
            if solve_time == solve_time_input:
                display_solve_info(solve_element)
                break
        else:
            print(f"\nNo solve found with a time of {solve_time_input}.\n")

    if __name__ == "__main__":
        main()

def option3():
    print("\nOption 3 Selected")
    print("\nView Overall Information")
    print("=============================")
    # Parse CubeData.xml and extract the solves.
    doc = xml.dom.minidom.parse(file_path)

    # Get all of the solve elements from CubeData.xml
    solves = doc.getElementsByTagName("solve")

    # Initialize variables for total time, number of solves, slowest time and fastest time.
    total_time = 0
    num_solves = 0
    slowest_time = float('-inf')  # Negative infinity to ensure the first time will be greater.
    fastest_time = float('inf')  # Positive infinity to ensure the first time will be smaller.

    # Lists to store solve times for visualizing.
    solve_times = []

    # Iterate for every solve.
    for solve in solves:
        # Extract the time from the Time element of each solve.
        time_element = solve.getElementsByTagName("Time")[0]
        time = float(time_element.firstChild.nodeValue)

        # Update the total time, number of solves, and check for the slowest and fastest times.
        total_time += time
        num_solves += 1
        solve_times.append(time)
        if time > slowest_time:
            slowest_time = time
        if time < fastest_time:
            fastest_time = time

    # Calculate the average time and calculate the total time across all solves.
    average_time = total_time / num_solves
    total_time_hours = total_time / 60 / 60

    # Display information.
    print("Total Amount of Solves:", num_solves)
    print("Total Solve Time: {:.2f} Hours".format(total_time_hours))
    print("Average Time: {:.2f}".format(average_time))
    print("Slowest Time: {:.2f}".format(slowest_time))
    print("Fastest Time: {:.2f}\n".format(fastest_time))

    # Plot the bar graph.
    plt.bar(range(1, num_solves + 1), solve_times, color='blue')
    plt.xlabel('Solve ID')
    plt.ylabel('Time (seconds)')
    plt.title('Solve Times')
    plt.yticks(np.arange(10, 50, 5), minor=False)
    plt.yticks(np.arange(10, 50, 1), minor=True)
    plt.ylim(10, 50)
    plt.show()

def option4():
    print("\nYou selected Option 4")
    print("\nView Start VS. End Information")
    print("=======================================")
    # Parse CubeData.xml and extract the solves.
    doc = xml.dom.minidom.parse(file_path)

    # Get all of the solve elements from CubeData.xml
    solves = doc.getElementsByTagName("solve")

    # Initialize variables for total time, number of solves, slowest time and fastest time.
    total_time_first_500 = 0
    total_time_last_500 = 0
    num_solves_first_500 = 0
    num_solves_last_500 = 0
    fastest_time_first_500 = float('inf') # Positive infinity to ensure the first time will be smaller.
    slowest_time_first_500 = float('-inf') # Negative infinity to ensure the first time will be greater.
    fastest_time_last_500 = float('inf') # Positive infinity to ensure the first time will be smaller.
    slowest_time_last_500 = float('-inf') # Negative infinity to ensure the first time will be greater.

    # Iterate for every solve.
    for i, solve in enumerate(solves):
        # Extract the time from the Time element of each solve.
        time_element = solve.getElementsByTagName("Time")[0]
        time = float(time_element.firstChild.nodeValue)
    
        # Check to see if the solve is in the first 500 solves or last 500 solves.
        if i < 500:
            total_time_first_500 += time
            num_solves_first_500 += 1
            if time < fastest_time_first_500:
                fastest_time_first_500 = time
            if time > slowest_time_first_500:
                slowest_time_first_500 = time
        elif i >= len(solves) - 500:
            total_time_last_500 += time
            num_solves_last_500 += 1
            if time < fastest_time_last_500:
                fastest_time_last_500 = time
            if time > slowest_time_last_500:
                slowest_time_last_500 = time

    # Calculating the average time for each range
    avg_time_first_500 = total_time_first_500 / num_solves_first_500 if num_solves_first_500 > 0 else 0
    avg_time_last_500 = total_time_last_500 / num_solves_last_500 if num_solves_last_500 > 0 else 0

    # Data for the bar graph.
    categories = ['First 500 Solves', 'Last 500 Solves']
    total_times = [total_time_first_500, total_time_last_500]
    avg_times = [avg_time_first_500, avg_time_last_500]
    fastest_times = [fastest_time_first_500, fastest_time_last_500]
    slowest_times = [slowest_time_first_500, slowest_time_last_500]

    # Plotting the bar graph.
    bar_width = 0.3
    index = range(len(categories))

    # Configuring the bars so that they fit the bar graph appropriately.
    fig, ax = plt.subplots()
    bar1 = ax.bar([i + bar_width for i in index], avg_times, bar_width, label='Average Time')
    bar2 = ax.bar([i + 2 * bar_width for i in index], fastest_times, bar_width, label='Fastest Time')
    bar3 = ax.bar([i + 3 * bar_width for i in index], slowest_times, bar_width, label='Slowest Time')

    # Labels, title and minor/major ticks.
    ax.set_xlabel('Solve Sets')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('First 500 Solves VS. Last 500 Solves')
    ax.set_xticks([i + 1.5 * bar_width for i in index])
    ax.set_xticklabels(categories)
    ax.legend()
    plt.yticks(np.arange(0, 50, 5), minor=False)
    plt.yticks(np.arange(0, 50, 1), minor=True)

    # Display information.
    print("Average Time (First 500 solves): {:.2f}".format(avg_time_first_500))
    print("Fastest Time (First 500 solves):", fastest_time_first_500)
    print("Slowest Time (First 500 solves):", slowest_time_first_500)

    print("\nAverage Time (Last 500 solves): {:.2f}".format(avg_time_last_500))
    print("Fastest Time (Last 500 solves):", fastest_time_last_500)
    print("Slowest Time (Last 500 solves):", slowest_time_last_500)
    print("")

    plt.show()

def option5():
    print("\nOption 5 Selected")
    print("\nView Solve Range Information")
    print("==========================================")
    # Parse CubeData.xml and extract the solves.
    def parse_cube_data(xml_string):
        dom = xml.dom.minidom.parseString(xml_string)
        solves = dom.getElementsByTagName("solve")
        return solves

    # Calculate the percentage of solves within a certain time range.
    def calculate_percentage_in_range(solves, time_range_start, time_range_end):
        total_solves = len(solves)
        solves_in_range = 0

        for solve in solves:
            # Extract the time element from each solve.
            time_element = solve.getElementsByTagName("Time")[0]
            # Convert the time into a float.
            solve_time = float(time_element.firstChild.data)

            if time_range_start <= solve_time <= time_range_end:
                solves_in_range += 1

        # Calculate the percentage of solves within a certain time range.
        percentage = (solves_in_range / total_solves) * 100
        return percentage

    if __name__ == "__main__":
        with open(file_path, "r") as file:
            cube_data_xml = file.read()

        solves = parse_cube_data(cube_data_xml)

        # Define the time ranges.
        time_ranges = [(10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50,), (50, 55)]

        # Calculate and print the percentages for each time range.
        percentages = []
        for time_range_start, time_range_end in time_ranges:
            percentage = calculate_percentage_in_range(solves, time_range_start, time_range_end)
            percentages.append(percentage)
            print(f"Solves between {time_range_start} and {time_range_end} seconds: {percentage:.3f}%")
        print("")

        custom_colors = ['cyan', 'purple', 'green', 'red', 'orange', 'yellow', 'blue', 'pink', 'brown']

        # Plot the bar graph.
        x_labels = [f"{start}-{end} s" for start, end in time_ranges]
        x_pos = np.arange(len(x_labels))
        plt.bar(x_pos, percentages, align='center', alpha=0.7, color=custom_colors)
        plt.xticks(x_pos, x_labels, rotation='vertical')
        plt.yticks(np.arange(0, 35, 5), minor=False)
        plt.yticks(np.arange(0, 35, 1), minor=True)

        plt.ylabel('Percentage')
        plt.title('Percentage of Solves in Each Time Range')
        
        plt.show()

while True:
    print("             Main Menu             ")
    print("===================================")
    print("1. View Solve Info Via Solve ID")
    print("2. View Solve Info Via Time")
    print("3. View Overall Information")
    print("4. View Start VS. End Information")
    print("5. View Solve Range Information")
    print("6. Exit")
    print("-----------------------------------")

    choice = input("Choose an Option (1-6): ")

    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        option4()
    elif choice == '5':
        option5()
    elif choice == '6':
        print("\nOption 6 Selected")
        print("\nExiting the program. Goodbye!\n")
        break
    else:
        print("\nSorry, that is an invalid choice. Please enter a number between 1 and 6.\n")