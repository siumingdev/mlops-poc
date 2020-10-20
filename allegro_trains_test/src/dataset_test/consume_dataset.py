from trains import Task
from trains import Task, StorageManager
import pandas as pd


task = Task.init(project_name="examples", task_name="consume dataset test")

dataset_upload_task: Task = Task.get_task(project_name="examples", task_name="upload_large_file")
# dataset_upload_task: Task = Task.get_task(task_id="f780976d8d624041b4b84dc83def506f")

print(dataset_upload_task.artifacts['example_large_file'].get_local_copy())
with open(dataset_upload_task.artifacts['example_large_file'].get_local_copy(), "r") as fh:
    i = 10
    for line in fh:
        print(line)
        i -= 1
        if i <= 0:
            break
