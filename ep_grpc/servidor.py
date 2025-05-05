from concurrent import futures

import grpc
import epdsid_pb2
import epdsid_pb2_grpc


class Testes(epdsid_pb2_grpc.TestesServicer):
    def __init__(self):
        self.contatos = {}

    def ChamadaVazio(self, request, context):
        return epdsid_pb2.Vazio()

    def ValorAbsolutoLong(self, request, context):
        return epdsid_pb2.Long(valor=abs(request.valor))

    def SomaListaLong(self, request, context):
        return epdsid_pb2.Long(valor=sum(request.valores))

    def InverteString(self, request, context):
        return epdsid_pb2.String(texto=request.texto[::-1])

    def AdicionaContato(self, request, context):
        self.contatos[request.id] = request
        return epdsid_pb2.StatusTransacao(status=True, msgstatus="Contato adicionado com sucesso!")

    def PegaContato(self, request, context):
        contato = self.contatos[request.id]
        return contato if contato else epdsid_pb2.Contato

    def AtualizaContato(self, request, context):
        if request.id in self.contatos:
            self.contatos[request.id] = request
            return epdsid_pb2.StatusTransacao(status=True, msgstatus="Contato atualizado com sucesso!")
        else:
            return epdsid_pb2.StatusTransacao(status=False, msgstatus="Contato não encontrado!")

    def RemoveContato(self, request, context):
        return epdsid_pb2.StatusTransacao(status=True, msgstatus="Contato removido com sucesso!") if self.contatos.pop(request.id, None) else epdsid_pb2.StatusTransacao(status=False, msgstatus="Contato não encontrado!")

    def ListaContatos(self, request, context):
        return epdsid_pb2.Contatos(contatos=self.contatos.values())


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    epdsid_pb2_grpc.add_TestesServicer_to_server(Testes(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("gRPC server running on port " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
