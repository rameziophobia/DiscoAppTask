from abc import ABC, abstractmethod
import pandas as pd
import io


class BaseFileLoader(ABC):
    @abstractmethod
    def load(self, file):
        pass


class BaseFileConverter(ABC):
    @abstractmethod
    def convert(self, file):
        pass


class JsonConverter(BaseFileConverter):
    def convert(self, df):
        return df.to_json(orient='records')


class CsvFileLoader(BaseFileLoader):
    def load(self, file):
        return pd.read_csv(file)


class XlsxFileLoader(BaseFileLoader):
    def load(self, file):
        return pd.read_excel(file)


class XmlFileLoader(BaseFileLoader):
    def load(self, file):
        xml_data = io.BytesIO(file.read())
        return pd.read_xml(xml_data)


class FileConverter():
    # Bridge pattern is used for the converter, data loader
    def __init__(self, fromType, toType):
        self.dataLoader = None
        self.converter = None
        if fromType == 'csv':
            self.dataLoader = CsvFileLoader()
        if fromType == 'xml':
            self.dataLoader = XmlFileLoader()
        if fromType == 'xlsx':
            self.dataLoader = XlsxFileLoader()
        if toType == 'json':
            self.converter = JsonConverter()

    def convert(self, file):
        if self.dataLoader is None or self.converter is None:
            raise NotImplementedError()
        data = self.dataLoader.load(file)
        return self.converter.convert(data)
