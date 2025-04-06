from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spline 3D Scene</title>
  <style>
    html, body {
      margin: 0;
      height: 100%;
      overflow: hidden;
    }
    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <iframe src="https://my.spline.design/robotfollowcursorforlandingpage-f010d93d1e6dca5fa37a9dd595f4f9b2/"></iframe>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

