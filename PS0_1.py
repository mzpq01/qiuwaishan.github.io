from HTMLParser import HTMLParser
import requests
import csv
 
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lists = []
        self.flag = 0
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "td":
            #print tag,attrs
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "class":
                        self.flag = 1

    def handle_data (self, data):
        if self.flag == 1:       
            self.lists.append( data )
            self.flag = 0
 
if __name__ == "__main__":
    response = requests.get('http://duspviz.mit.edu/_assets/data/riyadh_taz_data.html')
    html_code = response.text
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.lists)

    # output the result to .csv
    with open("output.csv", "wb") as csvfile:
        spamwriter = csv.writer( csvfile, dialect="excel", quotechar=',')
        spamwriter.writerow( ["taz", "popsaudimale", "popsaudifemale", 'totsaudi', "popnonsaudimale", "popnonsaudifemale", "totnonsaudi", "totpop"] )
        for i in xrange( len(hp.lists) ):
            if i % 8 == 0:
                if i != 0:
                    print writerow_line_list
                    spamwriter.writerow( writerow_line_list )
                writerow_line_list = []
            if hp.lists[i] != '\n':
                writerow_line_list.append( hp.lists[i] )
            else:
                writerow_line_list.append( " " )

    print "success"

