from trains import Task

task = Task.init('examples', 'upload_large_file', Task.TaskTypes.custom)

task.upload_artifact('example_large_file', "D:\projects\gndd\DB dump\dump-gndd_shp-202006080745.sql")
