import argparse
import json
import numpy as np
from collections import defaultdict
from tqdm import tqdm


def unbiased_pass_at_k_accuracy(data, k, n):

    # Group predictions by question_id
    grouped_data = defaultdict(list)
    for example in data:
        question_id = example["question_id"]
        if len(grouped_data[question_id]) >= n:
            continue
        grouped_data[question_id].append(example)

    # Calculate unbiased pass@K accuracy
    total_pass_k_prob = 0
    total_questions = 0
    
    for question_id, examples in grouped_data.items():
        # Count correct and total solutions for this question
        assert len(examples) == n  # Total number of samples
        c = sum(1 for ex in examples if ex["label"])  # Number of correct samples
        # Apply unbiased pass@k formula
        assert n >= k
        # Calculate unbiased pass@k probability
        if n - c < k:
            prob = 1.0
        else:
            prob = 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
            
        total_pass_k_prob += prob
        total_questions += 1
    
    # Calculate average pass@K probability across all questions
    avg_pass_k = total_pass_k_prob / total_questions if total_questions > 0 else 0
    # print(f"Questions Number: {total_questions}, Unbiased Pass@{k}/{n}: {avg_pass_k}")
    return avg_pass_k


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", type=str, required=True, help="Path to the JSONLines file")
    parser.add_argument("--n", type=int, required=True, help="unbiased n")
    args = parser.parse_args()
   
    Ks = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    res = []
    print("reading data ...")

    # Read the JSONLines file
    data = []
    test_file = args.file_path
    with open(test_file, 'r') as f:
        for i, line in tqdm(enumerate(f)):
            data.append(json.loads(line.strip()))

    print(f"Calculating Unbiased Pass@K for {args.file_path}")
    for K in tqdm(Ks):
        if K > args.n:
            break
        # print("-" * 80)
        unbiased_pass_k_accuracy = unbiased_pass_at_k_accuracy(data, k=K, n=args.n)
        res.append(unbiased_pass_k_accuracy)
    final_score = 0
    for i, ress in enumerate(res):
        if i == 0 or i == len(res) - 1:
            final_score += ress
        else:
            final_score += 2*ress
    print("=" * 80)
    print(f"The final score is: {final_score/2/(len(res)-1)*100:.2f}")
    print("=" * 80)
    for i in range(len(res)):
        print(f"{res[i]*100:.2f}", end=" & ")
    print("\n")
