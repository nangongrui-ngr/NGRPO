res_path=xxx
max_n=256

python calculate_metrics.py \
--file_path $res_path/aime2025-test-temp_0.6-top_p_0.95-top_k_-1.jsonl \
--n $max_n

python calculate_metrics.py \
--file_path $res_path/amc23-test-temp_0.6-top_p_0.95-top_k_-1.jsonl \
--n $max_n

python calculate_metrics.py \
--file_path $res_path/math-test-temp_0.6-top_p_0.95-top_k_-1.jsonl \
--n $max_n