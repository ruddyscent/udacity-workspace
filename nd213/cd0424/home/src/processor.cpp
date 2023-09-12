#include "processor.h"

#include <fstream>
#include <string>

#include "linux_parser.h"

using namespace std;

// DONE: Return the aggregate CPU utilization
float Processor::Utilization() {
  float utilization = 0.0;
  ifstream stream(LinuxParser::kProcDirectory + LinuxParser::kStatFilename);
  if (stream.is_open()) {
    string cpu, user, nice, system, idle, iowait, irq, softirq, steal, guest,
        guest_nice;
    stream >> cpu >> user >> nice >> system >> idle >> iowait >> irq >>
        softirq >> steal >> guest >> guest_nice;
    if (cpu == "cpu") {
      float idle_time = stof(idle) + stof(iowait);
      float non_idle_time = stof(user) + stof(nice) + stof(system) + stof(irq) +
                            stof(softirq) + stof(steal);
      float total_time = idle_time + non_idle_time;
      utilization =
          (non_idle_time - prev_non_idle_time) / (total_time - prev_total_time);

      // Store the current values for the next iteration
      prev_non_idle_time = non_idle_time;
      prev_total_time = total_time;
    }
  }
  return utilization;
}