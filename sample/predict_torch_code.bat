cd ..
python predict.py ^
  --converter_path model/torch_gen/converter.pkl ^
  --checkpoint_path  model/torch_gen ^
  --max_length 1500 ^
  --start_string "    def "