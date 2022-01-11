import matplotlib.pyplot as plt

data = {'step1':[], 'step2':[]}

with open("result.txt") as f:
    while 1:
        x = f.readline()
        # data.append(x)
        if x == "":
            break
        if x[-1] == '\n':
            x = x[:len(x)-1]
        x = x.split()
        data['step1'].append(int((x[6])[:-1]))
        data['step2'].append(int((x[10])[:-1]))

def graph(x,title):
    plt.plot(x, label='step1')
    plt.title(title)
    plt.xlabel('Combination_Number')
    plt.ylabel('Epochs')
    plt.savefig(title+'.png')
    plt.show()

graph(data['step1'], 'Speaker Combination vs Epochs (Step1)')
graph(data['step2'], 'Speaker Combination vs Epochs (Step2)')

# print(data)