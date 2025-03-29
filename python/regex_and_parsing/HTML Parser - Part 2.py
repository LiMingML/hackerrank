from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment', data, sep='\n')
        else:
            print('>>> Single-line Comment', data, sep='\n')

    def handle_data(self, data):
        if data.strip():
            print('>>> Data', data, sep='\n')


parser = MyHTMLParser()
html = '\n'.join([input() for _ in range(int(input()))])
parser.feed(html)