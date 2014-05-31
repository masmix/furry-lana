from sgmllib import SGMLParser
class URLLister(SGMLParser):
    def reset(self):                              #(1)
        SGMLParser.reset(self)
        self.urls = []
 
    def start_a(self, attrs):                     #(2)
        href = [v for k, v in attrs if k=='href'] #(3) (4)
        if href:
            self.urls.extend(href)

