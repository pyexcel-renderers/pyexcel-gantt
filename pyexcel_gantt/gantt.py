import re
import os
import sys
import json
from datetime import date, datetime

from pyexcel.renderer import Renderer
from jinja2 import Environment, FileSystemLoader


PY2 = sys.version_info[0] == 2
js_pattern = re.compile(r'<!-- build -->(.*)<!-- endbuild -->',
                        re.IGNORECASE | re.MULTILINE | re.DOTALL)
js_src_pattern = re.compile(r'src=\"(.*?)\"')


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            date_string = obj.strftime('%Y-%m-%d')
            return date_string
        if isinstance(obj, datetime):
            datetime_string = obj.strftime("%Y-%m-%d")
            return datetime_string
        return json.JSONEncoder.default(self, obj)


def _dumps(data):
    return json.dumps(data, cls=DateTimeEncoder)


class Chart(Renderer):
    def __init__(self, file_type):
        Renderer.__init__(self, file_type)
        loader = FileSystemLoader(_get_resource_dir('templates'))
        self._env = Environment(loader=loader,
                                keep_trailing_newline=True,
                                trim_blocks=True,
                                lstrip_blocks=True)

    def render_sheet(self, sheet, chart_type='bar',
                     width=600, height=400,
                     embed=False, **keywords):
        sheet.name_columns_by_row(0)
        gantt_data = dict(
            tasks=_dumps(sheet.get_records()),
            title=sheet.name,
            width=width,
            height=height
        )
        if embed:
            template = self._env.get_template('embed.html')
        else:
            template = self._env.get_template('full.html')
        html_content = template.render(**gantt_data)
        if PY2:
            html_content = html_content.encode('utf-8')
        html_content = freeze_js(html_content)
        self._stream.write(html_content)


def _get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


def freeze_js(html_content):
    matches = js_pattern.finditer(html_content)

    if not matches:
        return html_content

    for match in reversed(tuple(matches)):
        # JS file name
        src_matches = js_src_pattern.findall(match.group(1))

        js_content = ""
        for src in reversed(src_matches):
            file_path = os.path.join(_get_resource_dir('templates'), src)

            with open(file_path, "r") as f:
                js_content += f.read() + '\n'
        # Replace matched string with inline JS
        fmt = '<script type="text/javascript">{}</script>'
        js_content = fmt.format(js_content)
        html_content = (html_content[:match.start()] + js_content +
                        html_content[match.end():])

    return html_content
