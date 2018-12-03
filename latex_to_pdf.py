import nbconvert.exporters.pdf as pdf
import sys

if __name__ == '__main__':
    name = 'book.tex'
    f = open(name, 'r',  encoding="iso-8859-1")
    filedata = f.read()
    f.close()

    # postprocess
    newdata = filedata
	
    f = open(name, 'w', encoding="iso-8859-1")
    f.write(newdata)
    f.close()


    p = pdf.PDFExporter()
    p.run_latex(name)