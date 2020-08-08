import collections
from operator import itemgetter

def solution(l):
    
    # Your code here
    Version = collections.namedtuple('Vnumber', ['version', 'major', 'minor', 'revision'])
    versions = []
    
    for i in l:
        if len(i.split(".")) == 1:
            versions.append(Version(i, int(i.split(".")[0]), -1, -1))
        elif len(i.split(".")) == 2:
            versions.append(Version(i, int(i.split(".")[0]), int(i.split(".")[1]), -1))
        else:
            versions.append(Version(i, int(i.split(".")[0]), int(i.split(".")[1]), int(i.split(".")[2])))
    
    sort_versions = versions.sort(key = itemgetter(1,2,3))

    final_result = []

    for i in range(len(versions)):
        final_result.append(versions[i].version)

    return final_result
