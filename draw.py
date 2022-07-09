# import matplotlib.pyplot as plt
# import numpy as np
# pre = np.loadtxt('prediction.txt')
# label_reg = np.loadtxt('label.txt')

# for i in range(0,len(pre) - 200,200):
#     # plt.rcParams['figure.figsize'] = (80.0, 4.0)
#     cut_pre = pre[i: i + 200]
#     cut_label = label_reg[i: i + 200]
#     fig, ax = plt.subplots()
#     ax.plot(np.arange(len(cut_pre)), cut_pre, label='pre')
#     ax.plot(np.arange(len(cut_label)), cut_label, label='label_reg')
#     ax.legend()
#     path = 'pic/'+ str(i/200) + '_img.png'
#     plt.savefig(path)
#     print('result store in: ',path)

for i in range(41):
    path = r'!['+ str(i) + r".0_img](C:\Users\lby\Desktop\ADARNN\GBRT-for-TSF\pic" + r'\\'+ str(i) + r'.0_img.png)'
    print(path)