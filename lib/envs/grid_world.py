import numpy as np
from gym.envs.toy_text import discrete


class GridWorld(discrete.DiscreteEnv):

    metadata = {
        'render.modes': ['human', 'ansi']
    }

    def __init__(self):
        nS = 16
        nA = 4
        P = {
            0: {
                0: [(1.0, 0, -1.0, False)],
                1: [(1.0, 4, -1.0, False)],
                2: [(1.0, 1, -1.0, False)],
                3: [(1.0, 0, -1.0, False)]
            },
            1: {
                0: [(1.0, 1, -1.0, False)],
                1: [(1.0, 5, -1.0, False)],
                2: [(1.0, 2, -1.0, False)],
                3: [(1.0, 0, -1.0, False)]
            },
            2: {
                0: [(1.0, 2, -1.0, False)],
                1: [(1.0, 6, -1.0, False)],
                2: [(1.0, 3, -1.0, False)],
                3: [(1.0, 1, -1.0, False)]
            },
            3: {
                0: [(1.0, 3, -1.0, False)],
                1: [(1.0, 7, -1.0, False)],
                2: [(1.0, 3, -1.0, False)],
                3: [(1.0, 2, -1.0, False)]
            },
            4: {
                0: [(1.0, 0, -1.0, True)],
                1: [(1.0, 8, -1.0, False)],
                2: [(1.0, 5, -1.0, False)],
                3: [(1.0, 4, -1.0, False)]
            },
            5: {
                0: [(1.0, 1, -1.0, False)],
                1: [(1.0, 9, -1.0, False)],
                2: [(1.0, 6, -1.0, False)],
                3: [(1.0, 4, -1.0, False)]
            },
            6: {
                0: [(1.0, 2, -1.0, False)],
                1: [(1.0, 10, -1.0, False)],
                2: [(1.0, 7, -1.0, False)],
                3: [(1.0, 5, -1.0, False)]
            },
            7: {
                0: [(1.0, 3, -1.0, False)],
                1: [(1.0, 11, -1.0, False)],
                2: [(1.0, 7, -1.0, False)],
                3: [(1.0, 6, -1.0, False)]
            },
            8: {
                0: [(1.0, 4, -1.0, False)],
                1: [(1.0, 12, -1.0, False)],
                2: [(1.0, 9, -1.0, False)],
                3: [(1.0, 8, -1.0, False)]
            },
            9: {
                0: [(1.0, 5, -1.0, False)],
                1: [(1.0, 13, -1.0, False)],
                2: [(1.0, 10, -1.0, False)],
                3: [(1.0, 8, -1.0, False)]
            },
            10: {
                0: [(1.0, 6, -1.0, False)],
                1: [(1.0, 14, -1.0, False)],
                2: [(1.0, 11, -1.0, False)],
                3: [(1.0, 9, -1.0, False)]
            },
            11: {
                0: [(1.0, 7, -1.0, False)],
                1: [(1.0, 15, -1.0, True)],
                2: [(1.0, 11, -1.0, False)],
                3: [(1.0, 10, -1.0, False)]
            },
            12: {
                0: [(1.0, 8, -1.0, False)],
                1: [(1.0, 12, -1.0, False)],
                2: [(1.0, 13, -1.0, False)],
                3: [(1.0, 12, -1.0, False)]
            },
            13: {
                0: [(1.0, 9, -1.0, False)],
                1: [(1.0, 13, -1.0, False)],
                2: [(1.0, 14, -1.0, False)],
                3: [(1.0, 12, -1.0, False)]
            },
            14: {
                0: [(1.0, 10, -1.0, False)],
                1: [(1.0, 14, -1.0, False)],
                2: [(1.0, 15, -1.0, True)],
                3: [(1.0, 13, -1.0, False)]
            },
            15: {
                0: [(1.0, 15, 0.0, True)],
                1: [(1.0, 15, 0.0, True)],
                2: [(1.0, 15, 0.0, True)],
                3: [(1.0, 15, 0.0, True)]
            }
        }

        isd = np.array([
            0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
            0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
            0.0625, 0.0625
        ])

        super(GridWorld, self).__init__(nS, nA, P, isd)
