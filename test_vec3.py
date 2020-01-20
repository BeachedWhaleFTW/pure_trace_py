import math
import vec3

def create_vector(values):
        return vec3.Vect(values['components'])
    

class TestVect():
    def __init__(self, component_dict):
        self.component_dict = component_dict

    def test_magnitude(self):
        for k, v in self.component_dict.iteritems():
            vec = create_vector(v)
            print("Results of {} Magnitude: {}".format(v['description'], vec.magnitude() == v['magnitude']))
            
        return True

    def test_dot_product(self):
        vec1 = create_vector(self.component_dict[0])
        vec2 = create_vector(self.component_dict[1])
        answer = -27
        
        print("Results of {} and {} Dot Product: {}".format(vec1.components, vec2.components, vec1.dot_product(vec2) == answer))
        print("Results of {} and {} Dot Product: {}".format(vec2.components, vec1.components, vec2.dot_product(vec1) == answer))

        return True
    

if __name__ == '__main__':
    test_data = {0: {'description': 'basic 3d vector with negative elements',
                     'components': [1, -2, -2],
                     'magnitude': 3
                     },
                 1: {'description': 'basic 3d vector',
                     'components': [3, 6, 9],
                     'magnitude': math.sqrt(81+45)
                     }
                 }
    test = TestVect(test_data)
    test.test_magnitude()
    test.test_dot_product()
    
