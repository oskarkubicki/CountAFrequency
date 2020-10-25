from warcio.archiveiterator import ArchiveIterator
import string
import re

find_all_as= re.compile('a')
count =0
count_all = 0
alphabet_string = list(string.ascii_lowercase)

with open("CC", 'rb') as stream:
        for record in ArchiveIterator(stream,arc2warc=True):
            for letter in alphabet_string:
                if re.match('.+://.{0,4}'+letter, str(record.rec_headers.get_header('WARC-Target-URI'))):
                    text = record.content_stream().read()
                    count += text.decode('utf-8').count('a')
                    count_all += len(text.decode('utf-8'))

print(count)
print(count_all)
print("the final countdown "+str(float(count_all/count)))
