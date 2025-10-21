local_dir=xxx
target_dir=xxx

mkdir -p $target_dir
cp $local_dir/huggingface/added_tokens.json $target_dir
cp $local_dir/huggingface/tokenizer_config.json $target_dir
cp $local_dir/huggingface/vocab.json $target_dir
cp $local_dir/huggingface/special_tokens_map.json $target_dir
cp $local_dir/huggingface/tokenizer.json $target_dir
cp $local_dir/huggingface/merges.txt $target_dir

python scripts/model_merger.py \
--local_dir $local_dir \
--target_dir $target_dir