from time import perf_counter
import numpy as np

import grpc
import epdsid_pb2
import epdsid_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = epdsid_pb2_grpc.TestesStub(channel)


def ChamadaVazio():
    return stub.ChamadaVazio(epdsid_pb2.Vazio())


def ValorAbsolutoLong(valor):
    return stub.ValorAbsolutoLong(epdsid_pb2.Long(valor=valor))


def SomaListaLong(valores):
    return stub.SomaListaLong(epdsid_pb2.ListaLong(valores=valores))


def InverteString(texto):
    return stub.InverteString(epdsid_pb2.String(texto=texto))


def AdicionaContato(**contato):
    return stub.AdicionaContato(epdsid_pb2.Contato(**contato))


def PegaContato(id):
    return stub.PegaContato(epdsid_pb2.ContatoId(id=id))


def AtualizaContato(**contato):
    return stub.AtualizaContato(epdsid_pb2.Contato(**contato))


def RemoveContato(id):
    return stub.RemoveContato(epdsid_pb2.ContatoId(id=id))


def ListaContatos():
    return stub.ListaContatos(epdsid_pb2.Vazio())
