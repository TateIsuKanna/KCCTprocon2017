import math
import numpy
import copy
class piece:
    def __init__(self,vertexes):
        self.vertexes = vertexes
        self.angles = []
        for i,vertex in enumerate(vertexes):
            vec_front = vertexes[(i + 1) % len(vertexes)] - vertex
            vec_back = vertexes[(i - 1 + len(vertexes)) % len(vertexes)] - vertex
            inner_product = numpy.dot(vec_front,vec_back)
            angle = math.acos(inner_product / (numpy.linalg.norm(vec_front) * numpy.linalg.norm(vec_back)))
            if is_cross(vertexes,vertex,vec_front + vec_back) == False:
                angle = 2 * math.pi - angle
            self.angles.append(angle)
        print("角度 度",[numpy.rad2deg(i) for i in self.angles])

    def is_on_grid(self):
        """
		ピースの頂点がグリッド上に存在するかどうか判定します
		"""
        return numpy.allclose(self.vertexes,numpy.floor(self.vertexes))

    def is_overlapped(self,another,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        """枠selfに対して結合した時にピースが重なるか判定します

        another: piece
            ピース
        self_vertex1:
            枠の辺の頂点の番号，ピースの頂点 another_vertex1と重なる．
        self_vertex2:
            枠の辺のもうひとつの頂点の番号
        another_vertex1:
            ピースの辺の頂点の番号
        another_vertex2:
            ピースの辺のもうひとつの頂点の番号
        """
        shifted_another_piece_vertexes=another.vertexes-(another.vertexes[another_vertex1]-self.vertexes[self_vertex1])
        self_search_vertex2_list=numpy.concatenate((self.vertexes[1:],self.vertexes[0:1]))
        for i,self_search_vertex1 in enumerate(self.vertexes):
            self_search_vertex2=self_search_vertex2_list[i]
            if numpy.any(numpy.cross(self_search_vertex2- self_search_vertex1,shifted_another_piece_vertexes-self_search_vertex1)<0):
                return True
        return False

    def merge(self):
        print("Yuelia35 Test")

    def rotate(self):
        print("PaperyKettleAsata TEST")

    def flip(self):
        self.vertexes[:,0]*=-1
        self.vertexes[:,0]-=min(self.vertexes[:,0])

    def is_cross(self,vertexes,origin,vec_sum):
        count = 0
        for i,vertex in enumerate(vertexes):
            vertexes[i]=vertexes[i]-origin
        vec_sum = vec_sum*100
        for i,vertex in enumerate(vertexes):
            vertex_2=vertexes[(i + 1) % len(vertexes)]
            vertex_3=vertexes[(i + 2) % len(vertexes)]
            bx=vec_sum[0]
            by=vec_sum[1]
            cx=vertex[0]
            cy=vertex[1]
            dx=vertex_2[0]
            dy=vertex_2[1]
            ax = 0
            ay = 0
            ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
            tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
            tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
            td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
            #通常交差
            if (tc * td < 0) and (ta * tb < 0):
                count+=1
            #頂点パターン1-3
            if (td == 0):
                #交差パターン3
                if(ta == 0 and tb == 0 and tc == 0 and td == 0):
                    count = count
                #交差パターン2
                elif(is_cross_2(0,0,vec_sum[0],vec_sum[1],vertex[0],vertex[1],vertex_3[0],vertex_3[1])):
                    count = count
                #交差パターン1
                else:
                    count +=1
        return count % 2 == 0

    def is_cross_2(self,ax,ay,bx,by,cx,cy,dx,dy):
        ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
        tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
        tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
        td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

        return (tc * td < 0) and (ta * tb < 0)