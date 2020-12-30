import json
import socket
import threading
from random import choice
from math import ceil
from players import Player, read_names, create_player_list
from logic import Logic


# from logic import Logic


# Parte del código fue sacado de la actividad AF05

class Server:

    def __init__(self, host, port, log_on=True):

        self.host = host
        self.port = port
        self.log_on = log_on

        print("Inicializando servidor...")

        # Crear socket IPv4, TCP
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Ligar socket
        self.socket_server.bind((self.host, self.port))

        # Permite escuchar
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}")
        print("Servidor aceptando conexiones")

        # self.logic = Logic()

        # Crea y comienza thread encargado de aceptar clientes
        thread = threading.Thread(target=self.accept_clients, daemon=True)
        thread.start()

        # Carga lista de nombres

        self.players = create_player_list(read_names("names.txt"))

    # Acepta clientes y crea threads para escucharlos
    def accept_clients(self):

        print("Aceptando conexiones! ...")
        while True:
            client_socket, _ = self.socket_server.accept()
            player = choice(self.players)
            while player.client_socket:
                player = choice(self.players)
            player.client_socket = client_socket
            self.log(player, "Conectarse", "-")
            listen_client_thread = threading.Thread(
                target=self.listen_client,
                args=(player, ),
                daemon=True)

            listen_client_thread.start()

    def listen_client(self, player):
        try:
            while True:
                received = self.receive(player.client_socket)
                if received != "":
                    pass
                    # acá hay que cambiar según logica del backend 
                    # response = self.logica.manejar_mensaje(received, player, self.players)
                    # self.enviar_lista_respuestas(player, response)

        except ConnectionResetError:
            print(f"Error: conexión con {player} fue reseteada.")

        print(f"Cerrando conexión con {player}.")
        self.delete_client(player)

    # Encodea y serializa el mensaje (usando encode_message), agrega largo de bytes y número de bloque al mensaje
    # Divide contenido mensaje en bloques de 60bytes, rellena último bloque si es menor a 60
    def send(self, message, client_socket):
        print("servidor envía mensaje a cliente!")
        # Encodea y serializa mensaje
        encoded_message = self.encode_message(message)

        # Largo mensaje en big endian
        message_length = len(encoded_message).to_bytes(4, byteorder='big')
        client_socket.sendall(message_length)

        message_array = bytearray(encoded_message)
        block_number = 1

        while message_array:
            # Envía numero de bloque
            client_socket.sendall(block_number.to_bytes(4, byteorder='little'))
            block_number += 1

            # Si el bloque es de 60 o más bytes, envía bloque
            if len(message_array) >= 60:
                client_socket.sendall(message_array[:60])
                del message_array[:60]

            # Si tiene menos de 60, rellena con bytes 0 y lo envía
            else:
                client_socket.sendall(message_array.ljust(60, '\0'))
                message_array = None

    # Recibe mensaje de cliente, lee largo del mensaje y cada número de bloque
    def receive(self, client_socket):
        response_bytes_length = client_socket.recv(4)
        response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
        if response_length != 0:
            response = bytearray()

            # Calcula bloques totales a recibir
            total_blocks = ceil(response_length / 60)
            block_number = 0

            while block_number < total_blocks:
                block_number = int.from_bytes(client_socket.recv(4), byteorder='little')
                response.extend(client_socket.recv(60))

            # Calcula la cantidad de ceros que se agregó y los elimina
            extra_blocks = len(response) - response_length
            adjusted_response = response[:-extra_blocks]
            print(f"mensaje:{adjusted_response}")
            # print(type(adjusted_response))

            message = self.decode_message(adjusted_response)

            return message
        else:
            return ""
    def log(self, player, action, detail):
        name_headline = "Nombre"
        action_headline = "Acción"
        details_headline = "Detalle"
        if self.log_on:
            print(f"\n {name_headline:^10s} | {action_headline:^15s} | {details_headline:<30s}")
            print(f"\n {player.username:^10s} | {action:^15s} | {detail:<30s}")

    # Serializa el mensaje en JSON y lo encodea en UTF-8 (Por defecto)
    @staticmethod
    def encode_message(message):

        try:
            # Create JSON object
            json_message = json.dumps(message)
            # Encode JSON object
            bytes_message = json_message.encode()

            return bytes_message
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    @staticmethod
    def decode_message(message_bytes):
        try:
            message = json.loads(message_bytes)
            return message
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()

    def delete_client(self, player):
        self.players.remove(player)
        player.client_socket.close()
        player.client_socket = None
        player.address = None

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 47365
    test_server = Server(HOST, PORT)
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_server.send({"comando": "actualizar_jugadores", "jugadores": [
                     "tomasgv", "dasdsa", "gatochico", "cothidalgo", "cruz", "drpinto1", "jfuentesg26", "bvasquezm"]}, test_socket)
