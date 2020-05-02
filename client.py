import grpc
import mle_service_pb2
import mle_service_pb2_grpc
test = {
              "models": ["001", "002", "003", "qwteu"],
              "data":
                            {
                                          "pclass": 1,
                                          "name": "Futrelle, Mrs. Jacques Heath (Lily May Peel)",
                                          "sex": "female",
                                          "sibsp": 3,
                                          "parch": 3,
                                          "embarked": "Q",
                                          "fare": 150,
                                          "age": 20
                            }
}
def send_data(data):
    # открываем канал и создаем клиент
    channel = grpc.insecure_channel('localhost:6066')
    stub = mle_service_pb2_grpc.MleServiceStub(channel)
    request_models = mle_service_pb2.Request()
    request_models.models.extend(data['models'])
    for key, value in data['data'].items():
        setattr(request_models.data, key, value)
    # try:
    response = stub.get_predict(request_models)
# except grpc.RpcError as e:
#     err = e.code()
#     print(err.name, err.value, grpc.StatusCode)
# else:
    print(response)
    return response


send_data(test)
