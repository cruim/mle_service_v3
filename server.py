import time
from concurrent import futures
import grpc
import app
import mle_service_pb2
import mle_service_pb2_grpc
from google.protobuf.json_format import MessageToDict


class MLEServicer(mle_service_pb2_grpc.MleServiceServicer):
    def get_predict(self, request, context):
        response = mle_service_pb2.Responce()
        predict, status_code = app.get_predict(MessageToDict(request))
        if status_code == 200:
            for pred in predict:
                data = mle_service_pb2.ResponceModel()
                data.model_id = pred.get('model_id', 'unknown')
                data.value = pred.get('value', '0')
                data.result_code = pred.get('result_code', '0')
                data.error = pred.get('error', '')
                response.data.extend([data])
        else:
            response.message = str(predict)
        response.code = status_code
        return response
def serve():
    # создаем сервер
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    # прикреплям хандлеры
    mle_service_pb2_grpc.add_MleServiceServicer_to_server(MLEServicer(), server)
    # запускаемся на порту 6066
    print('Starting server on port 6066.')
    server.add_insecure_port('[::]:6066')
    server.start()
    # работаем час или до прерывания с клавиатуры
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
