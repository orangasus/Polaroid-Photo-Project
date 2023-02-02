class Polaroid_Photo:
    should_write_date = False
    def __init__(self, image, filename):
        self.image = image
        self.filename = filename

        self.name = self.get_proper_name()
        self.date = self.get_date_taken()

        self.should_write_date = (self.name == self.date) or (self.date == 'Unknown')

    def get_date_taken(self):
        try:
            return self.image.getexif()[36867]
        except:
            date = self.retrieve_date_from_image_name()
            if date == '':
                date = 'Unknown'
            return date

    def retrieve_date_from_image_name(self):
        result = ''
        if self.filename[0:4] == 'IMG_':
            if self.filename[4:12].isnumeric():
                result = self.filename[10:12] + '.' + self.filename[8:10] + '.' + self.filename[4:8]
        return result

    def show_image(self):
        self.image.show()

    def save_image(self, path):
        self.image.save(r"{0}\{1}_edit.jpg".format(path, self.name))

    def get_proper_name(self):
        result = ''
        if self.filename[0:4] == 'IMG_':
            if self.filename[4:12].isnumeric():
                result = self.filename[10:12] + '.' + self.filename[8:10] + '.' + self.filename[4:8]
        else:
            result = self.filename.split('.')[0]
        return result
