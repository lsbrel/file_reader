import pandas

class FileController:


    def __init__(self, file) -> None:

        self.__readFile(file=file)

    def getData(self, index):

        return self.__getFile().iloc[[index]]

    def setData(self, index, value, position):

        self.__getFile().loc[index, position] = value


    def saveFile(self, file):

        self.__getFile().to_csv(file, index=False, sep=';')

    def getNumLines(self):

        return self.num_lines

    def prettier(self, file):

        return file.to_string(index=False)

    def getYear(self,file):
        aux = file.split('-')[0]
        return aux[-4:]

    def transformDate(self, date):
        try:
            date = date.split('/')
            return f'{date[1]}-{date[0]}'

        except:
            return '01-01'

    # PRIVATE METHODS

    def __readFile(self, file) -> None:
        self.file = pandas.read_csv(file, sep=';')
        self.num_lines = len(self.file)

    def __getFile(self):

        return self.file

    # PRIVATE METHODS
