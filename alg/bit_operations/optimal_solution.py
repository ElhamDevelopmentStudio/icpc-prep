# """
# from page 102 of comp prog handbook
# """

# # def solve(arr : list[list[int]] , num_of_prods : int , num_of_days : int) -> int:
# #     res = 0
# #     for day in arr:
# #         print(min(day))
# #         res += min(day)
# #     return res



# if __name__ == "__main__":
#     num_of_products : int = 8
#     num_of_days : int = 3

#     arr : list[list[int]] = [
#         [6,9,5,2,8,9,1,6],
#         [8,2,6,2,7,5,7,2],
#         [5,3,9,7,3,5,1,4]
#     ]

#     res = solve(arr,num_of_days,num_of_products)
#     assert res == 5 , f"got {res}"
#     print(res)