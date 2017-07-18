import os
import pyexcel as p
from pyexcel_gantt.gantt import Chart


def test_full_html():
    chart = Chart('html')
    content = chart.get_io()
    chart.set_output_stream(content)
    sheet = p.get_sheet(file_name=os.path.join('demo', 'tasks.csv'))
    chart.render_sheet(sheet)
    assert "Task 2, Task 3" in content.getvalue()


def test_embed_html():
    chart = Chart('html')
    content = chart.get_io()
    chart.set_output_stream(content)
    sheet = p.get_sheet(file_name=os.path.join('demo', 'tasks.csv'))
    chart.render_sheet(sheet, embed=True)
    html_content = content.getvalue()
    assert "Task 2, Task 3" in html_content
    assert 'Snap.svg 0.5.0' not in html_content
    assert 'version : 2.18.1' not in html_content
    assert 'exports.Gantt' not in html_content
