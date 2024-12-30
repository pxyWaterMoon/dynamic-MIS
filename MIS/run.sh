export PATH="/public/software/CUDA/cuda-12.1/bin:$PATH"
export LD_LIBRARY_PATH="/public/software/CUDA/cuda-12.1/lib64:$LD_LIBRARY_PATH"

python MIS/main.py --mode train --dataset_name TWITTER_SNAP