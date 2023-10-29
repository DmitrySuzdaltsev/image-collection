import PIL


class ImageTransform:
    def __init__(self, desired_width, desired_height, lock_aspect_ratio=True):
        self.desired_width = desired_width
        self.desired_height = desired_height
        self.lock_aspect_ratio = lock_aspect_ratio

    def load(self, filepath):
        return PIL.Image.open(filepath)

    def resize(self, image, size=None):
        if size:
            desired_width, desired_height = size
        else:
            desired_width = self.desired_width
            desired_height = self.desired_height

        if self.lock_aspect_ratio:
            original_width, original_height = image.size
            ratio = max(desired_width / original_width,
                        desired_height / original_height)
            desired_width = original_width * ratio
            desired_height = original_height * ratio

        return image.resize((int(desired_width), int(desired_height)),
                            PIL.Image.Resampling.LANCZOS)
