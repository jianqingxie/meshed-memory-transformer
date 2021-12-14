from .field import RawField, Merge, ImageDetectionsField, TextField
from .dataset import COCO
from torch.utils.data import DataLoader as TorchDataLoader

class DataLoader(TorchDataLoader):
    def __init__(self, dataset, *args, **kwargs):
<<<<<<< HEAD
        super(DataLoader, self).__init__(dataset, *args, collate_fn=dataset.collate_fn(), **kwargs)
=======
        super(DataLoader, self).__init__(dataset, *args, collate_fn=dataset.collate_fn(), **kwargs)
>>>>>>> e0fe3fae68091970407e82e5b907cbc423f25df2
