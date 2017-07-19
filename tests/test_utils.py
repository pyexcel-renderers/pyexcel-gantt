from nose.tools import eq_
from pyexcel_gantt.utils import freeze_js, dumps
from datetime import date, datetime


def test_freeze_js():
    html_content = """
        </style>
        <!-- build -->
        <script src="js/moment-2.18.1.min.js"></script>
        <script src="js/snap.svg-0.5.1.min.js"></script>
        <script src="js/frappe-gantt-0.0.6.min.js"></script>
        <!-- endbuild -->
    </head><body>"""

    html_content = freeze_js(html_content)
    assert 'Snap.svg 0.5.0' in html_content
    assert 'version : 2.18.1' in html_content
    assert 'exports.Gantt' in html_content


def test_dumps():
    data = [date(2017, 7, 19), datetime(2017, 7, 19, 7, 22, 0)]
    json = dumps(data)
    eq_(json, '["2017-07-19", "2017-07-19"]')
