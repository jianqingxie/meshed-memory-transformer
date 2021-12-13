import torch

a = torch.ones(3,4)
print(a, a.shape)
print("*" * 40)
b = a.squeeze(-1)
print(b, b.size())