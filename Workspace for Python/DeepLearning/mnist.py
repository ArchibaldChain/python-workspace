# %%
import torch.nn.functional as F
import matplotlib.pyplot as plt
import torch.optim as optim
import torch.nn as nn
import torch
import torchvision
from torchvision import transforms, datasets

# %%
train = datasets.MNIST('', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))

test = datasets.MNIST('', train=False, download=True,
                      transform=transforms.Compose([
                          transforms.ToTensor()
                      ]))

# %%
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)

# %%

# %%


class Net(nn.Module):
    def __init__(self):
        super().__init__()


net = Net()
print(net)

# %%


class a:
    '''Will be a parent class'''

    def __init__(self):
        print("initializing a")


class b(a):
    '''Inherits from a, but does not run a's init method '''

    def __init__(self):
        print("initializing b")


class c(a):
    '''Inhereits from a, but DOES run a's init method'''

    def __init__(self):
        super().__init__()
        print("initializing c")


b_ob = b()
c_ob = c()

# %%


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


net = Net()
print(net)

# %%


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)


net = Net()
print(net)

X = torch.randn((28, 28))
X = X.view(-1, 28*28)
output = net(X)
print(output)

# %%

loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

# %%
for epoch in range(3):  # 3 full passes over the data
    for data in trainset:  # `data` is a batch of data
        X, y = data  # X is the batch of features, y is the batch of targets.
        # sets gradients to 0 before loss calc. You will do this likely every step.
        net.zero_grad()
        # pass in the reshaped batch (recall they are 28x28 atm)
        output = net(X.view(-1, 784))
        loss = F.nll_loss(output, y)  # calc and grab the loss value
        loss.backward()  # apply this loss backwards thru the network's parameters
        optimizer.step()  # attempt to optimize weights to account for loss/gradients
    print(loss)  # print loss. We hope loss (a measure of wrong-ness) declines!

# %%
correct = 0
total = 0

with torch.no_grad():
    for data in testset:
        X, y = data
        output = net(X.view(-1, 784))
        # print(output)
        for idx, i in enumerate(output):
            #print(torch.argmax(i), y[idx])
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print("Accuracy: ", round(correct/total, 3))

# %%

plt.imshow(X[0].view(28, 28))
plt.show()

print(torch.argmax(net(X[0].view(-1, 784))[0]))
