# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"C:\Users\fjrui\OneDrive\Documents\Desktop\Bootcamp\Assignment\module3\Starter_Code\PyPoll\Resources\election_data.csv")  # Input file path
file_to_output = os.path.join(r"C:\Users\fjrui\OneDrive\Documents\Desktop\Bootcamp\Assignment\module3\Starter_Code\PyPoll\analysis\election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists to track candidate names and vote counts
candidates = []
number_votes = []
percent_votes = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            number_votes.append(1)  # Start tracking the vote count for this candidate
        else:
            # Add a vote to the candidate's count
            index = candidates.index(candidate_name)
            number_votes[index] += 1

# Calculate vote percentages for each candidate
for votes in number_votes:
    percentage = (votes / total_votes) * 100
    percent_votes.append(round(percentage, 2))  # Round to 2 decimal places

# Determine the winner based on the highest vote count
for i in range(len(candidates)):
    if number_votes[i] > winning_votes:
        winning_votes = number_votes[i]
        winning_candidate = candidates[i]

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal and file)
    election_header = (
        "Election Results\n"
        "--------------------------\n"
        f"Total Votes: {total_votes}\n"
        "--------------------------\n"
    )
    print(election_header)
    txt_file.write(election_header)

    # Loop through the candidates to print and save each candidate's vote count and percentage
    for i in range(len(candidates)):
        candidate_results = (
            f"{candidates[i]}: {percent_votes[i]}% ({number_votes[i]})\n"
        )
        print(candidate_results)
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winner_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        "--------------------------\n"
    )
    print(winner_summary)
    txt_file.write(winner_summary)
