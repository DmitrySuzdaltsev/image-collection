import os
import numpy as np

from image_transform import ImageTransform
from utils import get_config


class ImageCollection:
    def __init__(self, config_path=None, config=None):
        self._cfg = config or get_config(config_path)
        self._transform = ImageTransform(self._cfg.width, self._cfg.height)

        self.card_deck_names = (
            self._cfg.card_decks or
            [d.name for d in os.scandir(self._cfg.img_dir) if d.is_dir()])
        self._images = self._load_images()
        self.labels = list(self._images.keys())

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.get_deck()[key]

        elif isinstance(key, int):
            return list(self.get_deck().values())[key]

        elif isinstance(key, slice):
            print(key.start, key.stop, key.step)
            start, stop, step = key.start, key.stop, key.step
            return list(self.get_deck().values())[start:stop:step]

    def __len__(self):
        return len(self._images)

    def get_deck(self, name=None):
        if name:
            deck = name
        else:
            deck = np.random.choice(self.card_deck_names)
        return self._images[deck]

    def _load_images(self):
        img_dir = self._cfg.img_dir

        images = {}
        for deck in self.card_deck_names:
            img_files = os.listdir(os.path.join(img_dir, deck))
            images[deck] = {}

            for filename in img_files:
                img_path = os.path.join(img_dir, deck, filename)
                img = self._transform.load(img_path)
                img = self._transform.resize(img)
                key, _ = os.path.splitext(filename)
                images[deck][key] = img
        return images


if __name__ == "__main__":
    ic = ImageCollection('config.yml')
    ic['KH'].show()
