from sys import version_info

py_version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
print("Version info.")
print(py_version)