export BERT_BASE_DIR=E:/GitHub/bert_lab
export DATA_DIR=E:/GitHub/bert_lab/data


python run_classifier.py \
  --task_name=case \
  --do_train=true \
  --do_eval=true \
  --data_dir=$DATA_DIR \
  --vocab_file=$BERT_BASE_DIR/model/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/model/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/model/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --output_dir=$BERT_BASE_DIR/tmp/






$env:BERT_BASE_DIR = "E:/GitHub/bert_lab/"
$env:DATA_DIR = "E:/GitHub/bert_lab/data/"

python run_classifier.py `
  --task_name=case `
  --do_train=true `
  --do_eval=false `
  --data_dir=$env:DATA_DIR `
  --vocab_file=$env:BERT_BASE_DIR/model/vocab.txt `
  --bert_config_file=$env:BERT_BASE_DIR/model/bert_config.json `
  --init_checkpoint=$env:BERT_BASE_DIR/model/bert_model.ckpt `
  --max_seq_length=128 `
  --train_batch_size=32 `
  --learning_rate=2e-5 `
  --num_train_epochs=3.0 `
  --output_dir=$env:BERT_BASE_DIR/tmp/



  python run_classifier.py `
  --task_name=case `
  --do_predict=true `
  --data_dir=$env:DATA_DIR `
  --vocab_file=$env:BERT_BASE_DIR/model/vocab.txt `
  --bert_config_file=$env:BERT_BASE_DIR/model/bert_config.json `
  --init_checkpoint=$env:BERT_BASE_DIR/tmp/ `
  --max_seq_length=128 `
  --output_dir=$env:BERT_BASE_DIR/tmp/output/