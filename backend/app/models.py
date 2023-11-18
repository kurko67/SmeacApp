from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who

id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=True)
    email = Column(String(100), unique=True, nullable=True)

"""

class Form(Model):
    __tablename__ = "forms"
    id = Column(Integer, primary_key=True, autoincrement=True)

    #firstForm

    firstctrl1 = Column(String(250), nullable=True)
    firstctrl2 = Column(String(250), nullable=True)
    firstctrl3 = Column(String(250), nullable=True)
    firstctrl4 = Column(String(250), nullable=True)
    firstctrl5 = Column(String(250), nullable=True)
    firstctrl6 = Column(String(250), nullable=True)
    firstctrl7 = Column(String(250), nullable=True)
    firstctrl8 = Column(String(250), nullable=True)
    firstctrl9 = Column(String(250), nullable=True)
    firstctrl10 = Column(String(250), nullable=True) 
    firstctrl11 = Column(String(250), nullable=True)
    firstctrl12 = Column(String(250), nullable=True)
    firstctrl13 = Column(String(250), nullable=True)

    #secondForm

    secondctrl1 = Column(String(250), nullable=True)
    secondctrl2 = Column(String(250), nullable=True)

    #thirdForm

    thirdctrl1 = Column(String(250), nullable=True)
    thirdctrl2 = Column(String(250), nullable=True)
    thirdctrl3 = Column(String(250), nullable=True)
    thirdctrl4 = Column(String(250), nullable=True)
    thirdctrl5 = Column(String(250), nullable=True)
    thirdctrl6 = Column(String(250), nullable=True)
    thirdctrl7 = Column(String(250), nullable=True)
    thirdctrl8 = Column(String(250), nullable=True)
    thirdctrl9 = Column(String(250), nullable=True)
    thirdctrl10 = Column(String(250), nullable=True)
    thirdctrl11 = Column(String(250), nullable=True) 
    thirdctrl12 = Column(String(250), nullable=True)
    thirdctrl13 = Column(String(250), nullable=True)
    thirdctrl14 = Column(String(250), nullable=True)
    thirdctrl15 = Column(String(250), nullable=True)
    thirdctrl16 = Column(String(250), nullable=True)
    thirdctrl17 = Column(String(250), nullable=True)
    thirdctrl18 = Column(String(250), nullable=True)

     #fourtForm

    fourtctrl1 = Column(String(250), nullable=True)
    fourtctrl2 = Column(String(250), nullable=True)
    fourtctrl3 = Column(String(250), nullable=True)
    fourtctrl4 = Column(String(250), nullable=True)
    fourtctrl5 = Column(String(250), nullable=True)
    fourtctrl6 = Column(String(250), nullable=True)

    #fiveForm

    fivectrl1 = Column(String(250), nullable=True)
    fivectrl2 = Column(String(250), nullable=True)
    fivectrl3 = Column(String(250), nullable=True)
    fivectrl4 = Column(String(250), nullable=True)
    fivectrl5 = Column(String(250), nullable=True)
    fivectrl6 = Column(String(250), nullable=True)
    fivectrl7 = Column(String(250), nullable=True)
    fivectrl8 = Column(String(250), nullable=True)

    created_at = Column(DateTime, default=func.now(), nullable=False)

