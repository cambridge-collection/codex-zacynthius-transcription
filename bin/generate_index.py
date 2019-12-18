import re
import sys
from os import path
from pathlib import Path
from html import escape

template = """\
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Codex Zacynthius Transcription</title>
  </head>
  <body>
    <div class="container mt-4">
      <div class="jumbotron">
        <h1 xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Codex Zacynthius Transcription</h1>
        <p class="lead">
          This site hosts the Codex Zacynthius transcriptions used on the <a href="https://cudl.lib.cam.ac.uk">Cambridge Digital Library</a>.
        </p>
        <p>
          The HTML transcriptions are created by the <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.birmingham.ac.uk/research/activity/itsee/projects/codex-zacynthius.aspx" property="cc:attributionName" rel="cc:attributionURL">Codex Zacynthius project</a> and are licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
        </p>
      </div>

{indexes}
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
"""

index_section_template = """\
<h2>{name}</h2>

<ul>
{entries}
</ul>
"""

index_entry_template = """\
<li><a href="{href}">{name}</a></li>\
"""


def extract_numbers(string):
  return tuple(int(m.group(1)) if m.group(1) else m.group(2)
               for m in re.finditer('(?:(\d+)|([^\d]+))', string))


def indent(text=None, lines=None, by=1, using='  '):
  if text is not None:
    if lines is not None:
      raise ValueError("Can't specify lines and text")
    return '\n'.join(indent(lines=text.split('\n'), by=by, using=using))

  if lines is None:
    raise ValueError("lines or text must be specified")
  return (f'{using * by}{line}' for line in lines)


def render_index_entry(path):
  href = '/'.join(path.parts[-2:])
  return index_entry_template.format(name=escape(path.stem), href=escape(href))


def render_index(path):
  assert path.is_dir()

  return index_section_template.format(name=escape(path.name.capitalize()), entries='\n'.join(
    indent(lines=(render_index_entry(f) for f in sorted(path.glob('*.html'),
                                                        key=lambda p: extract_numbers(p.stem))))
  ))


def render(path):
  assert path.is_dir()

  index_dirs = sorted([f for f in path.iterdir() if f.is_dir()])
  indexes = indent(text=''.join(render_index(path) for path in index_dirs), by=3)

  return template.format(indexes=indexes)


def main():
  if len(sys.argv) != 2:
    print("Usage: generate_index.py <transcription-dir>", file=sys.stderr)

  transcription_dir = Path(sys.argv[1])
  sys.stdout.write(render(transcription_dir))


if __name__ == '__main__':
  main()
