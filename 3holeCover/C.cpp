#include <iomanip>
#include <iostream>
using namespace std;
inline struct point{
    double x;
    double y;
    double z;
};
int main(){
	int N;
	cin>>N;
	int i;
	for(i=0;i<N;i++){
        int j;
        point a[3];
		for(j=0;j<3;j++){
			cin>>a[j].x>>a[j].y>>a[j].z;
		}
		int min=x[0]<x[1]?x[0]:x[1];
		int max=x[0]>x[1]?x[0]:x[1];
		if(x[2]<min) min=x[2];
		else if(x[2]>max) max=x[2];
		double answer=(max-min)/6.0;
		cout<<"Case #"<<i+1<<": ";
		cout<<fixed<<setprecision(10)<<answer<<endl;
	}
	return 0;
}
