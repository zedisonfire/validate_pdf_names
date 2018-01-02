import os


def getcharstwo():
    return ['ß', 'Â', 'Ú', 'þ', 'Ê', '¶', '·', 'Ò', 'Ô', '┴', 'Ý', '¾', 'Û', '║', '╔', '═']


def getvalues():
    return ['á', 'ô', 'é', 'ç', 'ã', 'ó', 'ú', 'ã', 'â', 'Á', 'í', 'ó', 'ê', 'º', 'É', 'Í']


def validatepdfnames():
    for folder in os.listdir('D:/2017_2_2/'):
        dir = 'D:/2017_2_2/'+folder+'/PROFESSOR/'
        ascii = getcharstwo()
        nonascii = getvalues()
        newpdf = ''
        for pdf in os.listdir(dir):
            aux = pdf
            bool = False
            for char in pdf:
                if char in ascii:
                    bool = True
                    newpdf = aux.replace(char, nonascii[ascii.index(char)])
                    aux = newpdf
            if bool is True:
                print(newpdf)
                os.rename(dir+pdf, dir+newpdf)


validatepdfnames()
