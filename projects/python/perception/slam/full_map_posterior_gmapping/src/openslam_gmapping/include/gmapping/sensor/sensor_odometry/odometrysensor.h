/*
 * Copyright 2020-2024 OpenDR European Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef ODOMETRYSENSOR_H
#define ODOMETRYSENSOR_H

#include <gmapping/sensor/sensor_base/sensor.h>
#include <string>

namespace GMapping {

  class OdometrySensor : public Sensor {
  public:
    OdometrySensor(const std::string &name, bool ideal = false);

    inline bool isIdeal() const { return m_ideal; }

  protected:
    bool m_ideal;
  };

};  // namespace GMapping

#endif
