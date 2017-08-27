from model.word_entity import A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z


class DictUtils(object):
    def get_model(self, title):
        return {
            'a': A,
            'b': B,
            'c': C,
            'd': D,
            'e': E,
            'f': F,
            'g': G,
            'h': H,
            'i': I,
            'j': J,
            'k': K,
            'l': L,
            'm': M,
            'n': N,
            'o': O,
            'p': P,
            'q': Q,
            'r': R,
            's': S,
            't': T,
            'u': U,
            'v': V,
            'w': W,
            'x': X,
            'y': Y,
            'z': Z
        }[title]

    def get_spreadsheet_index_by_word(self, title):
        return {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
        }[title]
