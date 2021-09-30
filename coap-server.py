from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

# CoAP에서 자원은 무엇인가?
# 자원은 등록될 수 있고 수정될 수 있고 조회될 수 있고 삭제될 수 있는 "대상" = IoT 자원

class HelloWorldResource(Resource):
    def __init__(self, name = "hello-world", coap_server=None):
        super(HelloWorldResource,self).__init__(name, coap_server, visible=True, observable=True, 
                allow_children=True)

        self.payload = "Get a friendly getting!!"

    def render_GET(self, request):
        self.payload = "Hello World from CoAPthon!"
        return self

class PingResource(Resource):
    def __init__(self, name="ping", coap_server=None):
        super(PingResource, self).__init__(name, coap_server, visible=True, observable=True, 
                allow_children=True)

    def render_GET(self, request):
        self.payload = "pong!"
        return self

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self,(host, port))
        self.add_resource('hello-world/', HelloWorldResource())
        self.add_resource('ping/', PingResource())

if __name__ == '__main__':
    server = CoAPServer("0.0.0.0", 5681)
    try:
        print("Server Started")
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")
