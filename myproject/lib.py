# my own package
import numpy as np
def try_me():
    return int(np.random.rand()*100)


if __name__ == '__main__':
    print(f'your score is {try_me()}%')
