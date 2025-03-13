# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidate_votes = {}  

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1
        
        # Get the candidate's name from the row
        Candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if Candidate not in Candidate_votes:
            Candidate_votes[Candidate] = 0

        # Add a vote to the candidate's count
        Candidate_votes[Candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nElection Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")

    # Write the total vote count to the text file

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

# Loop through the candidates to determine vote percentages and identify the winner
    
    for candidate, votes in Candidate_votes.items():
             
        # Get the vote count and calculate the percentage
        percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print(f"-------------------------")
    print(f"Winner: {winning_candidate}")
    print(f"-------------------------")

    # Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-------------------------\n")