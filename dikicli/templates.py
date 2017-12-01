HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" content="width=device-width, initial-scale=1">
<title>{% word %}</title>
<style type="text/css">
    body{margin:40px auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:0 10px}
    h1,h2,h3{line-height:1.2}
</style>
</head>
<body>

{% content %}

</body>
</html>
"""

CONFIG_TEMPLATE = """\
[dikicli]
data dir = {data_dir}
prefix = {prefix}
linewrap = {linewrap}
colors = {colors}
web browser = {browser}
"""
