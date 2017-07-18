from pyexcel.renderer import Renderer
from jinja2 import Environment, FileSystemLoader

import pyexcel_gantt.utils as utils


class Chart(Renderer):
    def __init__(self, file_type):
        Renderer.__init__(self, file_type)
        loader = FileSystemLoader(utils.get_resource_dir('templates'))
        self._env = Environment(loader=loader,
                                keep_trailing_newline=True,
                                trim_blocks=True,
                                lstrip_blocks=True)

    def render_sheet(self, sheet, chart_type='bar',
                     width=600, height=400,
                     embed=False, **keywords):
        sheet.name_columns_by_row(0)
        gantt_data = dict(
            tasks=utils.dumps(sheet.get_records()),
            title=sheet.name,
            width=width,
            height=height
        )
        if embed:
            template = self._env.get_template('embed.html')
        else:
            template = self._env.get_template('full.html')
        html_content = template.render(**gantt_data)
        if utils.PY2:
            html_content = html_content.encode('utf-8')
        html_content = utils.freeze_js(html_content)
        self._stream.write(html_content)

    def render_book(self, book, **keywords):
        raise Exception("Rendering book is not supported."
                        " Please specify a sheet index or sheet name")
