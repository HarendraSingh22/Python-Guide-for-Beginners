
'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
'''

def make_tags(tags, word):
  start_tag = '<'+ tags + '>'
  end_tag = '</'+ tags + '>'
  element = start_tag + word + end_tag
  return element
  
tags = 'cite'
word = 'Yay'
print(make_tags(tags,word))