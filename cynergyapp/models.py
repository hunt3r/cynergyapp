from sqlalchemy import Column, Integer, String
from database import Base

class Entry(Base):
    __tablename__ = 'entries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    type = Column(String(50), unique=False)
    library = Column(String(50), unique=False)
    from_buss = Column(String(50), unique=False)
    to_buss = Column(String(50), unique=False)
    length = Column(Integer)
    ampacity = Column(Integer)

    def __init__(self, name=None, 
                       type=None,
                       library=None,
                       from_buss=None,
                       to_buss=None,
                       length=None,
                       ampacity=None):
                       
        self.name = name
        self.type = type
        self.library = library
        self.from_buss = from_buss
        self.to_buss = to_buss
        self.length = length
        self.ampacity = ampacity
        

    def __repr__(self):
        return self.name