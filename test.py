import torch
print(torch.cuda.is_available())  # Doit retourner True
print(torch.cuda.get_device_name(0))  # Doit afficher "NVIDIA GeForce RTX 3060"
print(torch.version.cuda)
