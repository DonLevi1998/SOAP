from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return "Hello, World!"

application = Application(
    [HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, WsgiApplication(application))
    print("SOAP service running at http://127.0.0.1:8000/")
    print("WSDL available at http://127.0.0.1:8000/?wsdl")
    server.serve_forever()
