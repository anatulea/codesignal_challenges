'''
You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.

For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:

Initially their similarity is 0
Then, it is increased by the following rules:
+5, if the same protocol is used in both URLs.
+10, if url1 and url2 have the same address.
+k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
+1 if for each varNames common between them. Additional +1 if the respective values are equal too.
URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given in [] are optional, and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName and value) are guaranteed to contain only alphanumeric characters and periods.

Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

Example

For

url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
and

url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
the output should be
urlSimilarity(url1, url2) = 19.

Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.
'''
from urllib.parse import urlparse, parse_qs
from itertools import takewhile

def urlSimilarity(url1, url2):
    first_url = urlparse(url1)
    second_url = urlparse(url2)
    count = (first_url.scheme == second_url.scheme) * 5 + (first_url.netloc == second_url.netloc) * 10
        
    path1 = first_url.path.split('/')[1:]
    path2 = second_url.path.split('/')[1:]
    count += len(list(takewhile(lambda x: x[0] == x[1], zip(path1, path2))))
    
    query1 = parse_qs(first_url.query)
    query2 = parse_qs(second_url.query)
    count += sum(2 if query1[q] == query2[q] else 1 for q in query1.keys() & query2.keys())
        
    return count


'''
import re
def urlSimilarity(url1, url2):
    def urlStructure(url):
        (protocol, address, path, query) = re.findall(
            r'^(\w+)://([^/^?]+)([^?]*)\??(.*)$',
            url
        )[0]
        s = {'protocol': protocol, 'address': address}
        s['path'] = re.findall(r'(/[^/]+)',path)
        s['query'] = {}
        for q in re.findall(r'([^=^&]+=[^&]+)',query):
            (k,v) = q.split('=')
            s['query'][k] = v
        return s
    score = 0
    s1 = urlStructure(url1)
    s2 = urlStructure(url2)
    if s1['protocol'] == s2['protocol']:
        score += 5
    if s1['address'] == s2['address']:
        score += 10
    for i,v in enumerate(zip(s1['path'],s2['path'])):
        if v[0] == v[1]:
            score += 1
        else:
            break
    for k in s1['query'].keys() & s2['query'].keys():
        score += 2 if s1['query'][k] == s2['query'][k] else 1 
    return score
    '''
    