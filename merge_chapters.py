import io
import nbformat

def remove_formatting(nb):
    cells = nb['cells']
    for i in range (len(cells)):
        if 'source' in cells[i].keys():
            if cells[i]['source'][0:7] == '#format':
                del cells[i]
                return

def merge_notebooks(outfile, filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)
            remove_formatting(nb)
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)

    outfile.write(nbformat.writes(merged, nbformat.NO_CONVERT))

if __name__ == '__main__':
    with open('book.ipynb', 'w', encoding='utf-8') as f:
        merge_notebooks(f,
            ['./chapter1.ipynb',
             './chapter2.ipynb'])
