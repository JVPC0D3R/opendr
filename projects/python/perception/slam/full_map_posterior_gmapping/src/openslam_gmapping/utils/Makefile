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

OBJS= stat.o  movement.o
APPS= autoptr_test #stat_test

#LDFLAGS+= $(GSL_LIB)
#CPPFLAGS+= $(GSL_INCLUDE) -DFSLINE
CPPFLAGS+= -DFSLINE

-include ../global.mk
-include ../build_tools/Makefile.generic-shared-object

