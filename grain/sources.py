# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""APIs for reading data from various file formats."""


# pylint: disable=g-importing-member
# pylint: disable=g-multiple-import
# pylint: disable=unused-import

# Note to developers:
#  - When adding a new OSS data source make the format lib dependency optional
#    by lazily importing the source and providing an extra installation, e.g.
#    `pip install grain[parquet]`. This will allow users to avoid installing
#    all supported format dependencies.
from grain._src.python.data_sources import (
    ArrayRecordDataSource,
    SharedMemoryDataSource,
    RandomAccessDataSource,
    RangeDataSource,
)
