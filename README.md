# Nagetive-Enhanced Group Relative Policy Optimization

## Installation
```shell
conda create -n verl python=3.10.15
conda activate verl
pip install vllm==0.8.5
pip install latex2sympy2==1.5.4
pip install fire==0.5.0
pip install tensordict==0.6.2
pip install flash-attn==2.7.0.post2 --no-isolation
```

## Training
```shell
bash train_scripts/train_qwen2.5-math-7b_ngrpo.sh
```

## Evaluation
For AIME2025 and AMC datasets,

```shell
bash eval_amcaime.sh
```

And for MATH dataset,

```shell
bash eval_math.sh
```

## Acknowledgement

This code is based on [verl](https://github.com/volcengine/verl) and [RLVR DECOMPOSED](https://github.com/TianHongZXY/RLVR-Decomposed).