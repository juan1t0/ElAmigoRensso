#include <iostream>
#include <vector>

using namespace std;

int modulo(int a,int b){
	int q,r;
	q=a/b;
	r=a-(q*b);
	if(r<0){
		q--;
		r+=b;
	}
	return r;
}

int euclides(int a,int b){
	int r=modulo(a,b);
	while(r>0){
		a=b;
		b=r;
		r=modulo(a,b);
	}
	return b;
}
int inversoMult(int a,int b){
	int u0=1, v0=0, u1=0, v1=1,q ,r ,u ,v;
	while(b>0){
		q=a/b;
		r=modulo(a,b);
		a=b;
		b=r;
		u=u0-q*u1;
		v=v0-q*v1;
		u0=u1;
		u1=u;
		v0=v1;
		v1=v;
	}
	return u0;
}
void TRC(void){
	cout<<"Teorema del Resto Chino \n"<<"ingrese sus valores para a_i y m_i \n"<<"x=a_i mod m_i"<<"al terminar una ecuacion ingrese 0\n"<<"para dejar de agregar valores ingrese -1\n"<<endl;
	vector<int> a;
	vector<int> p;
	int o;
	while(o != -1){
		o=0;
		cin>>o;
		a.push_back(o);
		cin>>o;
		p.push_back(o);
		cin>>o;
	}
	
	vector<int> q;
	vector<int> Pi;
	int P=1,i;
	int sizz = p.size();
	for(i = 0 ; i < sizz ; i++)
		cout<<"X = "<<a[i]<<" mod "<<p[i]<<endl;
	cout<<endl;
	
	for(i = 0 ; i < sizz ; i++)
		P *= p[i];
	cout<<"El producto de los modulos es:"<<P<<endl;
	for(i = 0 ; i < sizz ; i++){
		Pi.push_back(P/p[i]);
		q.push_back(inversoMult(Pi[i],p[i]));
	}
	int R;
	for(i=0;i<sizz;i++)
		R+=modulo(a[i]*q[i]*Pi[i],P);
	R = modulo(R,P);
	
}
int main(void)
{
	TRC();
	return 0;
}
