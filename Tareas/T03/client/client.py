import threading
import socket
from interface import Controller

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # Inicializa UI
        self.controller = Controller(self)

        # Crear socket IPv4, TCP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((self.host, self.port))
            self.connected = True

            listen_thread = threading.Thread(
                target=self.listen_server, daemon=True)

            listen_thread.start()

        except ConnectionRefusedError:
            print(f"No se pudo conectar a {self.host}:{self.port}")
            self.client_socket.close()

    def listen_server(self):
        try:
            while self.connected:
                mensaje = self.receive()
                # cambiar esto con lógica cliente
                # self.controlador.manejar_mensaje(mensaje)
        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.client_socket.close()

    def send(self, message):
        print("cliente envía mensaje a servidor!")
        try:
            # Encodea y serializa mensaje
            encoded_message = self.encode_message(message)
            print(encoded_message)

            # Largo mensaje en big endian
            message_length = len(encoded_message).to_bytes(4, byteorder='big')
            client_socket.sendall(message_length)

            message_array = bytearray(encoded_message)
            block_number = 1

            while message_array:
                # Envía numero de bloque
                client_socket.sendall(
                    block_number.to_bytes(4, byteorder='little'))
                block_number += 1

                # Si el bloque es de 60 o más bytes, envía bloque
                if len(message_array) >= 60:
                    client_socket.sendall(message_array[:60])
                    del message_array[:60]

                # Si tiene menos de 60, rellena con bytes 0 y lo envía
                else:
                    client_socket.sendall(message_array.ljust(60, '\0'))
                    message_array = None

        except ConnectionError:
            self.client_socket.close()

    # Recibe mensaje de cliente, lee largo del mensaje y cada número de bloque
    def receive(self):
        response_bytes_length = self.client_socket.recv(4)
        response_length = int.from_bytes(
            response_bytes_length, byteorder='big')
        response = bytearray()

        # Calcula bloques totales a recibir
        total_blocks = ceil(response_length / 60)
        block_number = 0

        while block_number < total_blocks:
            block_number = int.from_bytes(self.client_socket.recv(4), byteorder='little')
            response.extend(self.client_socket.recv(60))

        # Calcula la cantidad de ceros que se agregó y los elimina
        extra_blocks = len(response) - response_length
        adjusted_response = response[:-extra_blocks]

        received = adjusted_response.decode()
        message = self.decode_message(received)

        return message

    def encode_message(self, message):

        try:
            # Create JSON object
            json_message = json.dumps(message)
            # Encode JSON object
            bytes_message = json_message.encode()

            return bytes_message
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    def decode_message(message_bytes):
        try:
            message = json.loads(message_bytes)
            return message
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()
