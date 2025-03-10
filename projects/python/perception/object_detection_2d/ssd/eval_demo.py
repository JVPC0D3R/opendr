# Copyright 2020-2024 OpenDR European Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

from opendr.perception.object_detection_2d import SingleShotDetectorLearner
from opendr.perception.object_detection_2d import WiderPersonDataset


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", help="Dataset root folder", type=str)
    parser.add_argument("--device", help="Device to use (cpu, cuda)", type=str, default="cuda", choices=["cuda", "cpu"])

    args = parser.parse_args()

    val_dataset = WiderPersonDataset(root=args.data_root, splits=['val'])

    ssd = SingleShotDetectorLearner(device=args.device)
    ssd.download(".", mode="pretrained")
    ssd.load("./ssd_default_person", verbose=True)
    ssd.eval(val_dataset)
