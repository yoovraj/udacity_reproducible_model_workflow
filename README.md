# Udacity Exersizes

- exercise_1 : [upload artifact module](./exercise_1/upload_artifact.py)  
```
python upload_artifact.py --input_file zen.txt 
--artifact_name zen_of_python
--artifact_type text_file
--artifact_description "20 aphorisms about writing good python code"
```

- exercise_2:  
```
mlflow run . -P file_url=https://raw.githubusercontent.com/scikit-learn/scikit-learn/4dfdfb4e1bb3719628753a4ece995a1b2fa5312a/sklearn/datasets/data/iris.csv -P artifact_name=iris -P artifact_description="This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length"
```

- exercise_3:  
```
mlflow run .  

mlflow run . -P hydra_options="main.experiment_name=prod"
```

- exercise_4:  
```
wandb artifact put \
      --name genres_mod.parquet \
      --type raw_data \
      --description "A modified version of the songs dataset" genres_mod.parquet

mlflow run . 
## Need to enable extension in jupyter lab
```

- exercise_5:  
```
mlflow run . -P input_artifact="exercise_4/genres_mod.parquet:latest" \
             -P artifact_name="preprocessed_data.csv" \
             -P artifact_type="text_file" \
             -P artifact_description="processed data file along with new feature addition"

wandb artifact get exercise_5/preprocessed_data.csv
```

- exersize_6:  
```
mlflow run . -P input_artifact="exercise_5/preprocessed_data.csv:latest" \
             -P artifact_root="data" \
             -P test_size=0.3 \
             -P stratify="genre"

wandb artifact get exercise_6/data_train.csv
wandb artifact get exercise_6/data_test.csv
---
wc -l  artifacts/data_train.csv:v0/data_train.csv
wc -l  artifacts/data_test.csv:v0/data_test.csv
wc -l  artifacts/preprocessed_data.csv:v0/preprocessed_data.csv
---

```
# environment setup
```
conda create --name udacity python=3.8 mlflow jupyter pandas matplotlib requests -c conda-forge
pip install -r requirements.txt
autopep8 --in-place --aggressive --aggressive  upload_artifact.py
```


