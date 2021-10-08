import html

def html_special_chars(data):
    return "".join([data.replace(n, html.escape(n)) for n in data.split('"'+'&<>')])

print(html_special_chars('<2>werw"<?&sd\'sfs>'))