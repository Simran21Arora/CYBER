#include<iostream>
using namespace std;
int main()
{
	int a,b,j,i,c=0;
	cout<<"enter the range:";
	cin>>a>>b;
	
	for(i=a;i<=b;i++)
	{
		c=0;
		for(j=1;j<=i;j++)
		{
			if(i%j==0)
			{
				c++;
			}
		}
		if(c==2)
		{
			cout<<i<<"is a prime number\n";
		}
	}
return 0;		
}
