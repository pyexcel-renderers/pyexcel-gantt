from pyexcel_gantt.gantt import freeze_js


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
    print(html_content)
