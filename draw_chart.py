import matplotlib.pyplot as plt

dilation = [0, 1, 5, 10, 15]
ours = [79.31, 80.61, 84.33, 86.12, 86.95]
denseaspp = [76.77, 78.00, 82.48, 85.09, 86.11]
aspp = [76.90, 78.14, 82.65, 85.32, 86.40]

plt.plot(dilation, ours, 'o-', color='r', label='ours_results')
plt.plot(dilation, denseaspp, '^-', color='orange', label='DenseASPP_results')
plt.plot(dilation, aspp, '+-', color='g', label='ASPP_results')
plt.xlabel('Trimap Width (pixel)')
plt.ylabel('mean mIoU (%)')
plt.title('Improvement along Object Boundaries')
plt.legend(['ours_results', 'DenseASPP_results', 'ASPP_results'])
plt.savefig('./boundary_results.png')
plt.show()