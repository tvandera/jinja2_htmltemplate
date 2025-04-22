from jinja2_htmltemplate.translate import HtmlTemplate

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

with open(args.input, "r") as f:
    html_template_input_string = f.read()

jinja_output = HtmlTemplate().from_string(html_template_input_string)

with open(args.output, "w") as f:
    f.write(jinja_output)