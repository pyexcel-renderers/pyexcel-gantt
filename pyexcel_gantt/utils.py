import re
import os
import sys
import json
from datetime import date, datetime

PY2 = sys.version_info[0] == 2
JS_PATTERN = re.compile(r'<!-- build -->(.*)<!-- endbuild -->',
                        re.IGNORECASE | re.MULTILINE | re.DOTALL)
JS_SRC_PATTERN = re.compile(r'src=\"(.*?)\"')


def freeze_js(html_content):
    matches = JS_PATTERN.finditer(html_content)

    if not matches:
        return html_content

    for match in reversed(tuple(matches)):
        # JS file block
        src_matches = JS_SRC_PATTERN.findall(match.group(1))

        js_content = ""
        for src in reversed(src_matches):
            file_path = os.path.join(get_resource_dir('templates'), src)

            with open(file_path, "r") as f:
                js_content += f.read() + '\n'
        # Replace matched string with inline JS
        fmt = '<script type="text/javascript">{}</script>'
        js_content = fmt.format(js_content)
        html_content = (html_content[:match.start()] + js_content +
                        html_content[match.end():])

    return html_content


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            date_string = obj.strftime('%Y-%m-%d')
            return date_string
        if isinstance(obj, datetime):
            datetime_string = obj.strftime("%Y-%m-%d")
            return datetime_string
        return json.JSONEncoder.default(self, obj)


def dumps(data):
    return json.dumps(data, cls=DateTimeEncoder)
