# vector class implementation
import matplotlib.pyplot as plt


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector3D(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x,
                        self.y - other.y,
                        self.z - other.z)

    def __mul__(self, scalar):
        """Scalar multiplication"""

        if not (isinstance(scalar, int) or isinstance(scalar, float)):
            raise TypeError(
                "You can only perform scalar multiplication with float or int")

        return Vector3D(scalar * self.x,
                        scalar * self.y,
                        scalar * self.z)

    def dot(self, other):
        """Dot product with another vector"""

        if not (isinstance(other, Vector3D)):
            raise TypeError(
                "You can only perform scalar multiplication with another vector")

        return self.x * other.x + self.y * other.y + self.z * other.z

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.quiver(0, 0, 0, self.x, self.y, self.z)

        ax.set_xlim([0, max(self.x, 1)])
        ax.set_ylim([0, max(self.y, 1)])
        ax.set_zlim([0, max(self.z, 1)])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title('3D Vector Plot')

        plt.show()


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)

v1.plot()
