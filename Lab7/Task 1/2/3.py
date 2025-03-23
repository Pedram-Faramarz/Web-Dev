def find_runner_up_score():
    n = int(input().strip())  # Read the number of scores (not actually used)
    scores = list(map(int, input().split()))  # Read scores and convert to list of integers
    
    unique_scores = list(set(scores))  # Remove duplicates
    unique_scores.sort(reverse=True)  # Sort in descending order
    
    print(unique_scores[1])  # The second highest score is at index 1

# Call the function
find_runner_up_score()
