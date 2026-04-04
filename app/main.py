import random


def flip_coin() -> dict:
    right_dict = {0: random.uniform(0.1, 0.6),
                  1: random.uniform(0.6, 2.0),
                  2: random.uniform(2.0, 10.0),
                  3: random.uniform(10.0, 18.0),
                  4: random.uniform(18.0, 22.0),
                  5: random.uniform(22.0, 27.0),
                  6: random.uniform(18.0, 22.0),
                  7: random.uniform(10.0, 18.0),
                  8: random.uniform(2.0, 10.0),
                  9: random.uniform(0.6, 2.0),
                  10: random.uniform(0.1, 0.6)}
    # tmp = 0
    # tmp2 = 0
    # for _ in range(10000):
    #     for _ in range(10):
    #         if random.randint(0, 1) == 0:
    #             tmp += 1
    #             tmp2 += 1
    #     result_dict[tmp] += tmp
    #     tmp = 0
    # for i in range(0, 11):
    #     result_dict[i] = math.ceil(result_dict[i]/tmp2 *100)
    return right_dict

# print(flip_coin())
# def draw_gaussian_distribution_graph() -> None:
#     xpoint = np.array([1,2,3,4,5,6,7,8,9])
#     ypoint = np.array([1,2,3,4,5,6,7,8,9])
#     plt.plot(xpoint, ypoint)
#     plt.show()
#
#     plt.savefig(sys.stdout.buffer)
#     sys.stdout.flush()
