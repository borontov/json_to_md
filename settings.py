import os

dirname = os.path.dirname(__file__)

data_to_convert_path = "data/"
json_filename = "result"
json_extension = "json"
json_filename_full = f"{json_filename}.{json_extension}"

full_path_to_json = os.path.join(dirname, data_to_convert_path, json_filename_full)

output_filename_full = "output.md"
