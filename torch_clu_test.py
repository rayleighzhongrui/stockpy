import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F
# 假数据
n_data = torch.ones(100, 2)         # 数据的基本形态
x0 = torch.normal(2*n_data, 1)      # 类型0 x data (tensor), shape=(100, 2)
y0 = torch.zeros(100)               # 类型0 y data (tensor), shape=(100, )
x1 = torch.normal(-2*n_data, 1)     # 类型1 x data (tensor), shape=(100, 1)
y1 = torch.ones(100)                # 类型1 y data (tensor), shape=(100, )

# 注意 x, y 数据的数据形式是一定要像下面一样 (torch.cat 是在合并数据)
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)  # FloatTensor = 32-bit floating
y = torch.cat((y0, y1), ).type(torch.LongTensor)    # LongTensor = 64-bit integer

#plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(),s=100, lw=0, cmap='RdYlGn')
#plt.show()
#construct the Net
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.out = torch.nn.Linear(n_hidden, n_output)
    def forward(self, x):
        x = F.relu(x)
        x = self.out(x)
        return x
net = Net(n_feature=2, n_hidden=10, n_output=2)
#print(net)
optimezer = torch.optim.SGD(net.parameters(), lr=0。02)
loss_func = torch.nn.CrossEntropyLoss()

for i in range(100):
    out = net(x)
    loss = loss_func(out,y)
    optimezer.zero_grad()
    loss.backward()
    optimezer.step()
    
