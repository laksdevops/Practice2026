# import platform
# print(len(dir(platform)))


# number = [1, 2, 3]
# l = dir(number)
# print(l)
# #d = dir()
# import platform
# print(platform.system())

# import platform
# print(platform.machine())

# import platform
# print(platform.python_version())

# import platform
# print(platform.processor())

# import platform
# print(platform.python_implementation())

from platform import python_version_tuple

for ver in python_version_tuple():
    print(ver, end=" ")

