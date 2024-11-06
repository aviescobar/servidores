import socket
import numpy as np
import cv2
import mss
import struct
import time

def run_client():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    client_socket.connect(('172.168.3.95', 5000))  # Asegúrate de que esta IP sea la correcta para el servidor

    with mss.mss() as sct:
        while True:
             try:

