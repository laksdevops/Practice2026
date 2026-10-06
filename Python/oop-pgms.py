# Basic class and object
# class Server:
#     def __init__(self, hostname):
#         self.hostname = hostname

#     def show_server(self):
#         print("Server:", self.hostname)


# server1 = Server("web01")
# server2 = Server("web02")

# server1.show_server()
# server2.show_server()

# Class with multiple attributes
# class Server:
#     def __init__(self, hostname, ip, environment):
#         self.hostname = hostname
#         self.ip = ip
#         self.environment = environment

#     def show_details(self):
#         print("Hostname:", self.hostname)
#         print("IP:", self.ip)
#         print("Environment:", self.environment)


# server1 = Server("web01", "192.168.1.10", "production")

# server1.show_details()

#self — very important
# class Server:
#     def __init__(self, hostname):
#         self.hostname = hostname

# server1 = Server("web01")
# server2 = Server("web02")

# print("server1 details", server1.hostname)
# print("server2 details", server2.hostname)

# Class with a method that performs an action
# class Server:

#     def __init__(self, hostname):
#         self.hostname = hostname

#     def start(self):
#         print(self.hostname, "is starting")

#     def stop(self):
#         print(self.hostname, "is stopping")


# server1 = Server("web01")

# server1.start()
# server1.stop()

# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b

# calc = Calculator()

# print(calc.add(4,3))
# print(calc.subtract(5,3))

# Class variable vs instance variable
# class Server:

#     operating_system = "Linux"

#     def __init__(self, hostname):
#         self.hostname = hostname


# server1 = Server("web01")
# server2 = Server("web02")

# print(server1.hostname)
# print(server2.hostname)

# print(server1.operating_system)
# print(server2.operating_system)