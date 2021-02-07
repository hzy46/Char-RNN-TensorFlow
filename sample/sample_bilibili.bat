cd ..
python sample.py --converter_path model/Bilibili/converter.pkl ^
  --checkpoint_path  model/Bilibili  ^
  --max_length 500  ^
  --use_embedding ^
  --num_layers 3 ^
  --start_string "我觉得"