#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <math.h>
#include <ctime>
#include <unordered_map>
using namespace std;


int main()
{
	vector<int> ns;
	for (int i = 1; i < 7; i++)
	{
		ns.push_back(pow(10, i) );
	}
	int new_n = ns[5] * 2;
	ns.push_back(new_n);

	multimap<int, string> order;
	unordered_multimap<int, string> unorder;
	string s = "value";
	for (int n : ns)
	{
		cout << "n is " << n << endl;
		srand(1);
		clock_t start_time = std::clock();
		for (int i = 0; i < n; i++)
		{
			order.insert(make_pair(rand(), s));
			
		}
		clock_t tot_time_order = std::clock() - start_time;
		cout << "multimap Time: "
			 << ((double)tot_time_order) / (double)CLOCKS_PER_SEC
			 << " seconds" << std::endl;


		srand(1);
		start_time = std::clock();
		for (int i = 0; i < n; i++)
		{
			unorder.insert(make_pair(rand(), s));

		}
		clock_t tot_time_unorder = std::clock() - start_time;
		cout << "unordered_multimap Time: "
			 << ((double)tot_time_unorder) / (double)CLOCKS_PER_SEC
			 << " seconds" << std::endl;

		cout << "different time is "
			 << (((double)tot_time_order) - ((double)tot_time_unorder)) / (double)CLOCKS_PER_SEC
			 << " seconds" << endl;
	}

}