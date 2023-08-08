# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import torch

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = torch.arange(12)
    print(x)
    print(x.shape)
    print(x.numel())
    X = x.reshape(3, 4)
    print(X)
    x = torch.tensor([1.0, 2, 4, 8])
    y = torch.tensor([2, 2, 2, 2])
    print(x + y, x - y, x * y, x / y, x ** y)  # **运算符是求幂运算
    X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
    Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    print(torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1))

    #广播机制
    a = torch.arange(3).reshape((3, 1))
    b = torch.arange(2).reshape((1, 2))
    print(a, b)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
