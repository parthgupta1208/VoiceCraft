
#include <iostream>

using namespace std;

int main() {
   int n;
   float total=0, avg;
   cout << "Enter the number of students: ";
   cin >> n;
   int marks[n];
   for(int i=0; i<n; i++) {
      cout << "Enter marks of student " << i+1 << ": ";
      cin >> marks[i];
      total += marks[i];
   }
   avg = total/n;
   cout<< "Total marks = " << total << endl;
   cout<< "Average marks = " << avg << endl;
   return 0;
}
