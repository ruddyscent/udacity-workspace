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
        pids.push_back(pid);
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
  string category, value;
  ifstream stream(kProcDirectory + kStatFilename);
  if (stream.is_open()) {
    while (stream >> category >> value)
    {
      if (category == "processes")
      {
          return stoi(value);
      }
    }
  }
}

// DONE: Read and return the number of running processes
int LinuxParser::RunningProcesses() { 
  string category, value;
  ifstream stream(kProcDirectory + kStatFilename);
  if (stream.is_open()) {
    while (stream >> category >> value)
    {
      if (category == "procs_running")
      {
          return stoi(value);
      }
    }
  }
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
  return command; 
}

// TODO: Read and return the memory used by a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Ram(int pid[[maybe_unused]]) { return string(); }

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

// TODO: Read and return the uptime of a process
// REMOVE: [[maybe_unused]] once you define the function
long LinuxParser::UpTime(int pid[[maybe_unused]]) { return 0; }
