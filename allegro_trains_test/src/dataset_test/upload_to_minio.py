import os

from trains import Task
import pandas as pd
from PIL import Image

task = Task.init(
  project_name='examples', 
  task_name='upload_to_minio', 
  # task_type=Task.TaskTypes.custom,
  output_uri='s3://localhost:9000/test-data'
  )

task.upload_artifact('example_large_file', "./artifacts.py")

df = pd.DataFrame(
    {
        'num_legs': [2, 4, 8, 0],
        'num_wings': [2, 0, 0, 0],
        # 'num_specimen_seen': [10, 2, 1, 8]
    },
    index=['falcon', 'dog', 'spider', 'fish']
)

task.upload_artifact('Pandas', artifact_object=df)
task.upload_artifact('dictionary', df.to_dict())

im = Image.open(os.path.join('data_samples', 'dancing.jpg'))
task.upload_artifact('pillow_image', im)

task.upload_artifact('local folder', artifact_object=os.path.join('data_samples'))