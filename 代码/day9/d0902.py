# 多维列表的遍历访问,使用for循环方法
books = [['Python核心编程',79],['Python基础教程',56],['Python编程手册',98]]
for book in books:
    for x in book:
        print(x,end='')
    print()


# # 使用while循环方法,实现多维列表的遍历访问
# books = [['Python核心编程',79],['Python基础教程',56],['Python编程手册',98]]
# x = 0
# while x < len(books):
#     y = 0
#     while y < len(books[x]):
#         print(books[x][y],end='')
#         y += 1
#     print()
#     x += 1
