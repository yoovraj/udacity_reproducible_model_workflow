# Udacity Exersizes

- exercise_1 : [upload artifact module](./exercise_1/upload_artifact.py)  
`
python upload_artifact.py --input_file zen.txt 
--artifact_name zen_of_python
--artifact_type text_file
--artifact_description "20 aphorisms about writing good python code"
`

# environment setup
```
conda create --name udacity python=3.8 mlflow jupyter pandas matplotlib requests -c conda-forge
pip install -r requirements.txt
autopep8 --in-place --aggressive --aggressive  upload_artifact.py
```


