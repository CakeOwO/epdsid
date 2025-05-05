from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Vazio(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Long(_message.Message):
    __slots__ = ("valor",)
    VALOR_FIELD_NUMBER: _ClassVar[int]
    valor: int
    def __init__(self, valor: _Optional[int] = ...) -> None: ...

class OitoLong(_message.Message):
    __slots__ = ("a", "b", "c", "d", "e", "f", "g", "h")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
    g: int
    h: int
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[int] = ..., d: _Optional[int] = ..., e: _Optional[int] = ..., f: _Optional[int] = ..., g: _Optional[int] = ..., h: _Optional[int] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("texto",)
    TEXTO_FIELD_NUMBER: _ClassVar[int]
    texto: str
    def __init__(self, texto: _Optional[str] = ...) -> None: ...

class SolicitacaoComplexo(_message.Message):
    __slots__ = ("id", "nome", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class RespostaComplexo(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
