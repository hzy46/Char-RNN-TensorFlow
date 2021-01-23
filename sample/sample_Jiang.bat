cd ..
python sample.py --converter_path model/ElderJiang/converter.pkl ^
  --checkpoint_path  model/ElderJiang  ^
  --max_length 500  ^
  --use_embedding ^
  --num_layers 3 ^
  --start_string "sometimes na"