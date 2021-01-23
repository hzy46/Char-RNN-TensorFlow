rem WangZengQi
python train.py ^
  --use_embedding True ^
  --input_file data/ZhaoHuaXiShi.txt ^
  --num_steps 80 ^
  --name Zhaohuaxishi ^
  --learning_rate 0.005 ^
  --num_seqs 32 ^
  --num_layers 3 ^
  --embedding_size 256 ^
  --lstm_size 256 ^
  --max_steps 100000