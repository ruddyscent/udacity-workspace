#include <dirent.h>
#include <unistd.h>
#include <sstream>
#include <string>
#include <vector>

#include "linux_parser.h"

using std::getline;
using std::ifstream;
using std::replace;
using std::stof;
using std::string;
using std::to_string;
using std::vector;

// DONE: An example of how to read data from the filesystem
string LinuxParser::OperatingSystem() {
  string line;
  string key;
  string value;
  ifstream filestream(kOSPath);
  if (filestream.is_open()) {
    while (getline(filestream, line)) {
      replace(line.begin(), line.end(), ' ', '_');
      replace(line.begin(), line.end(), '=', ' ');
      replace(line.begin(), line.end(), '"', ' ');
      std::istringstream linestream(line);
      while (linestream >> key >> value) {
        if (key == "PRETTY_NAME") {
          replace(value.begin(), value.end(), '_', ' ');
          return value;
        }
      }
    }
  }
  return value;
}

// DONE: An example of how to read data from the filesystem
string LinuxParser::Kernel() {
  string os, kernel, version;
  string line;
  ifstream stream(kProcDirectory + kVersionFilename);
  if (stream.is_open()) {
    getline(stream, line);
    std::istringstream linestream(line);
    linestream >> os >> version >> kernel;
  }
  return kernel;
}

// BONUS: Update this to use std::filesystem
vector<int> LinuxParser::Pids() {
  vector<int> pids;
  DIR* directory = opendir(kProcDirectory.c_str());
  struct dirent* file;
  while ((file = readdir(directory)) != nullptr) {
    // Is this a directory?
    if (file->d_type == DT_DIR) {
      // Is every character of the name a digit?
      string filename(file->d_name);
      if (std::all_of(filename.begin(), filename.end(), isdigit)) {
        int pid = stoi(filename);
        pids.emplace_back(pid);
      }
    }
  }
  closedir(directory);
  return pids;
}

// DONE: Read and return the system memory utilization`
float LinuxParser::MemoryUtilization() { 
  string category, value, unit;
  float mem_total, mem_free;
  ifstream stream(kProcDirectory + kMeminfoFilename);
  if (stream.is_open()) {
    while (stream >> category >> value >> unit)
    {
      if (category == "MemTotal:")
      {
          mem_total = stof(value);
      }
      else if (category == "MemFree:")
      {
          mem_free = stof(value);
      }
    }
  }
  return (mem_total - mem_free) / mem_total;
}

// DONE: Read and return the system uptime
long LinuxParser::UpTime() { 
  string uptime, idle_time;
  ifstream stream(kProcDirectory + kUptimeFilename);
  if (stream.is_open()) {
    stream >> uptime >> idle_time;
  }
  return stol(uptime);
 }

// TODO: Read and return the number of jiffies for the system
long LinuxParser::Jiffies() { return 0; }

// TODO: Read and return the number of active jiffies for a PID
// REMOVE: [[maybe_unused]] once you define the function
long LinuxParser::ActiveJiffies(int pid[[maybe_unused]]) { return 0; }

// TODO: Read and return the number of active jiffies for the system
long LinuxParser::ActiveJiffies() { return 0; }

// TODO: Read and return the number of idle jiffies for the system
long LinuxParser::IdleJiffies() { return 0; }

// TODO: Read and return CPU utilization
vector<string> LinuxParser::CpuUtilization() { return {}; }

// DONE: Read and return the total number of processes
int LinuxParser::TotalProcesses() { 
  int total_processes = 0;
  string category, value;
  ifstream stream(kProcDirectory + kStatFilename);
  if (stream.is_open()) {
    while (stream >> category >> value)
    {
      if (category == "processes")
      {
          total_processes = stoi(value);
          break;
      }
    }
  }
  return total_processes;
}

// DONE: Read and return the number of running processes
int LinuxParser::RunningProcesses() {
  int running_processes = 0;
  string category, value;
  ifstream stream(kProcDirectory + kStatFilename);
  if (stream.is_open()) {
    while (stream >> category >> value)
    {
      if (category == "procs_running")
      {
        running_processes = stoi(value);
      }
    }
  }
  return running_processes;
}

// DONE: Read and return the command associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Command(int pid) {
  ifstream stream(kProcDirectory + "/" + to_string(pid) + kCmdlineFilename);
  string command;
  if (stream.is_open()) {
    string line;
    getline(stream, command);
  }

  if (command.size() > 40)
  {
    command = command.substr(0, 37) + "...";
  }
  return command;
}

