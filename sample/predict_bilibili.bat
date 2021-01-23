cd ..
python predict.py --converter_path model/Bilibili/converter.pkl ^
  --checkpoint_path  model/Bilibili  ^
  --max_length 500  ^
  --use_embedding ^
  --num_layers 3 ^
  --start_string "¸Ä¸ï´º·ç"