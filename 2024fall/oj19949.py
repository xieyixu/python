import re

def count_entities(document):
    entities=re.findall(r'###(.*?)###(?:\s###(.*?)###)*',document)
    count=len(entities)
    return count
d=input()
print(count_entities(d))