import json
import settings
import handlers

with open(settings.full_path_to_json) as json_file:
    json_data = json.load(json_file)
    output = handlers.example.telegram_exported_saved_messages(
        json_data=json_data
    )
    with open(settings.output_filename_full, "w") as file:
        file.write(output)


