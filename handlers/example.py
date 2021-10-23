import templates
from typing import Union, Dict, List
from dateutil import parser as date_parser


def telegram_exported_saved_messages(json_data: Union[Dict, List]):
    messages = json_data.get("messages")
    chunks_by_date = {}
    datetime_to_date_string = lambda date: date.strftime("%Y.%m.%d")
    for message in messages:
        message_date = date_parser.parse(message.get("date"))
        key = datetime_to_date_string(message_date)
        if key not in chunks_by_date:
            chunks_by_date[key] = list()
        chunks_by_date[key].append(message)
    messages_chunks_sorted_by_date = sorted(chunks_by_date.items(), key=lambda item: date_parser.parse(item[0]))
    fields = [
        "forwarded_from",
        "saved_from",
        "file",
        "title",
        "thumbnail",
        "media_type",
        "duration_seconds",
        "photo",
        "text",
    ]
    output = templates.example.render(
        messages_chunks_sorted_by_date=messages_chunks_sorted_by_date,
        fields=fields,
    )
    return output

