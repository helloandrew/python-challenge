import csv

file_to_input = ("election_data.csv")
file_to_output = ("election_analysis.txt")

total_votes = 0
winning_vote = 0

#candidates list
candidate_names = []
candidate_votes = {}

with open(file_to_input) as election_data:
    election_data1 = csv.reader(election_data, delimiter = ",")
    header = next(election_data)
    for voter in election_data1:
        total_votes += 1
        if voter[2] not in candidate_names:
            candidate_names.append(voter[2])
            candidate_votes[voter[2]] = 0
            candidate_votes[voter[2]] += 1

        if voter[2] in candidate_names:
            candidate_votes[voter[2]] += 1
    output_1 = (f'\nElection Results\n'
    f'----------------------\n'
    f'Total Votes: {total_votes}'
    f'\n----------------------\n')
    print(output_1)
    
with open(file_to_output, "w") as file_txt:
    file_txt.write(output_1)
    for candidate in candidate_names:
        vote = candidate_votes.get(candidate)
        percent_vote = vote / total_votes * 100

        if vote > winning_vote:
            winning_vote = vote
            winning_candidate = candidate 
        output_2 = (f'{candidate}: {percent_vote:.3f}% ({vote})\n')
        file_txt.write(output_2)
        print(output_2)

    output_3 = (f'---------------------\n'
    f'Winner: {winning_candidate}\n'
    f'---------------------\n')
    print(output_3)
    file_txt.write(output_3)


        
        




