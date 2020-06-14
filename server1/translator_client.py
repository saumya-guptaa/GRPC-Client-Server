import grpc
import translator_pb2
import translator_pb2_grpc
with open('haproxy.crt', 'rb') as f:
    trusted_certs = f.read()
#credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
#print(os.environ.get("SERVER_ADDRESS"))
channel = grpc.insecure_channel("localhost:50053")#,credentials)
stub = translator_pb2_grpc.TranslatorStub(channel)
s1=input('Enter string here: ')
s2=input('Enter dest here: ')
text = translator_pb2.Text(value=s1,dest=s2)
response = stub.GoogTrans(text)
print(response.value)
