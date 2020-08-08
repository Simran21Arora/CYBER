#include<iostream>
#include<string>
using namespace std;
int main()
{
	int i,c=0,l;
	string s;
	cout<<"enter the string\n";
	getline(cin,s);
	
	l=s.length();
	
	for(i=0;i<l/2;i++)
	{
	    if(s[i]==s[l-i-1])
	    {
	    	c++;
		}
	}
	if(c==i)
	{
		cout<<s<<" is a palindrome string";
	}
	else     
	{
		cout<<s<<" is not a palindrome string";
	}
	return 0;
}
