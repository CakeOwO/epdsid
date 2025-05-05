from concurrent import futures

import grpc
import epdsid_pb2
import epdsid_pb2_grpc


class Testes(epdsid_pb2_grpc.TestesServicer):

    def ChamadaVazio(self, request, context):
        return epdsid_pb2.Vazio()

    def ValorAbsolutoLong(self, request, context):
        return epdsid_pb2.Long(valor=abs(request.valor))

    def SomaOitoLong(self, request, context):
        total = request.a + request.b + request.c + request.d + \
            request.e + request.f + request.g + request.h
        return epdsid_pb2.Long(valor=total)

    def InverteString(self, request, context):
        return epdsid_pb2.String(texto=request.texto[::-1])

    def ChamadaComplexo(self, request, context):
        return epdsid_pb2.RespostaComplexo(status=f"Recebido {request.nome} com id {request.id} e número de tags {len(request.tags)}")


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    epdsid_pb2_grpc.add_TestesServicer_to_server(Testes(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("gRPC server running on port " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
