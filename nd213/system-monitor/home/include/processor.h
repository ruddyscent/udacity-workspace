#ifndef PROCESSOR_H
#define PROCESSOR_H

class Processor {
 public:
  float Utilization();  // DONE: See src/processor.cpp

  // DONE: Declare any necessary private members
 private:
    float prev_non_idle_time = 0.0;
    float prev_total_time = 0.0;
};

#endif