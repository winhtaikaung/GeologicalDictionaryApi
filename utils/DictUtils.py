from model.Word import A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z


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