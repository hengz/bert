$env:BERT_BASE_DIR = "E:/GitHub/bert_lab/"
$env:DATA_DIR = "E:/GitHub/bert_lab/data/"

python run_classifier.py `
  --task_name=case `
  --do_predict=true `
  --data_dir=$env:DATA_DIR `
  --vocab_file=$env:BERT_BASE_DIR/model/vocab.txt `
  --bert_config_file=$env:BERT_BASE_DIR/model/bert_config.json `
  --init_checkpoint=$env:BERT_BASE_DIR/tmp/ `
  --max_seq_length=128 `
  --output_dir=$env:BERT_BASE_DIR/tmp/output/