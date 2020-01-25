import os



class Image:
    def __init__(self, args):
        self.size = args["size"]
        self.max_color_val = args["max_color_val"]
        self.color_data = args["color_data"]

    def save_to_ppm(self, filename):
        if os.path.exists(filename):
            os.unlink(filename)

        with open(filename, 'w') as f:
            f.write("P3 {} {}\n".format(self.size[0], self.size[1]))
            f.write("{}\n".format(self.max_color_val))
            for r in self.color_data:
                for i, c in enumerate(r):
                    if (i < self.size[0] - 1):
                        f.write("{} {} {} ".format(c[0], c[1], c[2]))
                    else:
                        f.write("{} {} {}".format(c[0], c[1], c[2]))
                f.write("\n")

        print("file saved as {}".format(filename))
