import math
import vec3

def create_vector(values):
    return vec3.Vect(values['components'])

def print_test(description='', test_name='', expected=0, actual=0):
    print("Results of {} {}:".format(description, test_name))
    if expected == actual:
        print("Pass")
    else:
        print("Expected {} and got {}".format(expected, actual))
    

class TestVect():
    def __init__(self, component_dict):
        self.component_dict = component_dict

    def test_magnitude(self):
        for k, v in self.component_dict.iteritems():
            vec = create_vector(v)
            print_test(v['description'], 'Magnitude', v['magnitude'], vec.magnitude())
            
        return True

    def test_normalize(self):
        for k, v in self.component_dict.iteritems():
            vec = create_vector(v)
            print_test(v['description'], 'Normalize', vec3.Vect(v['normal']).components, vec.normalize().components)

        return True

    def test_dot_product(self):
        vec1 = create_vector(self.component_dict[0])
        vec2 = create_vector(self.component_dict[1])
        answer = -27

        print_test("v1 and v2", 'Dot Product', answer, vec1.dot_product(vec2))
        print_test('v2 and v1', 'Dot Product', answer, vec2.dot_product(vec1))

        return True

    def test_add(self):
        vec1 = create_vector(self.component_dict[0])
        vec2 = create_vector(self.component_dict[1])
        answer = [4, 4, 7]

        print_test("v1 plus v2", "add", answer, (vec1 + vec2).components)

        return True

    def test_subtract(self):
        vec1 = create_vector(self.component_dict[0])
        vec2 = create_vector(self.component_dict[1])
        answer1 = [-2, -8, -11]
        answer2 = [2, 8, 11]

        print_test("v1 minus v2", "Subtract", answer1, (vec1 - vec2).components)
        print_test("v2 minus v1", "Subtract", answer2, (vec2 - vec1).components)

    def test_multiply(self):
        vec1 = create_vector(self.component_dict[0])
        scalar1 = 2
        scalar2 = -4
        answer1 = [2, -4, -4]
        answer2 = [-4, 8, 8]

        print_test("v1 times 2", "Multiply", answer1, (vec1 * scalar1).components)
        print_test("v2 times -4", "Multiply", answer2, (vec1 * scalar2).components)
    

if __name__ == '__main__':
    test_data = {0: {'description': 'basic 3d vector with negative elements',
                     'components': [1, -2, -2],
                     'magnitude': 3,
                     'normal': [1/3., -2/3., -2/3.]
                     },
                 1: {'description': 'basic 3d vector',
                     'components': [3, 6, 9],
                     'magnitude': math.sqrt(81+45),
                     'normal': [3 / math.sqrt(81+45), 6 / math.sqrt(81+45), 9 / math.sqrt(81+45)]
                     }
                 }
    test = TestVect(test_data)
    test.test_magnitude()
    test.test_dot_product()
    test.test_normalize()
    test.test_add()
    test.test_subtract()
    test.test_multiply()
