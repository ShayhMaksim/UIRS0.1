class road:

    def __init__(self):
        self.PictureArr = []
        for i in range(500):
            self.PictureArr.append([])
            for j in range(500):
                if 10000 < pow(i-250, 2)+pow(j-250, 2) < 40000:
                    self.PictureArr[i].append(0)
                else:
                    self.PictureArr[i].append(255)

