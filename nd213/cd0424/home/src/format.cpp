#include <iomanip>
#include <string>

#include "format.h"

using namespace std;

// DONE: Complete this helper function
// INPUT: Long int measuring seconds
// OUTPUT: HH:MM:SS
// REMOVE: [[maybe_unused]] once you define the function
string Format::ElapsedTime(long seconds) { 
    int hours = seconds / 3600;
    int minutes = (seconds % 3600) / 60;
    int secs = seconds % 60;
    ostringstream stream;
    stream << setw(2) << setfill('0') << hours << setw(1) << ":";
    stream << setw(2) << setfill('0') << minutes << setw(1) << ":";
    stream << setw(2) << setfill('0') << secs;
    return stream.str();
 }