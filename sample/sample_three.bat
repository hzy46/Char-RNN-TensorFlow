python sample.py ^
  --converter_path model/novel/converter.pkl ^
  --checkpoint_path  model/novel ^
  --use_embedding ^
  --max_length 2000 ^
  --num_layers 3 ^
  --lstm_size 256 ^
  --embedding_size 256 
  --start_string "其实"