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


def SomaOitoLong(a, b, c, d, e, f, g, h):
    return stub.SomaOitoLong(epdsid_pb2.OitoLong(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h))


def InverteString(texto):
    return stub.InverteString(epdsid_pb2.String(texto=texto))


def ChamadaComplexo(id, nome, tags):
    return stub.ChamadaComplexo(epdsid_pb2.SolicitacaoComplexo(id=id, nome=nome, tags=tags))
