import numpy as np
#
# # a1 = np.array([[1, 2, 3,4],[5, 6, 7,8]])
# # print(a1)
#
# # a1 = np.array([1, 2, 3,4],int)
# # print(a1)
# #
# # a = np.ones(4,int)
# # b = np.ones((4,1),int)
# # c = np.zeros(4,int)
# # print(a)
# # print(b)
# # print(c)
# #
# # a_2 = np.arange(0,16).reshape(4,4)
# # #4*4j矩阵
# # print(a_2[0,3])
# # # print(a_2[x == 15])
# #
# # #矩阵的创建
# #
# #
# # ##感受ai的魅力
# # matrix = np.array([
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ])
# #
# # print("原始判断矩阵:")
# # print(matrix)
# #
# # # 列归一化处理（每列元素除以该列元素之和）
# # column_sums = matrix.sum(axis=0)  # 计算每列的和
# # normalized_matrix = matrix / column_sums
# #
# # print("\n列归一化后的矩阵:")
# # print(normalized_matrix)

# 行归一化处理示例（如需行归一化，取消下面的注释）
# row_sums = matrix.sum(axis=1)  # 计算每行的和
# normalized_matrix_by_row = (matrix.T / row_sums).T
# print("\n行归一化后的矩阵:")
# print(normalized_matrix_by_row)


##不行，不学看不懂ai的代码，调试怎么办呢？？


a = np.array([[0,3,4],[1,2,5]])
print(a.sum())#所以元素求和
print(a.sum(axis=0))##各列求和
print(a.sum(axis=1))##各行
##返回的是列表
a_1 = np.sum(a,axis=0,keepdims=True)#keepdims=True 是 NumPy 中用于保持数组维度的参数
print(a_1)


b = np.array([[0,3,4],[16,4]])
c = np.array([[1,2,3],[4,5,6]])
print(b/c)
print(b/c.sum(axis=0))##b数组除以c的各列求和


#inv求矩阵的逆矩阵
#solve求解矩阵的线性方程组
#eig求矩阵的特征值和特征向量
x = np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
# x_1 = x.linalg.eig()#报错了
x_1 ,x_2= np.linalg.eig(x)##先返回特征值和特征向量
c = max(x_1)#最大的特征值
print(x_1)
print(x_2)
print(c)


###numpy库学完啦！！当然，是简单的使用
