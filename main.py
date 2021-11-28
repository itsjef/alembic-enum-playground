from enum import Enum

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def _(message: str) -> str:
    return message


class StrEnum(str, Enum):
    pass


class MyErrors(StrEnum):
    __slots__ = "_value_", "code"

    def __new__(cls, template, code):
        obj = str.__new__(cls, template)
        obj._value_ = template
        obj.code = code
        return obj

    def __str__(self):
        return self.value

    INCORRECT_ACCOUNT = (
        _("Incorrect account or password"),
        "L00001",
    )
    # FILE_UPDATE_DB = (
    #     _("File {id} update failed."),
    #     "F0001",
    # )

    FILE_EMPTY_ARCHIVE = (_("No files to download for given ids."), "F0005 ")
    FILE_NOT_FOUND = (_("File not found"), "F0004")
    FILE_NOT_EXISTS = (_("File not exists on given path."), "F0001")


class MyTable(Base):
    __tablename__ = "my_table"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    error = sa.Column(postgresql.ENUM(MyErrors))