// DONE: Read and return the memory used by a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Ram(int pid[[maybe_unused]]) {
  ifstream stream(kProcDirectory + "/" + to_string(pid) + kStatusFilename);
  string ram;
  if (stream.is_open()) {
    string line;
    string category, value;
    while (getline(stream, line))
    {
      std::istringstream linestream(line);
      linestream >> category >> value;
      // According to the following link, VmRSS is the correct one to use
      // https://man7.org/linux/man-pages/man5/proc.5.html
      if (category == "VmRSS:")
      {
        ram = value;
        break;
      }
    }
  }
  return ram;
 }

// DONE: Read and return the user ID associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Uid(int pid) {
  ifstream status_stream(kProcDirectory + "/" + to_string(pid) + kStatusFilename);
  string uid;
  if (status_stream.is_open()) {
    string line;
    string category, value;
    while (getline(status_stream, line))
    {
      std::istringstream linestream(line);
      linestream >> category >> value;
      if (category == "Uid:")
      {
        uid = value;
        break;
      }
    }
  }

  return uid;
 }

// DONE: Read and return the user associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::User(int pid) { 
  string uid = Uid(pid);

  string user;
  ifstream password_stream(kPasswordPath);
  if (password_stream.is_open()) {
    string line;
    string x, uid_tmp;
    while (getline(password_stream, line))
    {
      std::replace(line.begin(), line.end(), ':', ' ');
      std::istringstream linestream(line);
      linestream >> user >> x >> uid_tmp;
      if (uid == uid_tmp)
      {
        break;
      }
    }
  }

  return user;
}

float LinuxParser::CpuUtilization(int pid, float &prev_non_idle_time, float &prev_total_time) {
  float result = 0;
  ifstream stream(kProcDirectory + "/" + to_string(pid) + kStatFilename);
  if (stream.is_open()) {
    string line;
    getline(stream, line);
    std::istringstream linestream(line);
    string value;
    vector<string> cpu_utilization;
    while (linestream >> value)
    {
      cpu_utilization.emplace_back(value);
    }
    float utime = stof(cpu_utilization[13]);
    float stime = stof(cpu_utilization[14]);
    // float cutime = stof(cpu_utilization[15]);
    // float cstime = stof(cpu_utilization[16]);
    float total_time = stof(cpu_utilization[21]);

    float non_idle_time = utime + stime;
    float delta_non_idle_time = non_idle_time - prev_non_idle_time;
    float delta_total_time = total_time - prev_total_time;

    prev_non_idle_time = non_idle_time;
    prev_total_time = total_time;
    
    result = delta_non_idle_time / delta_total_time;
  }
  return result;
}

float LinuxParser::CpuUtilization(int pid) {
  float uptime = UpTime();
  float hertz = sysconf(_SC_CLK_TCK);
  float cpu_usage = 0;

  ifstream stream(kProcDirectory + "/" + to_string(pid) + kStatFilename);
  // vector<string> cpu_utilization;
  if (stream.is_open()) {
    string line;
    getline(stream, line);
    std::istringstream linestream(line);
    string value;
    vector<string> cpu_utilization;
    while (linestream >> value)
    {
      cpu_utilization.emplace_back(value);
    }
    float utime = stof(cpu_utilization[13]);
    float stime = stof(cpu_utilization[14]);
    float cutime = stof(cpu_utilization[15]);
    float cstime = stof(cpu_utilization[16]);
    float start_time = stof(cpu_utilization[21]);

    float total_time = utime + stime + cutime + cstime;
    float seconds = uptime - (start_time / hertz);
    cpu_usage = total_time / hertz / seconds;
  }
  return cpu_usage; 
}

// DONE: Read and return the uptime of a process
// REMOVE: [[maybe_unused]] once you define the function
long LinuxParser::UpTime(int pid) { 
  long uptime = 0;
  ifstream stream(kProcDirectory + "/" + to_string(pid) + kStatFilename);
  if (stream.is_open()) {
    string line;
    getline(stream, line);
    std::istringstream linestream(line);
    string value;
    vector<string> cpu_utilization;
    while (linestream >> value)
    {
      cpu_utilization.emplace_back(value);
    }
    uptime = stol(cpu_utilization[21]) / sysconf(_SC_CLK_TCK);
  }
  return uptime;
}