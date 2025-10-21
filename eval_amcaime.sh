#!/bin/bash
MODEL_PATH=xxx
OUTPUT_DIR=xxx
mkdir -p "$OUTPUT_DIR"
echo "Evaluating $MODEL_PATH"

export CUDA_VISIBLE_DEVICES=0,1,2,3
python eval.py \
  --model_name="$MODEL_PATH" \
  --datasets="test_dataset/aime2025,test_dataset/amc23" \
  --split="test" \
  --output_dir="$OUTPUT_DIR" \
  --batch_size=1000 \
  --max_tokens=4096 \
  --num_gpus=4 \
  --temperature=0.6 \
  --top_p=0.95 \
  --think_mode normal \
  --num_generation=256 | grep -v "ANTLR"
