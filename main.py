import socket
import numpy as np
import cv2
import mss
import struct
import time

def run_client():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
