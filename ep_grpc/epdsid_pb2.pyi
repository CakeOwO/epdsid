from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vazio(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Long(_message.Message):
    __slots__ = ("valor",)
    VALOR_FIELD_NUMBER: _ClassVar[int]
    valor: int
    def __init__(self, valor: _Optional[int] = ...) -> None: ...

class ListaLong(_message.Message):
    __slots__ = ("valores",)
    VALORES_FIELD_NUMBER: _ClassVar[int]
    valores: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, valores: _Optional[_Iterable[int]] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("texto",)
    TEXTO_FIELD_NUMBER: _ClassVar[int]
    texto: str
    def __init__(self, texto: _Optional[str] = ...) -> None: ...

class Contato(_message.Message):
    __slots__ = ("id", "nome", "email", "telefone", "rotulos", "endereco", "favorito")
    class Endereco(_message.Message):
        __slots__ = ("nomeendereco", "cidade", "estado", "cep", "pais")
        NOMEENDERECO_FIELD_NUMBER: _ClassVar[int]
        CIDADE_FIELD_NUMBER: _ClassVar[int]
        ESTADO_FIELD_NUMBER: _ClassVar[int]
        CEP_FIELD_NUMBER: _ClassVar[int]
        PAIS_FIELD_NUMBER: _ClassVar[int]
        nomeendereco: str
        cidade: str
        estado: str
        cep: str
        pais: str
        def __init__(self, nomeendereco: _Optional[str] = ..., cidade: _Optional[str] = ..., estado: _Optional[str] = ..., cep: _Optional[str] = ..., pais: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    ROTULOS_FIELD_NUMBER: _ClassVar[int]
    ENDERECO_FIELD_NUMBER: _ClassVar[int]
    FAVORITO_FIELD_NUMBER: _ClassVar[int]
    id: int
    nome: str
    email: str
    telefone: str
    rotulos: _containers.RepeatedScalarFieldContainer[str]
    endereco: Contato.Endereco
    favorito: bool
    def __init__(self, id: _Optional[int] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., telefone: _Optional[str] = ..., rotulos: _Optional[_Iterable[str]] = ..., endereco: _Optional[_Union[Contato.Endereco, _Mapping]] = ..., favorito: bool = ...) -> None: ...

class StatusTransacao(_message.Message):
    __slots__ = ("status", "msgstatus")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSGSTATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    msgstatus: str
    def __init__(self, status: bool = ..., msgstatus: _Optional[str] = ...) -> None: ...

class ContatoId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Contatos(_message.Message):
    __slots__ = ("contatos",)
    CONTATOS_FIELD_NUMBER: _ClassVar[int]
    contatos: _containers.RepeatedCompositeFieldContainer[Contato]
    def __init__(self, contatos: _Optional[_Iterable[_Union[Contato, _Mapping]]] = ...) -> None: ...
