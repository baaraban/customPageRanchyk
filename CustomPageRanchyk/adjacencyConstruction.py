from bz2 import BZ2File

from tqdm import tqdm_notebook

DBPEDIA_RESOURCE_PREFIX_LEN = len("http://dbpedia.org/resource/")
SLICE = slice(DBPEDIA_RESOURCE_PREFIX_LEN + 1, -1)


# def get_lines(filename): return (line.split() for line in BZ2File(filename))

def get_lines(filename):
    source_file = BZ2File(filename, "r")
    count = 0
    for line in source_file:
        count += 1
        if count <= 3:
            print(line)
    source_file.close()

def get_redirect(target, redirects):
    seen = set()
    while True:
        transitive_target = target
        target = redirects.get(targ)
        if target is None or target in seen: break
        seen.add(target)
    return transitive_target


def get_redirects(redirects_filename):
    redirects = {}
    lines = get_lines(redirects_filename)
    # for line in lines:
    #     print(line)
    # return {src[SLICE]: get_redirect(targ[SLICE], redirects)
    #         for src, _, targ, _ in tqdm_notebook(lines)}


# def add_item(lst, redirects, index_map, item):
#     k = item[SLICE]
#     lst.append(index_map.setdefault(redirects.get(k, k), len(index_map)))


    #
    # index_map = dict() # links->IDs
    # lines = get_lines(page_links_filename)
    # source, destination, data = [],[],[]
    # for l, split in tqdm_notebook(enumerate(lines), total=limit):
    #     if l >= limit: break
    #     add_item(source, redirects, index_map, split[0])
    #     add_item(destination, redirects, index_map, split[2])
    #     data.append(1)
