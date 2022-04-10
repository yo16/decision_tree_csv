from sklearn.datasets import make_moons

def get_moons():
    return make_moons(n_samples=300, noise=0.2, random_state=0)

