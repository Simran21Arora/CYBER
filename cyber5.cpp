#include<iostream>
#include<string>
using namespace std;
int main()
{
	string s;
	cout<<"enter the string\n";
	getline(cin,s);
	 
	int i,c,j;
	
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i]>=65 && s[i]<=90)
		{
	       	c=s[i]-64;
		}
		else if(s[i]>=97 && s[i]<=122)
		{
			c=s[i]-96;
		}
		
		for(j=0;j<c;j++){
		if(i%2==0)
		{
			cout<<"#";
		}
		else
		{
			cout<<"$";
		}
   	}
	}
return 0;	
}
