class FileConverter():
  def __init__(self, fromType, toType, file):
    self.fromType = fromType
    self.toType = toType
    self.file = file

  def convert(self):
    raise NotImplementedError()

