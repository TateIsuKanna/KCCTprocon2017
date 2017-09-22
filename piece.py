import math
import numpy
class piece:
    def __init__(self,vertexes):
        self.vertexes = vertexes
        self.length = []
        for i,vertex in enumerate(vertexes):
            self.length.append(numpy.linalg.norm(vertexes[(i + 1) % len(vertexes)] - vertex))
        print("length",self.length)
        self.angles = []
        self.inner_products = []
        for i,vertex in enumerate(vertexes):
            vec_front = vertexes[(i + 1) % len(vertexes)] - vertex
            vec_back = vertex - vertexes[(i - 1 + len(vertexes)) % len(vertexes)]
            inner_product = numpy.dot(vec_front,vec_back)
            angle = math.acos(inner_product / (numpy.linalg.norm(vec_front) * numpy.linalg.norm(vec_back)))
            self.inner_products.append(inner_product)
            self.angles.append(angle)
        print("角度 ラジアン",self.angles)
        print("角度 度",[numpy.rad2deg(i) for i in self.angles])
        print("内積",self.inner_products)

    def is_on_grid(self):
        for vertex in self.vertexes:
            if not numpy.allclose(vertex,numpy.floor(vertex)):
                return False
        return True

    def is_overlapped(self,another,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        pass

    def merge(self):
        print("Yuelia35 Test")
        print("Yuelia35 Test 2")

    def rotate(self):
        print("PaperyKettleAsata TEST")